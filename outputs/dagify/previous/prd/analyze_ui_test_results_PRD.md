# analyze_ui_test_results PRD

## Description
validate frontend interface functionality


## Conceptual Info

This node validates frontend interface functionality by analyzing visual validation results and interaction logs.

## Docstring

### Summary
This node audits visual validation results and interaction logs to categorize issues by severity and UX impact.

### Returns

output_structure -> (str, str, list, list, int, bool, list): Returns a tuple containing the visual validation results, interaction logs, severity issues, issue descriptions, total issues count, validity status, and UX impact categories.

### Raises

- TypeError: If the input test results or interaction logs are not in the correct format.

### Examples

```python
>>> test_outcomes = ['pass', 'fail']
>>> test_execution_time = [1.0, 2.0]
>>> analyze_ui_test_results(test_outcomes, test_execution_time)
({"visual_validation_results": 'OK', "interaction_logs": 'No issues found', "severity_issues": [], "issue_description": [], "total_issues_count": 0, "validity_status": True, "ux_impact_categories": []})
```

```python
>>> test_outcomes = ['fail', 'fail']
>>> test_execution_time = [1.0, 2.0]
>>> analyze_ui_test_results(test_outcomes, test_execution_time)
({"visual_validation_results": 'Error', "interaction_logs": 'Issues found', "severity_issues": ['critical'], "issue_description": ['description of issue'], "total_issues_count": 2, "validity_status": False, "ux_impact_categories": ['category']})
```
