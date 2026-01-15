# execute_tests PRD

## Description
Run the prepared test cases, capture the pass/fail status of each test, and record the execution timestamp. The output is a concise table listing each test name alongside its result.


## Conceptual Info

The execute_tests node orchestrates the actual execution of all defined test cases, ensuring that each test runs in the configured environment with the appropriate data and scripts. It aggregates the results into a human‑readable table for subsequent analysis.

## Docstring

### Summary
Execute all test cases and record their status in a table.

### Parameters

- **test_cases** (str): A string containing the detailed description of each test case (as produced by create_test_cases).
- **setup_status** (str): Status of the environment setup (e.g., 'Completed').
- **data_quality_metrics** (List[float]): Quality metrics of the prepared data to verify data integrity before execution.
- **script_names** (List[str]): Names of the test scripts to be executed.

### Returns

List[str]: A list of markdown table rows. The first row is the header 'Test Name | Status | Timestamp', followed by one row per test case with the test name, pass/fail status, and the UTC timestamp of execution.

### Raises

- RuntimeError: If the environment setup status is not 'Completed' or if any setup error is present.
- ValueError: If any of the input parameters are missing or of incorrect type.

### Examples

```python
>>> table = execute_tests(
...     test_cases='Test 1: ...\nTest 2: ...',
...     setup_status='Completed',
...     data_quality_metrics=[0.99, 0.98],
...     script_names=['test_login.py', 'test_payment.py']
>>> )
>>> print('\n'.join(table))
Test Name | Status | Timestamp\n--- | --- | ---\nTest 1 | Pass | 2026-01-15T12:34:56Z\nTest 2 | Fail | 2026-01-15T12:34:56Z
```

```python
>>> execute_tests('', 'Failed', [0.97], ['test1.py'])
RuntimeError: Environment setup not completed.
```
