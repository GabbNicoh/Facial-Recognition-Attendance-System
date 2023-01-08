from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# table for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_num = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))

class AttendanceSubject(db.Model):
    __tablename__ = 'attendancesubject'
    id = db.Column(db.Integer, primary_key=True)
    atdc_name = db.Column(db.Integer, unique=True)
    atdc_date = db.Column(db.DateTime(timezone=True), default=func.now)
    atdcrecord = db.relationship('attendancerecord')

class Log_Subject(db.Model):
    __tablename__ = 'logsubject'
    id = db.Column(db.Integer, primary_key=True)
    log_name = db.Column(db.String(150))
    log_time = db.Column(db.DateTime(timezone=True), default=func.now)
    log_status = db.Column(db.Stringg(150))
    attdc_record = db.relationship('logrecord')

class AttendanceRecord(db.Model):
    __tablename__ = 'attendancerecord'
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column(db.Integer, db.ForeignKey('attendancesubject.id'))
    subjects = db.relationship('subjects')

class Log_Record(db.Model):
    __tablename__ = 'logrecord'
    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('Attendance_Subject.id'))
    subjects = db.relationship('subjects')
    
class Subjects(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column()
    log_id = db.Column()