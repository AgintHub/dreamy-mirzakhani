# analyze_unit_test_results PRD

## Description
Aggregate testing anomalies.


## Conceptual Info

Aggregate testing anomalies by creating a defect summary table.

## Docstring

### Summary
Create a defect summary table from unit test results.

### Parameters

- **test_execution_status** (PrimitiveType.LIST_BOOL): Pass/fail status of each test case from the run_unit_tests node
- **actual_output_vs_expected_output** (PrimitiveType.LIST_STR): Difference between actual and expected output of each test case from the run_unit_tests node
- **test_case_timestamps** (PrimitiveType.LIST_STR): Timestamps for each test execution from the run_unit_tests node

### Returns

{test_type: PrimitiveType.STR, component_info: PrimitiveType.STR, description: PrimitiveType.STR, severity: PrimitiveType.STR, reproduction_steps: PrimitiveType.STR}: A defect summary table with columns: Test Type | Component | Description | Severity | Reproduction Steps.

### Raises

- TypeError: If the inputs from run_unit_tests node are not valid

### Examples

```python
>>> def run_unit_tests(test_execution_status, actual_output_vs_expected_output, test_case_timestamps):"
                "	test_results = []"
                "	for status, output, timestamp in zip(test_execution_status, actual_output_vs_expected_output, test_case_timestamps):"
                "		test_results.append("Test Type: unit, Component: , Description: , Severity: , Reproduction Steps: ")"
                "	return test_results"
                ""
                "analyze_unit_test_results = run_unit_tests([True, False, True], ['passed', 'failed', 'passed'], ['2022-01-01 12:00:00', '2022-01-01 12:01:00', '2022-01-01 12:02:00'])
["Test Type: unit, Component: , Description: , Severity: , Reproduction Steps: ", "Test Type: unit, Component: , Description: , Severity: , Reproduction Steps: ", "Test Type: unit, Component: , Description: , Severity: , Reproduction Steps: "]
```
