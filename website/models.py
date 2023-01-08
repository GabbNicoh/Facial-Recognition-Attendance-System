from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# table for User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_num = db.Column(db.Integer, unique=True)
    password = db.Column(db.String(150))

class AttendanceSubject(db.Model):
    __tablename__ = 'AttendanceSubject'
    id = db.Column(db.Integer, primary_key=True)
    atdc_name = db.Column(db.Integer, unique=True)
    atdc_date = db.Column(db.DateTime(timezone=True), default=func.now)
    atdc_record = db.relationship('AttendanceRecord')

class LogSubject(db.Model):
    __tablename__ = 'LogSubject'
    id = db.Column(db.Integer, primary_key=True)
    log_name = db.Column(db.String(150))
    log_time = db.Column(db.DateTime(timezone=True), default=func.now)
    log_status = db.Column(db.String(150))
    log_record = db.relationship('LogRecord')

class AttendanceRecord(db.Model):
    __tablename__ = 'AttendanceRecord'
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column(db.Integer, db.ForeignKey('AttendanceSubject.id'))
    subjects = db.relationship('Subjects')

class LogRecord(db.Model):
    __tablename__ = 'LogRecord'
    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('LogSubject.id'))
    subjects = db.relationship('Subjects')
    
class Subjects(db.Model):
    __tablename__ = 'Subjects'
    id = db.Column(db.Integer, primary_key=True)
    atdc_id = db.Column(db.Integer, db.ForeignKey('AttendanceRecord.id'))
    log_id = db.Column(db.Integer, db.ForeignKey('LogRecord.id'))