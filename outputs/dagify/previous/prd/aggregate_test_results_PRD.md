# aggregate_test_results PRD

## Description
Compile and analyze test outcomes from all test suites, producing a unified view of pass/fail metrics, failure diagnostics, false‑positive detection, and performance insights.


## Conceptual Info

The node consolidates raw results from unit, integration, system, and acceptance test suites into a single, analytics‑rich report. It quantifies overall quality, surfaces recurring failures, filters out false positives, and highlights performance hot‑spots to support decision‑making and downstream documentation generation.

## Docstring

### Summary
Aggregate results from all test suites, compute overall metrics, and generate a diagnostic summary.

### Parameters

- **unit_results** (dict): Output dictionary from `unit_test_suite` containing total_tests, passed_tests, failed_tests, failed_test_names, error_messages, and is_successful.
- **integration_results** (dict): Output dictionary from `integration_test_suite` containing executed_test_cases, passed_test_cases, failed_test_cases, overall_success, execution_time_seconds, and error_messages.
- **system_results** (dict): Output dictionary from `system_test_suite` containing total_test_cases, passed_test_cases, failed_test_cases, pass_rate_percentage, critical_failure_detected, average_response_time_ms, performance_metrics_ms, and error_messages.
- **acceptance_results** (dict): Output dictionary from `acceptance_test_suite` containing executed_test_cases, passed_test_cases, failed_test_cases, overall_pass, pass_rate, and defect_summary.

### Returns

dict: Aggregated test report matching the node's output_structure; keys are the field names listed above.

### Raises

- ValueError: If any input dictionary is missing required keys or contains non‑numeric counts that prevent aggregation.
- RuntimeError: If the function cannot compute average execution time due to zero total tests.

### Examples

```python
>>> unit_results = {
...     'total_tests': 120,
...     'passed_tests': 115,
...     'failed_tests': 5,
...     'failed_test_names': ['utils.test_add', 'db.test_connection'],
...     'error_messages': ['AssertionError', 'TimeoutError'],
...     'is_successful': False
>>> }
>>> integration_results = {
...     'executed_test_cases': ['api.login', 'api.logout'],
...     'passed_test_cases': ['api.login'],
...     'failed_test_cases': ['api.logout'],
...     'overall_success': False,
...     'execution_time_seconds': 42.7,
...     'error_messages': ['500 Internal Server Error']
>>> }
>>> system_results = {
...     'total_test_cases': 30,
...     'passed_test_cases': 28,
...     'failed_test_cases': 2,
...     'pass_rate_percentage': 93.33,
...     'critical_failure_detected': False,
...     'average_response_time_ms': 210.5,
...     'performance_metrics_ms': [200, 215, 210],
...     'error_messages': ['UI element not found']
>>> }
>>> acceptance_results = {
...     'executed_test_cases': ['login_flow', 'checkout_flow'],
...     'passed_test_cases': ['login_flow'],
...     'failed_test_cases': ['checkout_flow'],
...     'overall_pass': False,
...     'pass_rate': 0.5,
...     'defect_summary': 'Checkout fails on discount code.'
>>> }
>>> report = aggregate_test_results(
...     unit_results, integration_results, system_results, acceptance_results
>>> )
>>> print(report['summary_report'])
"Total tests executed: 182\nPassed: 144 (79.12%)\nFailed: 38 (20.88%)\nFailures: utils.test_add (AssertionError), db.test_connection (TimeoutError), api.logout (500 Internal Server Error), UI element not found, checkout_flow (business rule violation)\nFalse positives: []\nPerformance bottlenecks: average response time 0.21 s (system tests)\nOverall pass rate: 0.7912"
```
