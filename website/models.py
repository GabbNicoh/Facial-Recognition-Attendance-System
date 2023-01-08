from . import db
from flask_login import UserMixin

# table for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_num = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))

class Attendance_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Log_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)