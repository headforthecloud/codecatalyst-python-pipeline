# codecatalyst-python-pipeline

This is an example of how we can use pipelines with CodeCatalyst to validate python code.

## Python Code
The repository contains a file [lambda_function.py](lambda_function.py) which holds example Python code for an AWS Lambda function.

## Python Unit tests
The repository contains a number of tests that use the [PyTest](https://pytest.org) framework, with the tests being held in the [tests](tests) folder

## CodeCatalyst Pipeline
The repository contains a pipeline yaml file called [python-testing-pipeline.yaml](.codecatalyst/workflows/python-testing-pipeline.yaml). This configures a pipeline which will run on every commit to the repository, carrying out the following actions to validate the code:

* [Linting](#linting)
* [Vulnerability scanning](#vulnerability-scanning)
* [Unit Tests](#unit-tests)

## Pipeline Validation
---
### Linting
Linting is used to ensure that the repository code meets defined coding standards. The pipeline uses [pylint](https://github.com/pylint-dev/pylint) to perform this.

#### Configuration
Linting configuration is handled in the [.pylintrc](.pylintrc) file. In the example code, we set options such as
* allowed simple variable names
* maximum line length
* output format

#### Output
The output from the linting is captured in `tests/testresults/pylint-output.py`file. This categorises any issues found as one of the following levels:
* Informational
* Low
* Medium
* High
* Critical

---
### Vulnerability Scanning
To check for any issues in the code, the pipeline uses a tool called [bandit](https://github.com/PyCQA/bandit) to scan the code for any known vulnerabilities.
#### Output
The output from the linting is captured in `tests/testresults/bandit-output.sarif`file. Again, this categorises any issues found as one of the following levels:
* Informational
* Low
* Medium
* High
* Critical

---
### Unit Tests
As mentioned above, repository contains tests written using the [PyTest](https://pytest.org) framework. This tests the functionality of the code, reporting on test success/failure as well as how much of the code has been tested (code coverage)

#### Configuration
The unit tests are configured via [.pylintrc](.pylintrc) which defines where the tests to be run are, along with what output will be generated. Alongside this [.coveragerc](.coveragerc) defines where the tests are, to ensure that we don't include them in the list of number of files that we will generate code coverage for.

#### Output
The pipeline generates two reports 
* `PyTestResults` which lists each of the tests that will be executed, along with whether the test passed or failed.
* `CodeCoverage` describes which of the main code lines have been tested.

---




<div style="text-align: right"> Back to <a href="#codecatalyst-python-pipeline">Top</a> </div>