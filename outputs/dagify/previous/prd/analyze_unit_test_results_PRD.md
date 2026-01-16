# analyze_unit_test_results PRD

## Description
Decode unit test outcomes and metrics


## Conceptual Info

Calculates code coverage and classifies failures from unit test results

## Docstring

### Summary
This function takes in unit test results and calculates code coverage, classifies failures as defects or false positives, and ranks criticality of issues.

### Parameters

- **test_results** (List[TestResult]): List of test result objects containing pass/fail status, stack trace, and test duration

### Returns

StructuredOutput: Output structure containing test results, code coverage, test count, failure count, critical failure count, error count, and error messages

### Raises

- TypeError: If input test results are not a list of TestResult objects

### Examples

```python
>>> test_results = [TestResult(pass=True), TestResult(pass=False), TestResult(pass=True)]
>>> code_coverage, test_count, failure_count, critical_failure_count, error_count, error_messages = analyze_unit_test_results(test_results)

>>> code_coverage = 0.8
>>> test_count = 3
>>> failure_count = 1
>>> critical_failure_count = 1
>>> error_count = 0
>>> error_messages = ["Error Message"]
```

```python
>>> test_results = [TestResult(pass=True), TestResult(pass=False), TestResult(pass=False)]
>>> code_coverage, test_count, failure_count, critical_failure_count, error_count, error_messages = analyze_unit_test_results(test_results)

>>> code_coverage = 0.7
>>> test_count = 3
>>> failure_count = 2
>>> critical_failure_count = 2
>>> error_count = 0
>>> error_messages = ["Error Message", "Error Message"]
```
