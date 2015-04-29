from flask import Flask, request, flash, url_for, redirect, render_template, send_from_directory, g, abort
from flask_login import LoginManager, login_user, current_user,  login_required, logout_user
import mysql.connector as mariadb
import os
from user_class import *
from car_actions import *
from flaskext.uploads import *

import configuration
app = Flask(__name__, template_folder='../templates')

patch_request_class(app, 8 * 1024 * 1024)  # 8 megabyte file upload limit
UPLOADED_IMAGES_DEST = "../images/"


def car_dest(app):
    return "../images/cars/"
def pro_dest(app):
    return "../images/profiles/"
car_pics = UploadSet('cars', IMAGES + ("pic",), car_dest)
profile_pics = UploadSet('profilepics', IMAGES + ("pic",), pro_dest)
configure_uploads(app, [car_pics, profile_pics])

app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'


def isAdmin(current_user):
    admin_acct = False
    if current_user.acct_type == 1:
        # is admin
        admin_acct = True
    
    return admin_acct

@login_manager.user_loader
def load_user(userid):
    '''
    user_callback function for flask_login. Only seems to work when defined here.
    last_modified_by: edlafem1
    @param1 userid the id of the user you want data for.
    @return a user object filled with pertinent data from the database or None if there is no user with the given id.
    '''
    # get user info from DB here, validate userid is a valid User in DB.
    user = User(userid)
    #print vars(user)
    if user.exists is False:
        return None
    return user

'''
@app.route('/')
@login_required
def xeno_main():
    # Serves main landing page
    return render_template('index.tpl')
'''

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user is not None and current_user.is_authenticated():
        flash('Already logged in.')
        return redirect(request.args.get('next') or url_for('dashboard_view'))
    if request.method == 'GET':
        return render_template('login.tpl', next=request.args.get('next'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.validate_credentials(username, password)

        if user is None:
            flash('Username or Password is invalid', 'error')
            return render_template('login.tpl', username=username)
        login_user(user)
        flash("Logged in successfully.")
    print request.form['next']
    return redirect(request.form['next'] or url_for('dashboard_view'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/search', methods=["GET"])
@app.route('/search/<int:page>', methods=["GET"])
@login_required
def search(page=1):
    howmany = 20
    if page == 0:
        # view all
        howmany = -1
    car_data = []
    if 'search' not in request.args:
        car_data = get_cars(page, howmany)
        return render_template('car_list.tpl', cars=car_data, admin=isAdmin(current_user))
    elif 'search' in request.args:
        car_data = get_cars(0, -1, search_params={"general": request.args['search']})
        return render_template('search.tpl', search=request.args['search'], cars=car_data, admin=isAdmin(current_user))
    
    
@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard_view():
    new_car_data = get_cars(1, 8, get_new=True)
    featured_car_data = get_cars(1, 4, get_featured=True)
    return render_template('dash.tpl', new_cars=new_car_data, featured_cars=featured_car_data, admin=isAdmin(current_user))

@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if current_user is not None and current_user.is_authenticated():
        flash('Already logged in.')
        return redirect(request.args.get('next') or url_for('search'))
    if request.method == 'GET':
        return render_template('sign_up.tpl')
    user_data = request.form
    if user_data["password"] != user_data["password2"]:
        flash("Passwords do not match")
        return render_template('sign_up.tpl', name=user_data["full_name"], email=user_data["email"])
    user_creation = User.create_new_user(user_data)
    flash("Your account has been created. Please log in.")
    return render_template('login.tpl', username=user_data["email"])


@app.route('/addcar', methods=['GET', 'POST'])
@login_required
def add_car():
    # Add car page
    if request.method == 'GET':
        if not isAdmin(current_user):
            flash("Sorry, you need to be an admin to add cars to Xeno. Try searching to see if it's already here!")
            return redirect(url_for('search'))
        return render_template('add_car.tpl', admin=isAdmin(current_user))
    # getting here means they are submiting data
    new_car_data = request.form
    car_id = add_new_car(new_car_data, current_user)
    if car_id is not False:
        if 'photo' in request.files:
            filename = car_pics.save(request.files['photo'], name=str(car_id)+"_main.pic")
            print("Photo saved: " + filename)
        flash("Thank you for adding a car!")
    else:
        flash("Something went wrong...")
    return render_template('add_car.tpl', admin=isAdmin(current_user))



#################################################################

@app.route('/accounts')
@login_required
def approve_accounts():
    # Approve accounts page
    accounts = [{"name": "John Smith",
                 "address": "0000 Street Name, State Zip",
                 "paid": "NOT PAID",
                 "approved": "NOT APPROVED"},
                {"name": "Michael Bishoff",
                 "address": "0000 Street Name, State Zip",
                 "paid": "NOT PAID",
                 "approved": "NOT APPROVED"},
                {"name": "Jane Smith",
                 "address": "0000 Street Name, State Zip",
                 "paid": "NOT PAID",
                 "approved": "NOT APPROVED"}
                ]
    return render_template('new_accounts.tpl', admin=isAdmin(current_user), accounts=accounts)


@app.route('/profile')
@login_required
def profile():
    user_info = dict()
    user_info["firstname"] = current_user.fname
    user_info["lastname"] = current_user.lname
    user_info["credits"] = current_user.credits
    user_info["email"] = current_user.id
    user_info["date_joined"] = current_user.date_joined.strftime('%m/%d/%Y')
    if current_user.suspended is False:
        user_info["suspended_until"] = ""
    else:
        user_info["suspended_until"] = current_user.suspended_til.strftime('%m/%d/%Y')

    favorite_car = current_user.get_favorite_car()

    return render_template('profile.tpl', user_data=user_info, admin=isAdmin(current_user), fav_car=favorite_car)


# Allows stylesheets to be loaded.
# TODO  Consider finding a different way to serve static files without using flask
# or to simplify it. i.e. with a 'static' directory


@app.route('/style/<sheet>')
def return_stylesheet(sheet):
    return send_from_directory('../style', sheet)
# Allows scripts to be loaded


@app.route('/scripts/<js>')
def return_script_file(js):
    return send_from_directory('../scripts', js)
# Allows images to be loaded


@app.route('/images/<image>')
def return_images(image):
    return send_from_directory('../images', image)


@app.route('/surprise/<files>')
def return_surprise(files):
    # Allows surprise to show
    return send_from_directory('../surprise', files)


@app.route('/<path:path>')
def catch_all(path):
    # Catches any invalid links
    print 'You want path: %s' % path
    return send_from_directory('../', path)
    #print send_from_directory('../backend', '404.html')
    abort(401)
    return ''


if __name__ == '__main__':
    print "Running app on port 5000"
    app.run(debug=True, host='0.0.0.0', port=5000)



@app.route('/ajax_test')
def ajax_test():
    # Test of ajax calls
    print 'Ajax Test'
    print request.json
    print request.json['var1']
    var1 = request.args.get('var1', default=0, type=int)
    var2 = request.args.get('var2', default=0, type=int)
    var3 = request.args.get('var3', default='hello world', type=str)
    print var3
    return jsonify(in_var1=var1,
                   in_var2=var2,
                   in_var3=var3)
