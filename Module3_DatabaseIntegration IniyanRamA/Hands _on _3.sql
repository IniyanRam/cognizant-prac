-- 35

SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    COUNT(e.course_id) AS course_count
FROM students s
JOIN enrollments e
    ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) > (
    SELECT AVG(enrollment_count)
    FROM (
        SELECT COUNT(*) AS enrollment_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_enrollments
);

-- 36

SELECT
    c.course_id,
    c.course_name
FROM courses c
WHERE EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
)
AND NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.course_id = c.course_id
      AND e.grade <> 'A'
);  

-- 37

SELECT
    p.professor_id,
    p.prof_name,
    p.department_id,
    p.salary
FROM professors p
WHERE p.salary = (
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- 38 

SELECT
    department_id,
    avg_sal
FROM (
    SELECT
        department_id,
        AVG(salary) AS avg_sal
    FROM professors
    GROUP BY department_id
) AS db
WHERE avg_sal > 85000;

-- 39

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS full_name,
    d.dept_name AS department,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4
                WHEN 'B' THEN 3
                WHEN 'C' THEN 2
                WHEN 'D' THEN 1
                WHEN 'F' THEN 0
            END
        ), 2
    ) AS gpa
FROM students s
LEFT JOIN departments d
    ON s.department_id = d.department_id
LEFT JOIN enrollments e
    ON s.student_id = e.student_id
GROUP BY
    s.student_id,
    full_name,
    d.dept_name;
    
-- 40

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE e.grade
                WHEN 'A' THEN 4
                WHEN 'B' THEN 3
                WHEN 'C' THEN 2
                WHEN 'D' THEN 1
                WHEN 'F' THEN 0
            END
        ), 2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
    ON c.course_id = e.course_id
GROUP BY
    c.course_id,
    c.course_name,
    c.course_code;
    
-- 41

select * from vw_student_enrollment_summary where gpa > 3.0;

-- 42

UPDATE vw_student_enrollment_summary
SET department = 'Electronics'
WHERE student_id = 1;

-- there is an error as ERROR 1288 (HY000):
-- The target table vw_student_enrollment_summary of the UPDATE is not updatable.
-- Reasons:
-- 1. The view is built using multiple tables (students,
--    departments and enrollments).
-- 2. It contains aggregate functions such as COUNT() and AVG().
-- 3. It uses GROUP BY to summarize data.
-- 4. SQL cannot determine how a change to an aggregated row
--    should be propagated back to the underlying base tables.

-- Therefore, multi-table views containing JOINs, GROUP BY,
-- aggregate functions, DISTINCT or computed columns are
-- generally not updatable.

-- 43

DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    email,
    department_id,
    enrollment_year
FROM students
WHERE enrollment_year >= 2022
WITH CHECK OPTION;

-- 44

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    IF EXISTS (
        SELECT *
        FROM enrollments
        WHERE student_id = p_student_id
          AND course_id = p_course_id
    ) THEN
        SELECT 'Student is already enrolled in this course.' AS Message;
    ELSE
        INSERT INTO enrollments(student_id, course_id, enrollment_date)
        VALUES(p_student_id, p_course_id, p_enrollment_date);

        SELECT 'Enrollment Successful.' AS Message;
    END IF;
END$$

DELIMITER ;

CALL sp_enroll_student(1,3,'2022-07-10');

-- 45

CREATE TABLE IF NOT EXISTS department_transfer_log(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_student_id INT,
    IN p_new_department INT
)
BEGIN
    DECLARE old_dept INT;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transaction Rolled Back' AS Message;
    END;

    START TRANSACTION;

    SELECT department_id
    INTO old_dept
    FROM students
    WHERE student_id = p_student_id;

    UPDATE students
    SET department_id = p_new_department
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log
    (student_id, old_department, new_department)
    VALUES
    (p_student_id, old_dept, p_new_department);

    COMMIT;

    SELECT 'Transfer Successful' AS Message;

END$$

DELIMITER ;

CALL sp_transfer_student(1,2);

SELECT * FROM students WHERE student_id = 1;
SELECT * FROM department_transfer_log;

-- 46

CALL sp_transfer_student(1,100);

SELECT * FROM students WHERE student_id = 1;
SELECT * FROM department_transfer_log;

-- 47

START TRANSACTION;

INSERT INTO enrollments(student_id, course_id, enrollment_date)
VALUES(7,1,'2023-07-05');

SAVEPOINT first_insert;

INSERT INTO enrollments(student_id, course_id, enrollment_date)
VALUES(7,100,'2023-07-05');

ROLLBACK TO first_insert;

COMMIT;

SELECT *
FROM enrollments
WHERE student_id = 7;