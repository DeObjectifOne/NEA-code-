from utilities import db
from sqlalchemy.sql import func

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(150), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), default=func.now())
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    duration = db.Column(db.Integer, nullable=True)
    difficulty = db.Column(db.Integer, nullable=True)
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))
