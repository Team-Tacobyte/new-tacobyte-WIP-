from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(200))


class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id of the user associate
    bio = db.Column(db.String(500))
    website = db.Column(db.String(100))
