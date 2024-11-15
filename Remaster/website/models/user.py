from utilities import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullabe=False)
    email = db.Column(db.String(150), unique=True, nulllable=False)
    password = db.Column(db.string(150), nullable=False)
