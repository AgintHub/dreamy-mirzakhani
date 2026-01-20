# analyze_unit_test_results PRD

## Description
Identify unit-level anomalies


## Conceptual Info

This node analyzes the results of unit tests to identify failures and provide insights into the root causes of these failures.

## Docstring

### Summary
Analyze unit test results to identify test case failures and suggest root causes.

### Parameters

- **test_execution_status** (List[bool]): Pass/fail status of each test case
- **actual_output_vs_expected_output** (List[str]): Difference between actual and expected output of each test case
- **test_case_timestamps** (List[str]): Timestamps for each test execution

### Returns

dict: A dictionary containing test case names, actual outputs, suggested root causes, test types, passed tests, and failed tests.

### Raises

- ValueError: If the input test execution status, actual output vs expected output, or test case timestamps are empty or invalid.

### Examples

```python
>>> analyze_unit_test_results([True, False, True], ['pass', 'fail', 'pass'], ['2022-01-01 12:00:00', '2022-01-01 12:01:00', '2022-01-01 12:02:00'])
{'test_case_name': ['test_case_2'], 'actual_output': ['fail'], 'suggested_root_cause': ['Implementation error'], 'test_type': ['unit_test'], 'passed_tests': ['test_case_1', 'test_case_3'], 'failed_tests': ['test_case_2']}
```
