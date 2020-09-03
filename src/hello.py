from flask import Flask
from flask import render_template
import csv


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>')
def user(name):
    return 'Hello, {}!'.format(name)


@app.route("/ikea/coworkers/")
def list_coworkers():
    fileoutput = open('/Users/linh.huynh2/mylinkedin/src/coworkers.csv', 'r')
    myreader = csv.reader(fileoutput)

    lc = []
    for workerList in myreader:
        lc.append(tuple(workerList))
    return render_template("coworkers.html", coworkers_list=lc)

