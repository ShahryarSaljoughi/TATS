__author__ = 'shahryar_saljoughi'

from app import db
from pytz import timezone
from datetime import time

tehran = timezone('Asia/Tehran')

# just for test:
start_time = time(8)
end_time = time(9, 30)

association_table = db.Table(
    'association',
    db.Column('courses_id', db.Integer, db.ForeignKey('courses.id')),
    db.Column('students_id', db.Integer, db.ForeignKey('students.id')),
)
# association_table.__table_args__ = {'extend_existing': True}


class Course(db.Model):

    __tablename__ = 'courses'

    name = db.Column(db.TEXT)
    code = db.Column(db.INTEGER, nullable=False)
    starts_at = db.Column(db.TIME, nullable=False)
    ends_at = db.Column(db.TIME, nullable=False)
    is_TA = db.Column(db.BOOLEAN, nullable=False, default=False)
    students = db.relationship('Student',
                               secondary=association_table,
                               back_populates='courses')

    id = db.Column(db.INTEGER, primary_key=True)


class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.INTEGER, primary_key=True, nullable=False)
    first_name = db.Column(db.TEXT)
    last_name = db.Column(db.TEXT, nullable=False)
    courses = db.relationship('Course',
                              secondary=association_table,
                              back_populates='students')