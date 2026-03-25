# acceptance_test_suite PRD

## Description
Verify business rule compliance


## Conceptual Info

Runs the Acceptance Test Suite after the test environment and synthetic data are prepared. It executes business‑rule‑level test cases, evaluates each against acceptance criteria, and produces a concise execution summary for downstream aggregation.

## Docstring

### Summary
Execute acceptance tests and return detailed results summarizing compliance with business rules and user acceptance criteria.

### Parameters

- **environment_ready** (bool): Flag from `create_test_environment` indicating the test environment is healthy and ready.
- **test_data_paths** (List[str]): List of file system paths to the generated test data files from `generate_test_data`.
- **test_cases_definition** (List[dict]): Structured definitions of acceptance test cases (e.g., {'id': 'TC01', 'description': ..., 'expected_result': ...}).

### Returns

dict: A dictionary containing execution lists, pass/fail aggregates, pass rate, and a defect summary matching the node's output_structure.

### Raises

- RuntimeError: If `environment_ready` is False, indicating the environment cannot run tests.
- FileNotFoundError: If any path in `test_data_paths` does not exist or is unreadable.
- ValueError: If `test_cases_definition` is empty or malformed.

### Examples

```python
>>> result = acceptance_test_suite(
...     environment_ready=True,
...     test_data_paths=['/tmp/data1.json', '/tmp/data2.json'],
...     test_cases_definition=[
...         {'id': 'A1', 'description': 'Verify login', 'expected_result': 'success'},
...         {'id': 'A2', 'description': 'Reject invalid email', 'expected_result': 'error'}
...     ]
>>> )
{
  'executed_test_cases': ['A1', 'A2'],
  'passed_test_cases': ['A1'],
  'failed_test_cases': ['A2'],
  'overall_pass': False,
  'pass_rate': 0.5,
  'defect_summary': 'A2 failed: system returned success for invalid email.'
}
```

```python
>>> acceptance_test_suite(True, ['/tmp/data.json'], [{'id':'B1','description':'Check checkout','expected_result':'success'}])
{'executed_test_cases': ['B1'], 'passed_test_cases': ['B1'], 'failed_test_cases': [], 'overall_pass': True, 'pass_rate': 1.0, 'defect_summary': ''}
```
