from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from etc import settings


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql:{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'
