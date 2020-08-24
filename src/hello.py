from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>')
def user(name):
    return 'Hello, {}!'.format(name)


@app.route("/ikea/coworkers/")
def list_coworkers():
    lc = [
        ("Lev", "Ivanov"),
        ("Linh", "Huynh"),
    ]
    return render_template("coworkers.html", coworkers_list=lc)

