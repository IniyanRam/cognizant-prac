from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from typing import Optional, List
from database import engine, Base, get_db
import models
import schemas

app = FastAPI(
    title="Course Management API", 
    description="A full CRUD API for Course Management",
    version="1.0",
    contact={
        "name": "Developer",
        "email": "dev@example.com",
    }
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "API running"}

@app.post("/api/v1/courses/", response_model=schemas.CourseResponse, status_code=status.HTTP_201_CREATED, tags=['Courses'], summary="Create a new course", response_description="The created course")
async def create_course(course: schemas.CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.get("/api/v1/courses/{course_id}", response_model=schemas.CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get("/api/v1/courses/", response_model=List[schemas.CourseResponse], tags=['Courses'])
async def list_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(models.Course)
    if department_id is not None:
        query = query.filter(models.Course.department_id == department_id)
    query = query.offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@app.put("/api/v1/courses/{course_id}", response_model=schemas.CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course_update: schemas.CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    update_data = course_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(course, key, value)
        
    await db.commit()
    await db.refresh(course)
    return course

@app.delete("/api/v1/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    course = result.scalars().first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    await db.delete(course)
    await db.commit()
    return None

@app.get("/api/v1/courses/{course_id}/students/", response_model=List[schemas.StudentResponse], tags=['Courses'])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Course).filter(models.Course.id == course_id))
    if not result.scalars().first():
        raise HTTPException(status_code=404, detail="Course not found")
        
    query = select(models.Student).join(models.Enrollment).filter(models.Enrollment.course_id == course_id)
    students = await db.execute(query)
    return students.scalars().all()

def send_confirmation_email(student_email: str):
    print(f'Sending confirmation to {student_email}')

class EnrollmentCreate(schemas.EnrollmentResponse):
    pass

@app.post("/api/v1/enrollments/", response_model=schemas.EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=["Enrollments"])
async def create_enrollment(enrollment: schemas.EnrollmentResponse, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    db_enrollment = models.Enrollment(**enrollment.dict(exclude={"id"}))
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    
    student_result = await db.execute(select(models.Student).filter(models.Student.id == db_enrollment.student_id))
    student = student_result.scalars().first()
    if student:
        background_tasks.add_task(send_confirmation_email, student.email)
        
    return db_enrollment
