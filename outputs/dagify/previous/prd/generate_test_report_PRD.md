# generate_test_report PRD

## Description
Compile statistical analysis and recommendations


## Conceptual Info

generate_test_report aggregates unit, integration, system, and retest results to produce a concise statistical summary, defect overview, trend assessment, and a release readiness flag.

## Docstring

### Summary
Generate a comprehensive test report from multiple test stages.

### Parameters

- **unit_results** (dict): Output dictionary from execute_unit_tests. Expected keys: test_case_ids, passed_count, failed_count, pass_rate, failed_test_ids, failure_descriptions, is_successful.
- **integration_results** (dict): Output dictionary from execute_integration_tests. Expected keys include test_case_id, component_under_test, execution_status, execution_time_seconds, error_message, affected_components, total_tests_run, passed_count, failed_count, is_stable.
- **system_results** (dict): Output dictionary from execute_system_tests. Expected keys include test_case_ids, passed_flags, execution_times, defect_ids, total_tests, total_passed, total_failed, overall_pass_rate.
- **retest_results** (dict): Output dictionary from retest_defects. Expected keys include retested_defect_ids, retest_pass_count, retest_fail_count, overall_retest_success, retest_date, retest_summary.

### Returns

dict: Dictionary containing the aggregated test statistics, defect counts, trend score, release readiness flag, and report generation date.

### Raises

- ValueError: If any required key is missing from an input dictionary.
- TypeError: If the type of any input does not match the expected dictionary structure.

### Examples

```python
>>> unit_results = {
...     'test_case_ids': ['UT1', 'UT2'],
...     'passed_count': 2,
...     'failed_count': 0,
...     'pass_rate': 1.0,
...     'failed_test_ids': [],
...     'failure_descriptions': [],
...     'is_successful': True
>>> }
>>> integration_results = {
...     'test_case_id': ['IT1', 'IT2', 'IT3'],
...     'component_under_test': ['CompA', 'CompB', 'CompC'],
...     'execution_status': [True, False, True],
...     'execution_time_seconds': [0.5, 1.2, 0.8],
...     'error_message': ['', 'NullPointer', ''],
...     'affected_components': ['CompA', 'CompB', 'CompC'],
...     'total_tests_run': 3,
...     'passed_count': 2,
...     'failed_count': 1,
...     'is_stable': False
>>> }
>>> system_results = {
...     'test_case_ids': ['ST1', 'ST2', 'ST3', 'ST4'],
...     'passed_flags': [True, True, False, True],
...     'execution_times': [2.3, 1.9, 3.1, 2.0],
...     'defect_ids': ['D1', 'D2'],
...     'total_tests': 4,
...     'total_passed': 3,
...     'total_failed': 1,
...     'overall_pass_rate': 0.75
>>> }
>>> retest_results = {
...     'retested_defect_ids': ['D1'],
...     'retest_pass_count': 1,
...     'retest_fail_count': 0,
...     'overall_retest_success': True,
...     'retest_date': '2026-01-10',
...     'retest_summary': 'All retested defects resolved.'
>>> }
>>> report = generate_test_report(unit_results, integration_results, system_results, retest_results)
>>> print(report['total_tests'])
>>> print(report['defect_count'])
10
2
```

```python
>>> # When all tests pass with no defects
>>> unit_results = {
...     'test_case_ids': ['UT1'],
...     'passed_count': 1,
...     'failed_count': 0,
...     'pass_rate': 1.0,
...     'failed_test_ids': [],
...     'failure_descriptions': [],
...     'is_successful': True
>>> }
>>> integration_results = {
...     'test_case_id': ['IT1'],
...     'component_under_test': ['CompA'],
...     'execution_status': [True],
...     'execution_time_seconds': [0.7],
...     'error_message': [''],
...     'affected_components': ['CompA'],
...     'total_tests_run': 1,
...     'passed_count': 1,
...     'failed_count': 0,
...     'is_stable': True
>>> }
>>> system_results = {
...     'test_case_ids': ['ST1'],
...     'passed_flags': [True],
...     'execution_times': [2.1],
...     'defect_ids': [],
...     'total_tests': 1,
...     'total_passed': 1,
...     'total_failed': 0,
...     'overall_pass_rate': 1.0
>>> }
>>> retest_results = {
...     'retested_defect_ids': [],
...     'retest_pass_count': 0,
...     'retest_fail_count': 0,
...     'overall_retest_success': True,
...     'retest_date': '2026-01-10',
...     'retest_summary': 'No defects to retest.'
>>> }
>>> report = generate_test_report(unit_results, integration_results, system_results, retest_results)
>>> print(report['pass_rate'])
>>> print(report['ready_for_release'])
100.0
True
```
