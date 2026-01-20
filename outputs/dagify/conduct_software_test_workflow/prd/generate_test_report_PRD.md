# generate_test_report PRD

## Description
Compile test results summary


## Conceptual Info

This node synthesizes a concise health summary of the test cycle by consuming defect summaries produced by report_defects and execution-level results from prior test runs. It computes total tests, successful tests, defect density, and a risk rating to convey overall quality and risk posture.

## Docstring

### Summary
Compute a compact test execution summary from defect data and test execution outcomes.

### Parameters

- **defect_report_summary** (str): Serialized defect summary produced by report_defects (e.g., JSON string).
- **execution_summary** (str): Serialized execution results summary (e.g., JSON string) with total, passes, and optional failures.

### Returns

Dict[str, Any]: Dictionary containing the computed metrics: total_tests_executed (int), pass_count (int), defect_density (float), risk_assessment_rating (int).

### Raises

- ValueError: If inputs are not valid JSON or required fields are missing.
- TypeError: If input types do not conform to expected string inputs.

### Examples

```python
>>> defect_report_summary = '{"defects": 3, "details": []}'
>>> execution_summary = '{"tests_executed": 120, "passes": 117}'
>>> result = generate_test_report(defect_report_summary, execution_summary)
{'total_tests_executed': 120, 'pass_count': 117, 'defect_density': 0.025, 'risk_assessment_rating': 6}
```

```python
>>> defect_report_summary = '{"defects": 0, "details": []}'
>>> execution_summary = '{"tests_executed": 80, "passes": 80}'
>>> result = generate_test_report(defect_report_summary, execution_summary)
{'total_tests_executed': 80, 'pass_count': 80, 'defect_density': 0.0, 'risk_assessment_rating': 2}
```
