# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

1. **Testing Types for Course Management API:**
   - **Unit Testing**: Test the `get_password_hash` function to ensure it properly hashes a password and returns a string of the correct length.
   - **Integration Testing**: Test that `POST /api/courses/` correctly inserts a record into the test database and foreign keys (like `department_id`) are enforced.
   - **System Testing**: End-to-end test where a user logs in, gets a JWT, and uses that JWT to create a new course via the API.
   - **User Acceptance Testing (UAT)**: A college administrator uses the frontend application to create a new course and confirms it appears correctly on the dashboard.

2. **Classification**:
   - The above examples are **Functional**.
   - **Non-Functional Example**: Load test the `GET /api/courses/` endpoint to ensure it responds in <200ms when 500 concurrent users access it (Performance/Reliability).

3. **Black-Box vs White-Box Testing**:
   - **Black-Box Testing**: Testing the system based on inputs and expected outputs without looking at the internal code. (Typically done by **QA testers**).
   - **White-Box Testing**: Testing with full knowledge of the internal code structure, writing tests for specific functions or branches. (Typically done by **Developers**).

4. **Test Cases for POST /api/courses/**:

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|---|
| TC01 | Create valid course | API is running | 1. Send POST request with valid JSON containing name, code, credits. | Status 201 Created and JSON response containing created course. | | |
| TC02 | Missing required fields | API is running | 1. Send POST request with missing 'name' field. | Status 400 Bad Request with error message. | | |
| TC03 | Duplicate course code | API is running, Course 'CS101' exists | 1. Send POST with code 'CS101'. | Status 400 or 409 Conflict with error message indicating duplicate. | | |

## Task 2: Defect Lifecycle & Severity Classification

5. **Defect Lifecycle**:
   - `New`: Bug reported.
   - `Assigned`: Bug assigned to a developer.
   - `Open`: Developer is working on the bug.
   - `Fixed`: Developer pushes a fix.
   - `Retest`: QA tests the fix.
   - `Verified/Closed`: Bug fix confirmed by QA and closed.
   - *Alternate paths*: `Rejected` (if it is working as intended or is a duplicate), `Deferred` (if it will be fixed in a later release).

6. **Severity and Priority Classification**:
   - a) POST /api/courses/ returns 500: **Severity**: Critical. **Priority**: P1. (Blocks core functionality).
   - b) Truncated name > 150 chars: **Severity**: Low/Medium. **Priority**: P3. (Edge case, minor data loss).
   - c) Swagger typo: **Severity**: Low. **Priority**: P4. (Cosmetic, doesn't affect functionality).
   - d) Intermittent 401 on login: **Severity**: High. **Priority**: P1. (Core functionality intermittently broken, affects user access).

7. **Defect Report for Bug (a)**:
   - **Defect ID**: BUG-001
   - **Title**: POST /api/courses/ returns 500 Internal Server Error
   - **Environment**: QA Environment, Windows 10
   - **Build Version**: v1.0.0
   - **Severity**: Critical
   - **Priority**: P1
   - **Steps to Reproduce**: 1. Send a standard POST request to `/api/courses/` with valid payload. 
   - **Expected Result**: 201 Created response.
   - **Actual Result**: 500 Internal Server error with traceback.
   - **Attachments**: 'screenshot of 500 error'

8. **Severity vs Priority**:
   - **Severity** is how much the bug breaks the system. **Priority** is how urgently it needs fixing.
   - *High Severity / Low Priority Example*: The application crashes (High severity) but only when a user navigates to an obscure legacy screen and clicks a button 50 times very quickly (Low priority because almost no users do this).
