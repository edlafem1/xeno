from flask import Flask, request, flash, url_for, redirect, render_template, send_from_directory, g, abort
from flask_login import LoginManager, login_user, current_user,  login_required, logout_user
import mysql.connector as mariadb
import os
from user_class import *

import configuration
app = Flask(__name__, template_folder='../templates')
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'


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
    print vars(user)
    if user.exists is False:
        return None
    return user


@app.route('/')
@login_required
def xeno_main():
    # Serves main landing page
    return render_template('index.tpl')


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user is not None and current_user.is_authenticated():
        flash('Already logged in.')
        return redirect(request.args.get('next') or url_for('search'))
    if request.method == 'GET':
        return render_template('login.tpl')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.validate_credentials(username, password)

        if user is None:
            flash('Username or Password is invalid', 'error')
            return render_template('login.tpl', username=username)
        print "User = ", vars(user)
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("xeno_main"))
    return redirect(request.args.get('next') or url_for('search'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("xeno_main"))


@app.route('/search')
@app.route('/search/<int:page>')
@login_required
def search(page=1):
    howmany = 20
    if page == 0:
        # view all
        howmany = -1
    car_data = get_cars(page, howmany)
    return render_template('search.tpl')



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


@app.route('/addcar')
def add_car():
    # Add car page
    return render_template('add_car.tpl', admin=True)


#################################################################

@app.route('/accounts')
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
    return render_template('new_accounts.tpl', admin=True, accounts=accounts)
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
    return send_from_directory('../surprise/', files)


@app.route('/<path:path>')
def catch_all(path):
    # Catches any invalid links
    print 'You want path: %s' % path
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

