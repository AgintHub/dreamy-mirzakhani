# report_defects PRD

## Description
Aggregate testing anomalies


## Conceptual Info

This node aggregates testing anomalies from unit, integration, and regression tests.

## Docstring

### Summary
Aggregate testing anomalies from multiple test types.

### Parameters

- **unit_test_results** (dict): Results from unit tests.
- **integration_test_results** (dict): Results from integration tests.
- **regression_test_results** (dict): Results from regression tests.

### Returns

dict: Dict of test type, component info, description, severity, and reproduction steps.

### Raises

- TypeError: If input results are not dictionaries.

### Examples

```python
>>> defect_summary = report_defects(unit_test_results={'test_type': 'unit', 'description': 'test desc'},
>>> integration_test_results={'test_type': 'integration', 'description': 'test desc'},
>>> regression_test_results={'test_type': 'regression', 'description': 'test desc'})
{'test_type': 'unit', 'component_info': 'default', 'description': 'test desc', 'severity': 'low', 'reproduction_steps': 'no reproduction steps'}
```

```python
>>> defect_summary = report_defects({'test_type': 'unit', 'description': 'test desc'},
>>> {'test_type': 'integration', 'description': 'test desc'},
>>> {'test_type': 'regression', 'description': 'test desc'})
{'test_type': 'unit', 'component_info': 'default', 'description': 'test desc', 'severity': 'low', 'reproduction_steps': 'no reproduction steps'}
```
