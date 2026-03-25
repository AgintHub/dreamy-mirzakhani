# unit_test_suite PRD

## Description
Execute unit tests for core components


## Conceptual Info

Runs the complete unit‑test suite for the core codebase, aggregates results, measures coverage, and determines overall success based on pass count and a configurable coverage threshold.

## Docstring

### Summary
Execute all unit tests, compute coverage, and return a structured result summary.

### Parameters

- **env_ready** (bool): Flag indicating that the test environment is ready (output of `create_test_environment`).
- **test_data_paths** (List[str]): File system paths to synthetic test data files produced by `generate_test_data`.
- **coverage_threshold** (float): Minimum acceptable code coverage percentage (e.g., 80.0).

### Returns

dict: Dictionary containing keys `total_tests`, `passed_tests`, `failed_tests`, `coverage_percent`, `failed_test_names`, `error_messages`, and `is_successful` as defined in the node's output structure.

### Raises

- RuntimeError: If the test environment is not ready (`env_ready` is False).
- FileNotFoundError: If any path in `test_data_paths` does not exist.
- ValueError: If `coverage_threshold` is not between 0 and 100.

### Examples

```python
>>> result = unit_test_suite(
...     env_ready=True,
...     test_data_paths=['/tmp/data1.json', '/tmp/data2.json'],
...     coverage_threshold=85.0
>>> )
{
  'total_tests': 120,
  'passed_tests': 118,
  'failed_tests': 2,
  'coverage_percent': 87.3,
  'failed_test_names': ['test_calc_edge', 'test_invalid_input'],
  'error_messages': ['AssertionError in test_calc_edge', 'ValueError in test_invalid_input'],
  'is_successful': True
}
```

```python
>>> unit_test_suite(False, [], 80.0)
RuntimeError: Test environment is not ready.
```
