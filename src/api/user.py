from flask import request

from src.app import app, db
from src.models.user import User


@app.route('/users/', methods=['POST'])
def user_create():
    data = request.form
    user = User(
        username=data['username'],
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name'],
    )
    db.session.add(user)
    db.session.commit()
    return 'User created', 200


@app.route('/users/<int:uid>', methods=['GET'])
def user_get(uid):
    user = db.session.query(User).get(uid)
    return user, 200
