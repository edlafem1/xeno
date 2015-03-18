from flask import *
from flask_login import *
import os

app = Flask(__name__, template_folder='../')
app.secret_key = os.urandom(24)
#login_manager = LoginManager()
#login_manager.init_app(app)

from user_class import *

# Serves main landing page
@app.route('/')
def xeno_main():
    return render_template('index.html')
'''
@app.route("/login", methods=["GET", "POST"])
def login():
    pass
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        username = request.args.get('username', type=str)
        password = request.args.get('password', type=str)

        user = load_user()
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("xeno_main"))
    return render_template("login.html", form=form)
'''

# Test of ajax calls
@app.route('/ajax_test')
def ajax_test():
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


#################################################################

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


# Allows partials to be loaded
@app.route('/Partials/<partial>')
def return_partials(partial):
    return send_from_directory('../Partials', partial)


# Catches any invalid links
@app.route('/<path:path>')
def catch_all(path):
    print 'You want path: %s' % path
    print send_from_directory('../backend', 'teddy.txt')
    return ''


if __name__ == '__main__':
    print("Running app on port 5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
