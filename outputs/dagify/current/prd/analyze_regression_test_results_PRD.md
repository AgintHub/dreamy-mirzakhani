# analyze_regression_test_results PRD

## Description
Identify regression risks.


## Conceptual Info

Identify regression risks and output feature name, before/after state comparison, impact severity estimation, and regression summary.

## Docstring

### Summary
This function takes the output of the run_regression_tests function and identifies regression risks by extracting the feature name, before/after state comparison, impact severity estimation, and regression summary.

### Parameters

- **run_regression_tests_output** (dict): The output of the run_regression_tests function.

### Returns

dict: A dictionary containing the feature name, before/after state comparison, impact severity estimation, and regression summary.

### Examples

```python
>>> import data
>>> regression_results = run_regression_tests(data)
>>> regression_issues = analyze_regression_test_results(regression_results)
>>> print(regression_issues)
{'feature_name': 'feature_name', 'before_after_state_comparison': 'before/after state comparison', 'impact_severity_estimation': 5, 'regression_summary': 'regression summary'}
```
