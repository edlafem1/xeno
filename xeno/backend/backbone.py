from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! This works!'

if __name__ == '__main__':
    print("Running app on port 5000")
    app.run(debug=True, host='0.0.0.0', port=5000)