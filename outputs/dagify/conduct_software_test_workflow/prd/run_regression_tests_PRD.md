# run_regression_tests PRD

## Description
This node orchestrates the execution of regression test scenarios for unchanged features, collecting baseline vs actual results, state drift indicators, and performance metrics.


## Conceptual Info

Orchestrates execution of regression test scenarios, capturing baseline comparisons, state drift, and performance data.

## Docstring

### Summary
Run regression tests for unchanged features and return baseline comparisons, drift indicators, and performance metrics.

### Parameters

- **test_cases** (List[dict]): List of regression test case definitions produced by the design_regression_test_cases node. Each dictionary should contain at least `scenario_id`, `precondition_setup`, and `expected_state_preservation` keys.
- **environment** (dict): Environment configuration dictionary produced by the setup_test_environment node. Includes keys like `hardware_specs`, `software_specs`, `test_data_sets`, and `mock_services`.

### Returns

dict: Dictionary containing three keys:
- `baseline_vs_actual_results`: List[str]
- `state_drift_indicators`: List[str]
- `performance_metrics`: List[str]
Each list element corresponds to a regression scenario executed.

### Raises

- RuntimeError: If the environment status is False, indicating the test environment failed to set up.
- ValueError: If any required test case field is missing or empty.

### Examples

```python
>>> # Example input test cases and environment
>>> test_cases = [
...     {
...         "scenario_id": "reg01",
...         "precondition_setup": "load fixture A",
...         "expected_state_preservation": "database record X remains unchanged"
...     }
>>> ]
>>> environment = {
...     "hardware_specs": ["8 CPU cores", "32GB RAM"],
...     "software_specs": ["Python 3.11", "pytest 7.4"],
...     "test_data_sets": ["dataset1.csv"],
...     "mock_services": ["auth_service"],
...     "environment_status": True
>>> }
>>> results = run_regression_tests(test_cases, environment)
>>> print(results['baseline_vs_actual_results'])
["reg01: baseline=200ms, actual=210ms"]
```

```python
>>> # Example output structure after running tests
>>> print(results['state_drift_indicators'])
>>> print(results['performance_metrics'])
["reg01: no drift detected"]
["reg01: throughput=150 req/s", "reg01: response_time=210ms"]
```
