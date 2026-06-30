"""
Task 3 - Eager Loading to Fix N+1

Without joinedload():
- SQLAlchemy first retrieves all enrollment records.
- It then executes additional SELECT queries whenever
  enrollment.student or enrollment.course is accessed.
- This results in the N+1 query problem.

With joinedload():
- SQLAlchemy retrieves enrollments, students and courses
  using a single SQL query with JOINs.
- This eliminates the extra database queries and improves
  performance.

Observed Result:
Before joinedload: Multiple SQL queries were executed.
After joinedload: A single SQL query retrieves all required data.
"""

#Task 2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from hands_on_6 import (
    Department,
    Student,
    Course,
    Enrollment
)

engine = create_engine(
    "mysql+mysqlconnector://root:Iniyan2005@localhost/college_db_orm",
    echo=True
)

from datetime import date
Session = sessionmaker(bind=engine)
session = Session()

#81
cs = Department(department_name="Computer Science")
it = Department(department_name="Information Technology")
ece = Department(department_name="Electronics")

session.add_all([cs, it, ece])
session.commit()

s1 = Student(
    first_name="Rejina",
    last_name="U",
    email="rejina@gmail.com",
    enrollment_year=2022,
    department=cs
)

s2 = Student(
    first_name="Rahul",
    last_name="K",
    email="rahul@gmail.com",
    enrollment_year=2023,
    department=cs
)

s3 = Student(
    first_name="Priya",
    last_name="M",
    email="priya@gmail.com",
    enrollment_year=2022,
    department=it
)

s4 = Student(
    first_name="Arjun",
    last_name="R",
    email="arjun@gmail.com",
    enrollment_year=2024,
    department=ece
)

s5 = Student(
    first_name="Divya",
    last_name="S",
    email="divya@gmail.com",
    enrollment_year=2023,
    department=cs
)

session.add_all([s1, s2, s3, s4, s5])
session.commit()

#82
c1 = Course(
    course_code="CS101",
    course_name="Database Systems",
    credits=4
)

c2 = Course(
    course_code="CS102",
    course_name="Operating Systems",
    credits=4
)

c3 = Course(
    course_code="CS103",
    course_name="Computer Networks",
    credits=3
)

session.add_all([c1, c2, c3])
session.commit()

e1 = Enrollment(
    student=s1,
    course=c1,
    enrollment_date=date(2022,8,10),
    grade=9.0
)

e2 = Enrollment(
    student=s2,
    course=c2,
    enrollment_date=date(2023,8,10),
    grade=8.5
)

e3 = Enrollment(
    student=s3,
    course=c1,
    enrollment_date=date(2022,8,10),
    grade=8.0
)

e4 = Enrollment(
    student=s5,
    course=c3,
    enrollment_date=date(2023,8,10),
    grade=9.5
)

session.add_all([e1,e2,e3,e4])
session.commit()

#83
students = (
    session.query(Student)
    .join(Department)
    .filter(Department.department_name == "Computer Science")
    .all()
)

print("\nStudents in Computer Science")

for student in students:
    print(student.first_name, student.last_name)

#84
'''print("\nEnrollment Details without joinedload")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )
'''
print("\nEnrollment Details (Using joinedload)")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )

#85
student = (
    session.query(Student)
    .filter_by(email="rejina@gmail.com")
    .first()
)

student.enrollment_year = 2025

session.commit()

print("Student Updated")

#86
enrollment = session.query(Enrollment).first()

session.delete(enrollment)

session.commit()

print("Enrollment Deleted")
print(session.query(Enrollment).count())

''' Django ORM Equivalent:

 enrollments = (
     Enrollment.objects
     .select_related("student", "course")
     .all()
 )
'''