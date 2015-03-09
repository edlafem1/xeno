from flask import *

app = Flask(__name__, template_folder='../')


@app.route('/')
def xeno_main():
    return render_template('index.html')

# Allows stylesheets to be loaded.
# TODO  Consider finding a different way to serve static files without using flask
#       or to simplify it. i.e. with a 'static' directory
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
