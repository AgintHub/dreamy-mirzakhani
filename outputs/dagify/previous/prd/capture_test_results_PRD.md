# capture_test_results PRD

## Description
Aggregate raw results from the test run.


## Conceptual Info

This node aggregates raw results from the test run, collecting data on pass/fail status, execution time, and failure details for each test case.

## Docstring

### Summary
Captures and aggregates test execution data from the output of execute_test_cases node.

### Parameters

- **test_case_results** (List[Dict[str, Any]]): List of dictionaries containing test case execution results, each with 'test_case_id', 'passed', 'failure_reason', 'execution_time' keys.

### Returns

Dict[str, Any]: Dictionary containing aggregated test results, including lists of test case IDs, pass/fail status, execution times, failure details, and totals for tests, passed, and failed.

### Raises

- ValueError: If the input test_case_results is empty or contains invalid data.

### Examples

```python
>>> capture_test_results([
...     {'test_case_id': 'TC1', 'passed': True, 'failure_reason': None, 'execution_time': 10.0},
...     {'test_case_id': 'TC2', 'passed': False, 'failure_reason': 'Assertion error', 'execution_time': 5.0}
>>> ])
{'test_case_ids': ['TC1', 'TC2'], 'pass_fail_status': [True, False], 'execution_times': [10.0, 5.0], 'failure_details': [None, 'Assertion error'], 'total_tests': 2, 'total_passed': 1, 'total_failed': 1}
```
