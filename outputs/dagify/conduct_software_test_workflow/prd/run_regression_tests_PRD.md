# run_regression_tests PRD

## Description
This node orchestrates the execution of regression test scenarios for unchanged features, collecting baseline vs actual results, state drift indicators, and performance metrics.


## Conceptual Info

Orchestrates regression test scenarios and collects results for unchanged features.

## Docstring

### Summary
Executes regression test scenarios and records results.

### Returns

tuple[primitive_type.List[str], primitive_type.List[str], primitive_type.List[str]]: baseline_vs_actual_results, state_drift_indicators, performance_metrics

### Examples

```python
>>> baseline_vs_actual_results, state_drift_indicators, performance_metrics = run_regression_tests()
>>> print(baseline_vs_actual_results)
[ ['baseline_result1', 'baseline_result2'], ['state_drift_indicator1', 'state_drift_indicator2'], ['perf_metric1', 'perf_metric2'] ]
```

```python
>>> design_regression_test_cases, setup_test_environment = get_nodes()
>>> design_regression_test_cases.design_test_cases()
>>> setup_test_environment.setup_environment()
>>> run_regression_tests()
>>> output = run_regression_tests()
[ ['actual_result1', 'actual_result2'], ['state_drift_indicator1', 'state_drift_indicator2'], ['perf_metric1', 'perf_metric2'] ]
```
