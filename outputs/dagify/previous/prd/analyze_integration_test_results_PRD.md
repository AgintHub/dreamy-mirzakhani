# analyze_integration_test_results PRD

## Description
Evaluate component interaction validation


## Conceptual Info

Evaluate integration test results to identify interface mismatches and timing issues, and map errors to source service contracts.

## Docstring

### Summary
Analyze integration test results to identify issues and map errors.

### Returns

dict: Dictionary containing issues found, issue severity levels, collected metrics, and error mapping.

### Examples

```python
>>> result = analyze_integration_test_results(execute_integration_tests())
{'issues_found': ['issue1', 'issue2'], 'issue_severity_levels': ['high', 'medium'], 'metrics_collected': ['execution_time', 'error_rate'], 'error_mapping': {'error1': 'contract1', 'error2': 'contract2'}}
```
