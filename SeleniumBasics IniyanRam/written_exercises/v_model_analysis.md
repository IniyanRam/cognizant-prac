# Hands-On 2: SDLC vs TDLC & Agile QA Integration

## Task 1: V-Model Mapping

9. **V-Model Diagram**:
Requirements => Acceptance Testing
  System Design => System Testing
    Architecture Design => Integration Testing
      Module Design => Unit Testing
                 Coding

10. **Test Artifacts per SDLC Phase**:
- Requirements → Acceptance Test Plan
- System Design → System Test Plan
- Architecture Design → Integration Test Plan
- Module Design → Unit Test Cases

11. **Entry & Exit Criteria**:
- **Unit Testing**: 
  - Entry: Module code completed and compiled. 
  - Exit: All unit tests pass, coverage code metrics met.
- **Integration Testing**: 
  - Entry: Unit tested modules are available and integrated. 
  - Exit: No high severity integration bugs, all integrated flows work.
- **System Testing**: 
  - Entry: Full system is integrated and deployed to QA env. 
  - Exit: 100% test execution, no open critical bugs.
- **Acceptance Testing**: 
  - Entry: System testing signed off. 
  - Exit: Stakeholders approve the software for Production.

12. **Early QA Engagement Points**:
- Reviewing Requirements documents for ambiguities and testability.
- Participating in Architecture/Design discussions to plan integration tests and mock data early.

## Task 2: Agile QA and Shift-Left Testing

13. **3 Problems with Waterfall Testing for the API**:
- Bugs are found too late, making them expensive and risky to fix.
- Requirements misunderstandings aren't caught until the end.
- Automated testing is delayed, slowing down feedback loops.

14. **QA in Agile Ceremonies**:
- **Sprint Planning**: Define acceptance criteria and point estimates for testing effort.
- **Daily Standup**: Report testing progress, and blockages (e.g. environment down).
- **Sprint Review**: Demo tested features and automated tests to stakeholders.
- **Retrospective**: Discuss what went well with the QA process and how to improve.

15. **Shift-Left Practices**:
- **(a) Review requirements for testability**: Discussing Edge cases during grooming for `/api/courses`.
- **(b) BDD (Given-When-Then)**: Writing cucumber tests for course enrollment before code is written.
- **(c) Static Code Analysis**: Running SonarQube/linters on every push to catch issues before QA deploy.
- **(d) API Contract Testing**: Using tools like Pact to verify frontend and backend match before integrating.

16. **Acceptance Criteria (Gherkin format)**:

*Happy Path:*
Given I am an authenticated college admin
When I submit the course form with valid data
Then the course is created successfully

*Duplicate Course Code:*
Given I am an authenticated college admin and course "CS101" exists
When I submit the course form with code "CS101"
Then I should see a validation error about duplicate codes

*Missing Required Fields:*
Given I am an authenticated college admin
When I submit the course form with the name field empty
Then I should see a validation error that name is required
