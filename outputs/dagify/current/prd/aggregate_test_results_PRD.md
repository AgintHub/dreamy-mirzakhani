# aggregate_test_results PRD

## Description
Compile collected test outcome metrics


## Conceptual Info

This node aggregates test results from regression, unit, and integration tests into a standardized format.

## Docstring

### Summary
Compile collected test outcome metrics from regression, unit, and integration tests.

### Parameters

- **regression_test_results** (PrimitiveType.DICT): Output of run_regression_test node
- **unit_test_results** (PrimitiveType.DICT): Output of run_unit_test node
- **integration_test_results** (PrimitiveType.DICT): Output of run_integration_test node

### Returns

PrimitiveType.DICT: {'test_pass_rate': float, 'test_fail_rate': float, 'error_counts': list[int], 'execution_times': list[float]}

### Examples

```python
>>> regression_test_results = run_regression_test(input_data)
>>> unit_test_results = run_unit_test(input_data)
>>> integration_test_results = run_integration_test(input_data)
>>> aggregate_test_results(regression_test_results, unit_test_results, integration_test_results)
{test_pass_rate: 0.8, test_fail_rate: 0.2, error_counts: [2, 3, 1], execution_times: [10.5, 8.2, 12.1]}
```

```python
>>> regression_test_results = {'test_completion_status': 'success', 'test_failure_count': 1, 'test_error_counts': [1], 'test_execution_time': 10.5, 'stack_trace_reports': ''}
>>> unit_test_results = {'unit_test_results': ['pass', 'fail'], 'exception_details': ['Exception'], 'execution_time': 8.2}
>>> integration_test_results = {'integration_test_results': ['pass', 'pass', 'fail'], 'test_success_status': True, 'error_counts': [2], 'execution_times': [12.1, 15.6]}
>>> aggregate_test_results(regression_test_results, unit_test_results, integration_test_results)
{test_pass_rate: 0.8333, test_fail_rate: 0.1667, error_counts: [2, 0, 1], execution_times: [10.5, 8.2, 15.6]}
```
