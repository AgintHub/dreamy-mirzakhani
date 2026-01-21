# report_defects PRD

## Description
Aggregate testing anomalies


## Conceptual Info

Consolidates defect findings from unit, integration, and regression testing into a single, normalized defect summary table suitable for reporting and risk assessment. Enables quick triage and traceability to specific test types and components.

## Docstring

### Summary
Aggregate defect records from unit, integration, and regression analyses into a unified defect summary table.

### Parameters

- **unit_results** (List[Dict[str, str]]): Defect records produced by analyze_unit_test_results. Each dict should contain keys: test_type, component_info, description, severity, reproduction_steps.
- **integration_results** (List[Dict[str, str]]): Defect records produced by analyze_integration_test_results. Each dict should contain keys: test_type, component_info, description, severity, reproduction_steps.
- **regression_results** (List[Dict[str, str]]): Defect records produced by analyze_regression_test_results. Each dict should contain keys: test_type, component_info, description, severity, reproduction_steps.

### Returns

List[Dict[str, str]]: A list of defect records, each with keys: test_type, component_info, description, severity, reproduction_steps.

### Raises

- ValueError: If any input is not a list of dictionaries with the required keys, or if the combined dataset is empty without a default fallback.
- TypeError: If inputs are provided but are not lists.

### Examples

```python
>>> unit_results = [
...     {'test_type': 'unit', 'component_info': 'AuthService', 'description': 'Null pointer on login', 'severity': 'high', 'reproduction_steps': 'Invoke login with empty password'},
>>> ]
>>> integration_results = []
>>> regression_results = []
>>> report_defects(unit_results, integration_results, regression_results)
[{'test_type': 'unit', 'component_info': 'AuthService', 'description': 'Null pointer on login', 'severity': 'high', 'reproduction_steps': 'Invoke login with empty password'}]
```

```python
>>> unit_results = [
...     {'test_type': 'unit', 'component_info': 'AuthService', 'description': 'Null pointer on login', 'severity': 'High', 'reproduction_steps': 'Click login with invalid credentials'},
...     {'test_type': 'unit', 'component_info': 'UserService', 'description': 'Timeout on user fetch', 'severity': 'Medium', 'reproduction_steps': 'Fetch user details repeatedly until timeout'}
>>> ]
>>> integration_results = [
...     {'test_type': 'integration', 'component_info': 'API Gateway -> User Service', 'description': 'Mismatch in data contract', 'severity': 'High', 'reproduction_steps': 'Call API with payload X'},
>>> ]
>>> regression_results = []
>>> report_defects(unit_results, integration_results, regression_results)
[{'test_type': 'unit', 'component_info': 'AuthService', 'description': 'Null pointer on login', 'severity': 'High', 'reproduction_steps': 'Click login with invalid credentials'}, {'test_type': 'unit', 'component_info': 'UserService', 'description': 'Timeout on user fetch', 'severity': 'Medium', 'reproduction_steps': 'Fetch user details repeatedly until timeout'}, {'test_type': 'integration', 'component_info': 'API Gateway -> User Service', 'description': 'Mismatch in data contract', 'severity': 'High', 'reproduction_steps': 'Call API with payload X'}]
```
