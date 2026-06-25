CREATE DATABASE college_db;
USE college_db;


CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),
    FOREIGN KEY (student_id)
        REFERENCES students(student_id),
    FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
);

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

INSERT INTO departments (dept_name, hod_name, budget) VALUES
('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
('Electronics', 'Dr. Priya Nair', 620000.00),
('Mechanical', 'Dr. Suresh Iyer', 540000.00),
('Civil', 'Dr. Ananya Sharma', 430000.00);


INSERT INTO students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
VALUES
('Arjun','Mehta','arjun.mehta@college.edu','2003-04-12',1,2022),
('Priya','Suresh','priya.suresh@college.edu','2003-07-25',1,2022),
('Rohan','Verma','rohan.verma@college.edu','2002-11-08',2,2021),
('Sneha','Patel','sneha.patel@college.edu','2004-01-30',3,2023),
('Vikram','Das','vikram.das@college.edu','2003-09-14',1,2022),
('Kavya','Menon','kavya.menon@college.edu','2002-05-17',2,2021),
('Aditya','Singh','aditya.singh@college.edu','2004-03-22',4,2023),
('Deepika','Rao','deepika.rao@college.edu','2003-08-09',1,2022);


INSERT INTO courses
(course_name, course_code, credits, department_id)
VALUES
('Data Structures & Algorithms','CS101',4,1),
('Database Management Systems','CS102',3,1),
('Object Oriented Programming','CS103',4,1),
('Circuit Theory','EC101',3,2),
('Thermodynamics','ME101',3,3);


INSERT INTO enrollments
(student_id, course_id, enrollment_date, grade)
VALUES
(1,1,'2022-07-01','A'),
(1,2,'2022-07-01','B'),
(2,1,'2022-07-01','B'),
(2,3,'2022-07-01','A'),
(3,4,'2021-07-01','A'),
(4,5,'2023-07-01',NULL),
(5,1,'2022-07-01','C'),
(5,2,'2022-07-01','A'),
(6,4,'2021-07-01','B'),
(7,5,'2023-07-01',NULL),
(8,1,'2022-07-01','A'),
(8,3,'2022-07-01','B');

INSERT INTO professors
(prof_name, email, department_id, salary)
VALUES
('Dr. Anand Krishnan','anand.k@college.edu',1,95000.00),
('Dr. Meena Pillai','meena.p@college.edu',1,88000.00),
('Dr. Sunil Rajan','sunil.r@college.edu',2,82000.00),
('Dr. Latha Gopal','latha.g@college.edu',3,79000.00),
('Dr. Kartik Bose','kartik.b@college.edu',4,76000.00);


SELECT * FROM departments;
SELECT * FROM students;
SELECT * FROM courses;
SELECT * FROM enrollments;
SELECT * FROM professors;

-- 1NF (First Normal Form)
-- All tables contain atomic (single-valued) attributes.
-- Each column stores only one value and there are no repeating groups.
-- Example violation: Storing multiple phone numbers as
-- '9876543210,9123456789' in a single column would violate 1NF.

-- 2NF (Second Normal Form)
-- Every non-key attribute is fully functionally dependent on the entire primary key.
-- In the enrollments table, the candidate key is (student_id, course_id).
-- enrollment_date and grade depend on both student_id and course_id,
-- not on either attribute individually.
-- Therefore, the schema satisfies 2NF.

-- 3NF (Third Normal Form)
-- There are no transitive dependencies in the schema.
-- For example, storing dept_name in the students table would violate 3NF because:
-- student_id -> department_id -> dept_name
-- Instead, students stores only department_id, while dept_name is stored
-- separately in the departments table.

-- 3NF Analysis for enrollments Table
-- The enrollments table contains:
-- enrollment_id (Primary Key)
-- student_id (Foreign Key)
-- course_id (Foreign Key)
-- enrollment_date
-- grade
--
-- All non-key attributes depend directly on the primary key.
-- No non-key attribute depends on another non-key attribute.
-- Therefore, the enrollments table satisfies Third Normal Form (3NF).


ALTER TABLE students
ADD COLUMN phone_number VARCHAR(15);

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'college_db'
  AND TABLE_NAME = 'students';

ALTER TABLE courses
ADD COLUMN max_seats INT DEFAULT 60;

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'college_db'
  AND TABLE_NAME = 'courses';

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (grade IN ('A','B','C','D','F') OR grade IS NULL);

SHOW CREATE TABLE enrollments;

ALTER TABLE departments
CHANGE COLUMN hod_name head_of_dept VARCHAR(100);

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'college_db'
  AND TABLE_NAME = 'departments';

ALTER TABLE students
DROP COLUMN phone_number;

DESCRIBE students;
DESCRIBE departments;
DESCRIBE courses;
DESCRIBE enrollments;