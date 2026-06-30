-- Hands on 4 
-- Task 1

EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;


/* JSON Output:
EXPLAIN
"{
  query_block"": {"
    "select_id": 1
    "cost_info": {
      "query_cost": "5.30"
    }
    "nested_loop": [
      {
        "table": {
          "table_name": "s"
          "access_type": "ALL"
          "possible_keys": [
            "PRIMARY"
          ]
          "rows_examined_per_scan": 10
          "rows_produced_per_join": 1
          "filtered": "10.00"
          "cost_info": {
            "read_cost": "1.90"
            "eval_cost": "0.10"
            "prefix_cost": "2.00"
            "data_read_per_join": "824"
          }
          "used_columns": [
            "student_id"
            "first_name"
            "last_name"
            "enrollment_year"
          ]
          "attached_condition": "(`college_db`.`s`.`enrollment_year` = 2022)"
        }
      }
      {
        "table": {
          "table_name": "e"
          "access_type": "ref"
          "possible_keys": [
            "student_id"
            "course_id"
          ]
          "key": "student_id"
          "used_key_parts": [
            "student_id"
          ]
          "key_length": "5"
          "ref": [
            "college_db.s.student_id"
          ]
          "rows_examined_per_scan": 1
          "rows_produced_per_join": 1
          "filtered": "100.00"
          "cost_info": {
            "read_cost": "1.50"
            "eval_cost": "0.15"
            "prefix_cost": "3.65"
            "data_read_per_join": "48"
          }
          "used_columns": [
            "student_id"
            "course_id"
          ]
          "attached_condition": "(`college_db`.`e`.`course_id` is not null)"
        }
      }
      {
        "table": {
          "table_name": "c"
          "access_type": "eq_ref"
          "possible_keys": [
            "PRIMARY"
          ]
          "key": "PRIMARY"
          "used_key_parts": [
            "course_id"
          ]
          "key_length": "4"
          "ref": [
            "college_db.e.course_id"
          ]
          "rows_examined_per_scan": 1
          "rows_produced_per_join": 1
          "filtered": "100.00"
          "cost_info": {
            "read_cost": "1.50"
            "eval_cost": "0.15"
            "prefix_cost": "5.30"
            "data_read_per_join": "1K"
          }
          "used_columns": [
            "course_id"
            "course_name"
          ]
        }
      }
    ]
  }
}"


In the students table (referred as s) it can be seen that the JSON shows "access_type" to be ALL, which refers to a FULL TABLE SCAN. Other tables do not have full table scans. 
The enrollments table, referred as e shows access type "ref" "ref" indicates an index lookup using a non-unique index, the cources table has "eq_ref" which means primary index lookup

Estimated Rows Examined:

Students table (s): 10 rows examined per scan.
Enrollments table (e): 1 row examined per scan.
Courses table (c): 1 row examined per scan.

The students table performs a Full Table Scan (access_type = ALL),
examining all 10 rows because there is no index on enrollment_year.
The enrollments table uses an index lookup (ref), while the courses
table uses a primary key lookup (eq_ref), making them more efficient.

Task 2
*/
CREATE INDEX idx_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_student_course
ON enrollments(student_id, course_id);

CREATE INDEX idx_course_code
ON courses(course_code);

EXPLAIN FORMAT=JSON
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/* Output of updated EXPLAIN:
EXPLAIN
"{
  query_block"": {"
    "select_id": 1
    "cost_info": {
      "query_cost": "3.15"
    }
    "nested_loop": [
      {
        "table": {
          "table_name": "s"
          "access_type": "ALL"
          "possible_keys": [
            "PRIMARY"
          ]
          "rows_examined_per_scan": 10
          "rows_produced_per_join": 1
          "filtered": "10.00"
          "cost_info": {
            "read_cost": "1.90"
            "eval_cost": "0.10"
            "prefix_cost": "2.00"
            "data_read_per_join": "824"
          }
          "used_columns": [
            "student_id"
            "first_name"
            "last_name"
            "enrollment_year"
          ]
          "attached_condition": "(`college_db`.`s`.`enrollment_year` = 2022)"
        }
      }
      {
        "table": {
          "table_name": "e"
          "access_type": "ref"
          "possible_keys": [
            "idx_student_course"
            "course_id"
          ]
          "key": "idx_student_course"
          "used_key_parts": [
            "student_id"
          ]
          "key_length": "5"
          "ref": [
            "college_db.s.student_id"
          ]
          "rows_examined_per_scan": 2
          "rows_produced_per_join": 2
          "filtered": "100.00"
          "using_index": true
          "cost_info": {
            "read_cost": "0.25"
            "eval_cost": "0.20"
            "prefix_cost": "2.45"
            "data_read_per_join": "64"
          }
          "used_columns": [
            "student_id"
            "course_id"
          ]
          "attached_condition": "(`college_db`.`e`.`course_id` is not null)"
        }
      }
      {
        "table": {
          "table_name": "c"
          "access_type": "eq_ref"
          "possible_keys": [
            "PRIMARY"
          ]
          "key": "PRIMARY"
          "used_key_parts": [
            "course_id"
          ]
          "key_length": "4"
          "ref": [
            "college_db.e.course_id"
          ]
          "rows_examined_per_scan": 1
          "rows_produced_per_join": 2
          "filtered": "100.00"
          "cost_info": {
            "read_cost": "0.50"
            "eval_cost": "0.20"
            "prefix_cost": "3.15"
            "data_read_per_join": "1K"
          }
          "used_columns": [
            "course_id"
            "course_name"
          ]
        }
      }
    ]
  }
}"

Comparison with Baseline:

After creating the indexes, the overall estimated query cost
decreased from 5.30 to 3.15, indicating an improvement in
query efficiency.

The students table still uses access_type = ALL (Full Table Scan). This is because the table currently contains only 10
rows, and the MySQL query optimizer determines that scanning the entire table is cheaper than using the index on
enrollment_year.

The enrollments table now uses the composite index (idx_student_course), as shown by the access_type = ref and
key = idx_student_course. This reduces the cost of locating matching enrollment records and improves join performance.

The courses table continues to use access_type = eq_ref, which performs an efficient primary key lookup using the
PRIMARY index.

Although the newly created index on enrollment_year is not used for this small dataset, it would become beneficial for
large tables containing thousands or millions of rows, where a Full Table Scan would be significantly more expensive.
Overall, the indexes have reduced the estimated query cost and improved the execution plan.
*/

-- 55
/*MySQL does not support partial indexes with a WHERE clause. 

An alternative in MySQL would be to create a regular index on (student_id, grade), although
it indexes all rows instead of only those where grade IS NULL.
*/