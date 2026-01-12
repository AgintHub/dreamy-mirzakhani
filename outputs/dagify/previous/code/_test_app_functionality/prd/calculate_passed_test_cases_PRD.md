# calculate_passed_test_cases PRD

## Description
Calculates the number of passed test cases from unit, integration, and UI test results.


## Conceptual Info

This shim function is designed to calculate the total number of passed test cases by aggregating the results from unit tests, integration tests, and UI tests. It plays a crucial role in assessing the overall success of the test suite.

## Docstring

### Summary
Calculates the total number of passed test cases from various test results.

### Parameters

- **unit_results** (str): A string representing the results of unit tests, potentially containing pass/fail information.
- **integration_results** (str): A string representing the results of integration tests, potentially containing pass/fail information.
- **ui_results** (str): A string representing the results of UI tests, potentially containing pass/fail information.

### Returns

int: The total number of test cases that passed across all provided test results.

### Raises

- ValueError: If any of the input test results are not in the expected format or contain invalid data.
- TypeError: If the input parameters are not of the expected type (str).

### Examples

```python
>>> calculate_passed_test_cases(unit_results='10 passed, 2 failed', integration_results='8 passed, 1 failed', ui_results='5 passed, 0 failed')
23
```

```python
>>> calculate_passed_test_cases(unit_results='5 passed, 0 failed', integration_results='3 passed, 2 failed', ui_results='2 passed, 1 failed')
10
```
