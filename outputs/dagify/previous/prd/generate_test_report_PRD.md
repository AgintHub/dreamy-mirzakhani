# generate_test_report PRD

## Description
Compile test results summary


## Conceptual Info

This node takes the aggregated test results and outputs a test summary containing total tests executed, pass/fail counts, defect density, and risk assessment rating.

## Docstring

### Summary
Takes the aggregated test results and outputs a test summary.

### Parameters

- **report_defects** (report_defects): Aggregated test results

### Returns

dict: Test summary with total tests executed, pass/fail counts, defect density, and risk assessment rating.

### Raises

- Error: If there's an error aggregating the test results

### Examples

```python
>>> def generate_test_report(report_defects)
...     # Assuming report_defects is a dictionary with aggregated test results"
                "    total_tests_executed = report_defects['total_tests_executed']"
                "    pass_count = report_defects['pass_count']"
                "    defect_density = report_defects['defect_density']"
                "    risk_assessment_rating = report_defects['risk_assessment_rating']"
                "    return {'total_tests_executed': total_tests_executed, 'pass_count': pass_count, 'defect_density': defect_density, 'risk_assessment_rating': risk_assessment_rating}
{"total_tests_executed": 100, "pass_count": 90, "defect_density": 0.02, "risk_assessment_rating": 5}
```
