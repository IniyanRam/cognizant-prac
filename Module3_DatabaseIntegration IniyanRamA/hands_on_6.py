from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    DECIMAL
)

from sqlalchemy.orm import declarative_base, relationship
engine = create_engine(
    "mysql+mysqlconnector://root:Iniyan2005@localhost/college_db_orm"
)

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String(100))

    students = relationship("Student", back_populates="department")

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollment_year = Column(Integer)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_code = Column(String(20))
    course_name = Column(String(100))
    credits = Column(Integer)

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )

class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.student_id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    enrollment_date = Column(Date)

    grade = Column(DECIMAL(4,2))

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )

class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))

Base.metadata.create_all(engine)
print("Tables created ")
