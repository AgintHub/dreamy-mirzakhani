# run_unit_tests PRD

## Description
Execute module-level test cases.


## Conceptual Info

The node runs the suite of unit tests generated in the design phase, collects execution metadata, and returns structured results for downstream analysis.

## Docstring

### Summary
Run module‑level unit tests and capture pass/fail status, output diffs, and timestamps.

### Parameters

- **test_cases** (List[Dict[str, Any]]): A list of test case definitions produced by `design_unit_test_cases`. Each dictionary contains at least `test_id`, `input_parameters`, and `expected_output` keys.
- **environment** (Dict[str, Any]): Environment configuration dictionary produced by `setup_test_environment`, including hardware_specs, software_specs, test_data_sets, mock_services, and environment_status.

### Returns

Dict[str, List[Union[bool, str, str]]]: A dictionary with keys `test_execution_status`, `actual_output_vs_expected_output`, and `test_case_timestamps`, each containing a list aligned to the input test_cases order.

### Raises

- RuntimeError: If the test environment is not successfully set up (environment['environment_status'] is False).
- ValueError: If any test case dictionary lacks required keys (`test_id`, `input_parameters`, or `expected_output`).
- Exception: Any unexpected exception raised during test execution (e.g., import errors, runtime failures).

### Examples

```python
>>> test_cases = [
...     {
...         'test_id': 'TC01',
...         'input_parameters': {'a': 2, 'b': 3},
...         'expected_output': 5
...     },
...     {
...         'test_id': 'TC02',
...         'input_parameters': {'a': -1, 'b': 1},
...         'expected_output': 0
...     }
>>> ]
>>> environment = {
...     'environment_status': True
>>> }
>>> result = run_unit_tests(test_cases, environment)
>>> print(result['test_execution_status'])
>>> print(result['actual_output_vs_expected_output'])
>>> print(result['test_case_timestamps'])
[True, True]
['OK', 'OK']
['2026-01-20 10:15:23', '2026-01-20 10:15:24']
```

```python
>>> test_cases = [
...     {
...         'test_id': 'TC01',
...         'input_parameters': {'a': 2, 'b': 3},
...         'expected_output': 5
...     },
...     {
...         'test_id': 'TC03',
...         'input_parameters': {'a': 10, 'b': 5},
...         'expected_output': 15
...     }
>>> ]
>>> environment = {
...     'environment_status': True
>>> }
>>> # Assume the second test fails because the implementation returns 14
>>> result = run_unit_tests(test_cases, environment)
>>> print(result['test_execution_status'])
>>> print(result['actual_output_vs_expected_output'])
>>> print(result['test_case_timestamps'])
[True, False]
['OK', 'Expected 15 but got 14']
['2026-01-20 10:15:23', '2026-01-20 10:15:24']
```
