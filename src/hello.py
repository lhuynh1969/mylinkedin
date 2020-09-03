import csv

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<name>')
def user(name):
    return 'Hello, {}!'.format(name)


@app.route("/ikea/coworkers/")
def list_coworkers():
    lc = []
    with open('static/coworkers.csv', 'r') as fileoutput:
        myreader = csv.reader(fileoutput)
        for workerList in myreader:
            lc.append(tuple(workerList))

    return {
        "envelope": lc,
    }

