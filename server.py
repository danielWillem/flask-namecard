from flask import Flask
from flask import render_template

myApp = Flask(__name__)

@myApp.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    myApp.run(debug=True)