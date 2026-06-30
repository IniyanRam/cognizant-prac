import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iniyan2005",
    database="college_db"
)

cursor = conn.cursor()

# Task 56 - Simulate the N+1 Problem

print("Task 56: N+1 Problem")

start = time.time()

query_count = 0

# Query 1
cursor.execute("SELECT * FROM enrollments")
query_count += 1

enrollments = cursor.fetchall()

# One query for every enrollment
for enrollment in enrollments:
    student_id = enrollment[1]

    cursor.execute(
        "SELECT first_name, last_name FROM students WHERE student_id = %s",
        (student_id,)
    )

    cursor.fetchone()
    query_count += 1

end = time.time()

n1_time = end - start

print("Total Queries:", query_count)
print("Execution Time:", n1_time, "seconds")

# Task 57 - Solve using JOIN

print("\nTask 57: JOIN Solution")

start = time.time()

cursor.execute("""
SELECT
    e.enrollment_id,
    s.first_name,
    s.last_name,
    c.course_name,
    e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
""")

rows = cursor.fetchall()

end = time.time()

join_time = end - start

print("Total Queries: 1")
print("Execution Time:", join_time, "seconds")

# Task 58 - Compare both approaches

print("\nTask 58: Comparison")

print("N+1 Queries :", query_count)
print("JOIN Queries: 1")
print("Extra Queries:", query_count - 1)

print("\nN+1 Time :", n1_time, "seconds")
print("JOIN Time:", join_time, "seconds")

"""
Task 59 Analysis

N+1 Problem:

The N+1 approach executes one query to retrieve all enrollment records.

It then executes one additional query for every enrollment to retrieve the student's name.

Example:
10 enrollments
= 1 + 10
= 11 queries

100 enrollments
= 101 queries

1000 enrollments
= 1001 queries

10000 enrollments
= 10001 queries

This results in a large number of unnecessary database round-trips.

The JOIN approach retrieves all required data using a single SQL query, making it significantly more efficient.

In ORM frameworks, this problem is commonly caused by lazy loading.

It can be avoided using eager loading techniques such as:
- JOIN
- select_related() in Django
- joinedload() in SQLAlchemy
"""

cursor.close()
conn.close()