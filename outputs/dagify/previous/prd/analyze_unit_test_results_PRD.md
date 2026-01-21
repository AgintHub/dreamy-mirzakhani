# analyze_unit_test_results PRD

## Description
Aggregate testing anomalies from unit test results and create a defect summary table.


## Conceptual Info

Transform raw unit-test results into a concise defect-record suitable for defect triage. This node distills pass/fail signals and diffs from run_unit_tests into a single defect row that is consumed by report_defects.

## Docstring

### Summary
Aggregate unit test anomalies and produce a single defect summary record.

### Parameters

- **test_execution_status** (List[bool]): Pass/fail status for each unit test from run_unit_tests.
- **actual_output_vs_expected_output** (List[str]): Differences between actual and expected outputs for each test.
- **test_case_timestamps** (List[str]): Timestamps for each test execution.

### Returns

Dict[str, str]: A single defect summary record represented as a dictionary with keys: test_type, component_info, description, severity, reproduction_steps.

### Raises

- TypeError: If inputs are not lists or not of the expected element types.
- ValueError: If input lists have mismatched lengths.

### Examples

```python
>>> analyze_unit_test_results([False], ["expected 3, got 2"], ["2025-01-01 10:00:00"])
{\'test_type\': \'unit\', \'component_info\': \'Unknown\', \'description\': \'Unit test failure: expected 3, got 2\', \'severity\': \'high\', \'reproduction_steps\': \'Failed test at 2025-01-01 10:00:00; diff: expected 3, got 2\'}
```

```python
>>> analyze_unit_test_results([True, True], ["", ""], ["2025-01-01 10:05:00","2025-01-01 10:06:00"])
{\'test_type\': \'unit\', \'component_info\': \'Unknown\', \'description\': \'No unit test anomalies detected.\', \'severity\': \'low\', \'reproduction_steps\': \'N/A\'}
```
