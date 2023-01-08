from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# table for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_num = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))

class Attendance_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now)

class Log_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)