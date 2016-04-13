from flask import Flask, request, flash, url_for, redirect, render_template, send_from_directory, g, abort
from flask_login import LoginManager, login_user, current_user,  login_required, logout_user
import mysql.connector as mariadb
import os
from user_class import *
from car_actions import *
from flaskext.uploads import *
from send_email import *
import simplejson as json

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
        elif user.banned:
            flash('<span style=\'color:red;\'>Unfortunatly, this account has been banned.</span>')
            return render_template('login.tpl')
        elif user.suspended:
            flash('<span style=\'color:red;\'>We are sorry, but you have been suspended until ' +
                  user.suspended_til.strftime('%m-%d-%Y %H:%M:%S')
                  + 'GMT and will be unable to access Xeno until then.</span>')
            return render_template('login.tpl')
        login_user(user)
#        flash("Logged in successfully.")
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
        car_data = get_cars(page, howmany, isAdmin=isAdmin(current_user))
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
    reserved_car_data = get_reserved_car(current_user.db_id)
    reserved_car_names = []
    reserved_car_status = []
    
    for i in range(len(reserved_car_data)):
        car_id = reserved_car_data[i]['for_car']
        car = get_single_car(car_id, isAdmin(current_user))
        car_name = str(car["year"]) + " " + car["make"] + " " + car["model"]
        reserved_car_names.append( car_name )
        reserved_car_status.append(str(car['status']))
    
    waiting = check_waitlist(current_user.db_id)
    
    return render_template('dash.tpl',
                           reserved_car_data=reserved_car_data,
                           reserved_car_names=reserved_car_names,
                           reserved_car_status=reserved_car_status,
                           new_cars=new_car_data,
                           featured_cars=featured_car_data,
                           waiting=waiting,
                           admin=isAdmin(current_user)
                          )

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


@app.route("/write_review", methods=['POST'])
@login_required
def write_review():
    review_info = request.form
    confirm = create_review(review_info, current_user.db_id)
    flash(confirm)
    return redirect(url_for("car_profile") + review_info["car_id"] or "/car/" + review_info["car_id"])

#################################################################

@app.route('/accounts', methods=['GET', 'POST'])
@login_required
def approve_accounts():
    if not isAdmin(current_user):
        flash("Sorry, you must be an admin to see this page.")
        return redirect(url_for('search'))

    if request.method == "POST":
        retVals  ={}
        acct_id = request.json['acct_id']
        date = datetime.datetime.now()
        dateStr = "Not changed"
        ecalateStr = "Not changed"
        updated = "Err"
        if 'approved' in request.json:
            #approved = request.json['approved']
            if request.json['approved'] == "true":
                date = "CURRENT_TIMESTAMP()"
                dateStr = "Not suspended"
            else:
                date = datetime.datetime(3000, 1, 1)
                dateStr = "Banned permanently" # date.strftime("%Y-%m-%d %H:%M:%S")
            updated = admin_only_user_update(acct_id, ["suspended_until"], [date])
        elif 'suspended' in request.json:
            if request.json['suspended'] == "true":
                now = datetime.datetime.now()
                date = now + datetime.timedelta(weeks=1)
                dateStr = date.strftime("%Y-%m-%d %H:%M:%S")
            else:
                date = "CURRENT_TIMESTAMP()"
                dateStr = "Not suspended"
            updated = admin_only_user_update(acct_id, ["suspended_until"], [date])
        elif 'escalated' in request.json:
            updated = admin_only_user_update(acct_id, ["acct_type"], [request.json["escalated"]])
            ecalateStr = "Account changed to " + request.json["escalated"]

#        elif 'fixed' in request.json:
#            updated = fix_car(acct_i
            
        if updated == 0:
            retVals["suspended_until"] = dateStr #.strftime("%Y-%m-%d %H:%M:%S")
            retVals["acct_id"] = acct_id
            retVals["escalated"] = ecalateStr
            retVals["error"] = ""
        else:
            retVals["error"] = "Xeno was not able to perform the update."
            retVals["update"] = updated
        return json.dumps(retVals)
    '''
        print 'Acct Mgmt Ajax'
    var1 = request.args.get('var1', default=0, type=int)
    var2 = request.args.get('var2', default=0, type=int)
    retVals = {"in_var1": var1, "in_var2": var2}
    print retVals
    return json.dumps(retVals)
    '''
    # Approve accounts page
    accounts = get_all_users()
    # this array has name, userid, banned, suspended
    carMaintenance = get_broken_cars()
    
    return render_template('new_accounts.tpl', admin=isAdmin(current_user), accounts=accounts, carMaintenance=carMaintenance)


@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
    
    profile_pic = str(current_user.db_id) + "_profile.jpg"
    
    # Check if the user is editing their profile
    if request.method == "POST":
        if 'photo' in request.files:
            print "OS: " + str(os.path.isfile("../images/profiles/" + profile_pic))
            # Check if the user has an old profile picture
            if os.path.isfile("../images/profiles/" + profile_pic):
                os.remove("../images/profiles/" + profile_pic)
            
            profile_pic = profile_pics.save(request.files['photo'], name=str(current_user.db_id)+"_profile.jpg")
            print("Photo saved: " + profile_pic)
    
    # Check if the user has a profile picture or not
    if not os.path.isfile("../images/profiles/" + profile_pic):
        profile_pic = "blank_face.jpeg"
    
    user_info = dict()
    user_info["id"] = current_user.db_id
    user_info["profile_pic"] = profile_pic
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

    recent_activity = get_activity(current_user.db_id)
    recent_cars = []

    for activity in recent_activity:
        recent_cars.append(get_single_car(activity['car'], isAdmin(current_user)))

    return render_template('profile.tpl', user_data=user_info, admin=isAdmin(current_user), fav_car=favorite_car, activity=recent_activity, recent_cars=recent_cars)

@app.route('/car')
@app.route('/car/')
@app.route('/car/<int:id>')
@login_required
def car_profile(id=-1):
    if id == -1:
        flash("It seems you tried to view a car that isn't there.")
        return redirect(url_for('search') or '/search')
    car_data = get_single_car(id, isAdmin(current_user))
    if car_data is None:
        flash("We're sorry but something went wrong. Please try again.")
        return redirect(url_for('search') or '/search')
    reviews = get_car_reviews(id)
    unavailableDates = get_reserved_dates(id)
    return render_template('car_profile.tpl', car=car_data, reviews=reviews, admin=isAdmin(current_user),
                           blockedDates=unavailableDates)

@app.route('/car_details', methods=['POST'])
@login_required
def car_details():
    car_id = request.form["car_id"]
    if not isAdmin(current_user):
        return redirect(url_for("car_profile") + "/" + str(car_id) or '/car/' + str(car_id))
    needs_work = request.form["needs_work"]
    description = request.form["work_details"]
    result = log_work(car_id, description, current_user.db_id)
    flash("Thanks for noting this.")
    return redirect(url_for("car_profile") + str(car_id) or '/car/' + str(car_id))

@app.route('/car_status', methods=['POST'])
def car_status():
    car_id = request.json["car_id"]
    enabled = request.json["enabled"]
    car_status = 1

    if enabled == "true":
        car_status = 1
    else:
        car_status = 4

    result = update_car_status(car_id, car_status)
    if result is not None:
        flash("Thanks for noting this.")
    else:
        flash("Sorry something went wrong.")
    return redirect(url_for("car_profile") + str(car_id) or '/car/' + str(car_id))




@app.route('/reserve', methods=['POST'])
@login_required
def reserve_car():
    if "rentalDate" in request.form:
        text_date = request.form["rentalDate"]
        car_id = request.form["which_car"]
        confirm = True
        confirm = make_reservation(car_id, text_date, current_user)

        if confirm is True:
            flash("Thank you, your reservation has been made.")
            
            # Gets the car data from the DB
            car = get_single_car(car_id, isAdmin(current_user))
            car = str(car["year"]) + " " + car["make"] + " " + car["model"]
            
            emailBody = 'You reserved a ' + car + ' for ' + text_date + '! You can pick it up any time on ' + text_date + ' and you must return it at 11:59pm that night.'
            
            # Sends an email to the user
#            sendEmail(current_user.id, emailBody)
            
        else:
            flash(confirm)
            #flash("We're sorry, we could not make your reservation.")
    flash("Invalid selection. Please try again.")
    return redirect(url_for('car_profile') + str(car_id) or "/car/" + str(car_id))


@app.route('/claim', methods=['POST'])
@login_required
def claim():
    # Claims the car
    result = claim_car(current_user.db_id, request.form["car_id"])
    
    # Displays a confirmation message to the user
    if result:
        flash("Something went wrong D:")
    else:
        flash("You have claimed your car!")
    
    # Sends them back to the dashboard
    return redirect(url_for('dashboard_view'))


@app.route('/return', methods=['POST'])
@login_required
def handle_return():
    # Returns the car
    result = return_car(current_user.db_id,
                        request.form["reservation_id"],
                        request.form["car_id"])
    
    # Displays a confirmation message to the user
    if result:
        flash("Something went wrong D:")
    else:
        flash("Thank you for returning our car.")
    
    # Sends them back to the dashboard
    return redirect(url_for('dashboard_view'))


@app.route('/waitlist', methods=['POST'])
@login_required
def waitlist():
    # Checks if the user wants to join or remove the waitlist
    if int(request.form['join']):
        # Adds the user to the waitlist
        result = join_waitlist(current_user.db_id)
    
        # Displays a confirmation message to the user
        if not result:
            flash("You are already on the waitlsit.")
        else:
            flash("You have joined the waitinglist! You will receive an email once a car is available.")
    
    else:
        # Removes the user from the waitlist
        result = leave_waitlist(current_user.db_id)
        
        # Displays a confirmation message to the user
#        if not result:
        flash("You have beend removed from the waitlist.")
#       else:
#            flash("You are not on the waitlsit.")
        
    
    # Sends them back to the dashboard
    return redirect(url_for('dashboard_view'))




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




@app.route('/ajax_test')
def ajax_test():
    # Test of ajax calls
    print 'Ajax Test'
    var1 = request.args.get('var1', default=0, type=int)
    var2 = request.args.get('var2', default=0, type=int)
    retVals = {"in_var1": var1, "in_var2": var2}
    print retVals
    return json.dumps(retVals)


@app.route('/<path:path>')
def catch_all(path):
    # Catches any invalid links
    print 'You want path: %s' % path
    return send_from_directory('../', path)
    #print send_from_directory('../backend', '404.html')
    #abort(401)
    #return ''


if __name__ == '__main__':
    app.run(debug=configuration.XENO_DEBUG_MODE, host='0.0.0.0', port=configuration.XENO_PORT)
    print "Running app on port 5000"
