# Interview Test Assignment
This test assignment implemented using the Pytest framework. 
Test results are printed in a workflow step titled "Run Tests".

## Installation

### Clone the Repository:
```bash
git clone https://github.com/qa-baykov/pytest.git
cd your-repository-folder
```

### Create a Virtual Environment (Optional but recommended):
``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies:
``` bash
pip install -r requirements.txt
```

## Running the Tests
**To run the tests locally, you can use the following commands:**
1. Run tests with all data:
``` bash
pytest -s
```
2. Run tests to find stock symbols that are in actual stocks but not in the given test data:
``` bash
pytest --set-to-run=not_in_test -s
```
3. Run tests to find stock symbols that are in the given test data but not in actual stocks:
``` bash
pytest --set-to-run=not_in_actual -s
```
**To run the tests manually in Actions use options run:**
``` yml
  options:
    - pytest -s
    - pytest --set-to-run=not_in_test -s
    - pytest --set-to-run=not_in_actual -s
```
**Test will be executed automatically by schedule at 08:00 AM UTC (01:00 AM PDT) every day**
``` yaml
  schedule:
    - cron: '0 1 * * *'
```

## Viewing Test Results
After running the tests, you can find the log file with the detailed test results attached as an artifact in the corresponding workflow run.

To view the log file:

* Go to the workflow run on the CI/CD platform.
* Look for the "Run Tests" step.
