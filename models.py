from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from taskapp import app

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = "task"
    id = db.Column('id', db.Integer, primary_key=True)
    priority_id = db.Column('priority_id', db.Integer, db.ForeignKey('priority.id'))
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)
    is_done = db.Column('is_done', db.Boolean, default=False)

    priority = db.relationship('Priority', foreign_keys=priority_id, backref="tasks")


class Priority(db.Model):
    __tablename__ = "priority"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    value = db.Column('value', db.Integer)

