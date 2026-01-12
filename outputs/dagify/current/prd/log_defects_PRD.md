# log_defects PRD

## Description
Record failed test cases with diagnostic information


## Conceptual Info

The log_defects node aggregates all failed test executions from unit, integration, and system test runs. It transforms raw failure metadata into a structured defect record that can be imported into a tracking system. Each defect record includes reproduction steps, expected vs actual outcomes, severity classification, and a unique defect ID for downstream retesting.

## Docstring

### Summary
Create defect logs from failed test results.

### Parameters

- **unit_results** (dict): Dictionary containing unit test execution results. Expected keys: 'test_case_ids', 'failed_test_ids', 'failure_descriptions', 'is_successful'. Each failure description should include the test name, timestamp, environment, reproduction steps, expected and actual results.
- **integration_results** (dict): Dictionary containing integration test execution results. Expected keys: 'test_case_id', 'execution_status', 'error_message', 'component_under_test', 'execution_time_seconds', 'affected_components', 'is_stable'. For each failed test, the error_message and component information are required.
- **system_results** (dict): Dictionary containing system test execution results. Expected keys: 'test_case_ids', 'passed_flags', 'defect_ids', 'execution_times', 'overall_pass_rate'. For each failed test, the corresponding defect_id must be provided.
- **severity_map** (dict): Optional mapping from textual severity to numeric code. Keys are severity strings ('Low', 'Medium', 'High', 'Critical') and values are integers 1–4. If omitted, a default mapping is used.

### Returns

List[Dict[str, Any]]: A list of defect dictionaries, each matching the output structure defined above.

### Raises

- ValueError: If required fields are missing from any of the input result dictionaries.
- TypeError: If the input arguments are not of the expected types.

### Examples

```python
>>> unit_results = {
...     'test_case_ids': ['UC1', 'UC2'],
...     'failed_test_ids': ['UC2'],
...     'failure_descriptions': ['Failed due to timeout'],
...     'is_successful': False
>>> }
>>> integration_results = {
...     'test_case_id': ['IT1', 'IT2'],
...     'execution_status': [True, False],
...     'error_message': ['', 'NullPointerException'],
...     'component_under_test': ['AuthService', 'AuthService'],
...     'execution_time_seconds': [0.12, 0.47],
...     'affected_components': ['AuthService'],
...     'is_stable': False
>>> }
>>> system_results = {
...     'test_case_ids': ['ST1'],
...     'passed_flags': [False],
...     'defect_ids': ['D123'],
...     'execution_times': [3.5],
...     'overall_pass_rate': 0.0
>>> }
>>> defect_logs = log_defects(unit_results, integration_results, system_results)
>>> print(defect_logs[0]['test_case_id'])
UC2
```

```python
>>> # Using a custom severity map
>>> severity_map = {'Low': 1, 'Medium': 2, 'High': 3, 'Critical': 4}
>>> defect_logs = log_defects(unit_results, integration_results, system_results, severity_map)
>>> print(defect_logs[1]['severity_code'])
3
```
