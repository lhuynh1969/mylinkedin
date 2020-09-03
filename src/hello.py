from flask import Flask
from flask import render_template
<<<<<<< HEAD
import csv
=======
>>>>>>> eef86dcaa9b8eae0d5d7d74a3ab42a049102d167


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

