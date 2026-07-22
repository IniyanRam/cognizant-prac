from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: Optional[int] = None

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True

class DepartmentResponse(BaseModel):
    id: int
    name: str
    head_of_dept: str
    budget: float
    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department_id: Optional[int] = None
    enrollment_year: int

    class Config:
        from_attributes = True

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    enrollment_date: date
    grade: Optional[str] = None

    class Config:
        from_attributes = True
