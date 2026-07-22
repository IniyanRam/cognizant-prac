# Hands-On 3: Test Automation Process & Strategy

## Task 1: Automation Decision and Test Case Selection

17. **5 Criteria for Deciding What to Automate**:
- **Repetitive Execution**: Tests run frequently (e.g. regression).
- **High Risk**: Critical business workflows.
- **Stable UI/Feature**: Features that aren't constantly changing.
- **Data-Driven**: Tests that need to run with multiple data sets.
- **Positive ROI**: Time saved > time to write and maintain the script.
*(Applied to scenario)*: Testing `POST /api/courses/` is high business risk, stable, and used frequently in regression, making it a great automation candidate.

18. **Automate or Manual**:
- (a) Regression test for CRUD: **Automate** (Highly repetitive, stable).
- (b) Exploratory testing: **Manual** (Requires human intuition).
- (c) Performance test: **Automate** (Impossible to do manually).
- (d) UI test for login form: **Automate** (Core functionality, runs often).
- (e) Verify API documentation text: **Manual** (One-time or context-heavy visual check).
- (f) Smoke test after deploy: **Automate** (Needs to be fast and repetitive).

19. **Test Automation ROI Calculation**:
- Manual test time: 30 mins.
- Automation creation time: 4 hours (240 mins).
- Runs to break even: 240 / 30 = 8 runs. 
After 8 runs, it pays for itself. (Maintenance starts at run 10, overhead = 20% of 30m = 6 minutes per run. Still highly positive ROI over the long term.)

20. **Flaky Tests**:
- **Definition**: A test that sometimes passes and sometimes fails without code changes.
- **Example**: A Selenium test fails because a page loads too slowly in one environment.
- **Prevention strategies**: 
  1) Use Explicit Waits instead of `time.sleep()`. 
  2) Isolate test data so tests don't step on each other. 
  3) Retry mechanisms for network-level flakiness.

## Task 2: Compare Automation Framework Types

21. **5 Automation Framework Types**:
- **Linear**: Simple record & playback (Selenium IDE). Pro: Fast to start. Con: No reusability. Example: Quick one-time scrape.
- **Modular**: Break tests into functions. Pro: Reusable parts. Con: Hardcoded data. Example: Simple Course login function.
- **Data-Driven**: Parameterize test inputs from CSV/Excel. Pro: Test many combinations easily. Con: Setup overhead. Example: Submitting 50 bad course payloads.
- **Keyword-Driven**: Action keywords mapped to functions (e.g. Robot Framework). Pro: Non-technical people can write tests. Con: Heavy abstraction to maintain.
- **Hybrid**: Mix of the above. Pro: Highly scalable. Con: Complex to build. Example: Large scale enterprise POM suite.

22. **Recommendation**:
For testing login with 50 user combinations and supporting both technical/non-technical users, use a **Hybrid Framework** (Combining Data-Driven for the 50 combinations + Keyword/BDD for non-technical teammates).

23. **Hybrid Framework Folder Structure**:
```
tests/
  test_courses.py        # Test execution scripts
pages/
  course_page.py         # Page Object Model locators/methods
data/
  login_data.csv         # Data for Data-Driven tests
utils/
  driver_factory.py      # Browser setup and teardown
reports/
  report.html            # Output results
conftest.py              # Pytest fixtures
```
