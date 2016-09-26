__author__ = 'panizava'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config')

from app.models import Course, Student
db.create_all()
