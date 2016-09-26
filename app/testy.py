__author__ = 'panizava'
from models import Course, Student
from datetime import time
from app import db
t1 = time(8)
t2 = time(9, 30)

math = Course(name='math', code=123456, starts_at=t1, ends_at=t2)
ap = Course(name='ap', code=123457, starts_at=time(9, 30), ends_at=time(11))
ca = Course(name='ca', code=123458, starts_at=time(14), ends_at=time(15, 30))
dd = Course(name='digital design', code=123459, starts_at=t1, ends_at=t2)
ds = Course(name='Data Stuctures', code=123460, starts_at=time(14), ends_at=time(15, 30))
os = Course(name='Operations Systems', code=123461, starts_at=time(9, 30), ends_at=time(11))

courses = [ap, ca, dd, ds, os]
for course in courses:
    db.session.add(course)
db.session.commit()

p1 = Student(last_name='saljoughi')
p2 = Student(last_name='bakhtiari')
p3 = Student(last_name='balaboland')

students =list()
students.append(p1)
students.append(p2)
students.append(p3)

for student in students:
    db.session.add(student)
db.session.commit()

