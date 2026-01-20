# report_defects PRD

## Description
Aggregate testing anomalies


## Conceptual Info

Aggregate testing anomalies from unit, integration, and regression tests.

## Docstring

### Summary
Compile defects from various test types into a summary table.

### Parameters

- **unit_test_results** (dict): Output from analyze_unit_test_results
- **integration_test_results** (dict): Output from analyze_integration_test_results
- **regression_test_results** (dict): Output from analyze_regression_test_results

### Returns

list[dict]: List of defect dictionaries with test_type, component_info, description, severity, and reproduction_steps

### Raises

- ValueError: If any test result is not provided or is malformed

### Examples

```python
>>> unit_test_results = {'test_case_name': 'test1', 'actual_output': 'fail', 'suggested_root_cause': 'code issue'}
>>> integration_test_results = {'interface_failures': ['failure1'], 'component_pairs': ['pair1']}
>>> regression_test_results = {'feature_name': 'feature1', 'before_after_state_comparison': 'comparison1'}
>>> report_defects(unit_test_results, integration_test_results, regression_test_results)
[{'test_type': 'unit', 'component_info': '', 'description': 'test1 failed', 'severity': 'high', 'reproduction_steps': 'rerun test1'}]
```
