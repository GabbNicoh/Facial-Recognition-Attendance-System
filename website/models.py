from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# table for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_num = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))

class Attendance_Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atdc_name = db.Column(db.Integer, unique=True)
    atdc_date = db.Column(db.DateTime(timezone=True), default=func.now)
    attdc_record = db.relationship('Attendance_Record')

class Log_Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_name = db.Column(db.String(150))
    log_time = db.Column(db.DateTime(timezone=True), default=func.now)
    log_status = db.Column(db.Stringg(150))
    attdc_record = db.relationship('Log_Record')

class Attendance_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column(db.Integer, db.ForeignKey('Attendance_Subject.id'))
    subjects = db.relationship('Subjects')
    # subject_id = db.Column(db.String(40), db.ForeignKey())

class Log_Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('Attendance_Subject.id'))
    subjects = db.relationship('Subjects')
    

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column()
    log_id = db.Column()