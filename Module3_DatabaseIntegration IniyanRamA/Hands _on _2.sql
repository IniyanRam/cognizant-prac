 -- 15
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

-- 16
INSERT INTO students
(first_name, last_name, email, date_of_birth, department_id, enrollment_year)
VALUES
('Iniyan','Ram','Iniyan.ram@college.edu','2005-12-13',1,2025),
('harsh','Bothra','harsh.bothra@college.edu','2005-01-25',1,2025);

-- 17
UPDATE enrollments SET grade = 'B' WHERE student_id = 5 AND course_id = 1;

select * from enrollments where student_id=5 and course_id=1;

-- 18

SET SQL_SAFE_UPDATES = 0;

DELETE FROM enrollments
WHERE grade IS NULL;

SET SQL_SAFE_UPDATES = 1;

-- 19

select count(*) from enrollments;

-- 20

select * from students where enrollment_year=2022 order by last_name asc;

-- 21

select * from courses where credits>=3 order by credits desc;

-- 22

select * from professors where salary>=80000 and salary <= 95000;

-- 23

select * from students where email like '%@college.edu';

-- 24

SELECT enrollment_year,COUNT(*) AS total_students FROM Students GROUP BY enrollment_year;

-- 25

SELECT CONCAT(s.first_name, ' ', s.last_name) AS full_name,d.dept_name AS department 
FROM students s JOIN departments d ON s.department_id = d.department_id;

-- 26

SELECT e.enrollment_id, CONCAT(s.first_name, ' ', s.last_name) AS student_name,c.course_name,e.enrollment_date,
e.grade 
FROM enrollments e JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
ORDER BY e.enrollment_id;

-- 27

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name
FROM students s
LEFT JOIN enrollments e
    ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- 28

SELECT
    c.course_id,
    c.course_name,
    COUNT(e.student_id) AS no_of_students
FROM courses c
LEFT JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name
ORDER BY c.course_id;

-- 29

SELECT
    d.department_id,
    d.dept_name,
    p.prof_name,
    p.salary
FROM departments d
LEFT JOIN professors p
    ON d.department_id = p.department_id
ORDER BY d.department_id, p.prof_name;

-- 30

select c.course_name, count(e.student_id) as enrollment_count from courses c 
left join enrollments e on c.course_id=e.course_id 
group by c.course_id,c.course_name;

-- 31

select department_id,Round(avg(salary),2) as avg_sal from professors group by department_id;

-- 32

select dept_name,budget from departments where budget>600000;

-- 33

SELECT
    e.grade,
    COUNT(*) AS grade_count
FROM enrollments e
LEFT JOIN courses c
    ON e.course_id = c.course_id
WHERE c.course_code = 'CS101'
GROUP BY e.grade;

-- 34

SELECT
    d.dept_name,
    COUNT(e.student_id) AS total_students
FROM departments d
JOIN courses c
    ON d.department_id = c.department_id
JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY d.department_id, d.dept_name
HAVING COUNT(e.student_id) > 2;