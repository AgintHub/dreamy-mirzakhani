# generate_test_report PRD

## Description
Compile test results summary


## Conceptual Info

The `generate_test_report` node aggregates defect information from the `report_defects` node and computes high‑level test metrics such as total tests executed, pass/fail counts, defect density, and an overall risk rating. These metrics are used downstream by the sign‑off stage to evaluate the quality of the software release.

## Docstring

### Summary
Generate a concise test report from defect data.

### Parameters

- **defect_summary** (dict): Dictionary containing defect details aggregated by `report_defects`. Expected keys are `test_type`, `component_info`, `description`, `severity`, and `reproduction_steps`. Each key maps to a list of values extracted from the defect table.
- **total_tests_executed** (int): Total number of test cases that were run across all test types.

### Returns

dict: A dictionary with the following integer and float metrics:
- `total_tests_executed` (int)
- `pass_count` (int)
- `defect_density` (float)
- `risk_assessment_rating` (int 1‑10)

### Raises

- ValueError: Raised if `defect_summary` does not contain all required keys or if `total_tests_executed` is negative.

### Examples

```python
>>> defect_summary = {
...     'test_type': ['unit', 'integration', 'regression'],
...     'component_info': ['auth', 'db', 'api'],
...     'description': ['NullPointer', 'Timeout', 'DataLoss'],
...     'severity': ['high', 'medium', 'high'],
...     'reproduction_steps': ['step1', 'step2', 'step3']
>>> }
>>> total_tests_executed = 120
>>> report = generate_test_report(defect_summary, total_tests_executed)
{
    'total_tests_executed': 120,
    'pass_count': 102,
    'defect_density': 0.025,
    'risk_assessment_rating': 7
}
```

```python
>>> defect_summary = {
...     'test_type': [],
...     'component_info': [],
...     'description': [],
...     'severity': [],
...     'reproduction_steps': []
>>> }
>>> report = generate_test_report(defect_summary, 0)
{
    'total_tests_executed': 0,
    'pass_count': 0,
    'defect_density': 0.0,
    'risk_assessment_rating': 0
}
```
