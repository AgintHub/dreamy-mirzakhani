# analyze_results PRD

## Description
Analyze the table of test execution outcomes produced by `execute_tests` and produce a concise list of key insights, categorizing failures and highlighting recurring error patterns.


## Conceptual Info

The `analyze_results` node consumes the execution status table from its parent `execute_tests` node and extracts actionable insights. It identifies overall failure rates, groups failures by type (e.g., assertion failure, timeout, exception), and reports any error messages that recur across multiple tests. The output is a human‑readable summary intended for report generation and further process review.

## Docstring

### Summary
Generate a concise bullet‑point summary of test execution results.

### Parameters

- **test_results_table** (str): Markdown table string produced by `execute_tests` with columns "Test Name" and "Status". Each row ends with a newline and status may include a timestamp or detailed status string such as "PASS", "FAIL", or "ERROR: ...".

### Returns

str: Markdown-formatted bullet points summarizing key findings, including total tests, pass/fail counts, common failure types, and any notable error patterns.

### Raises

- ValueError: Raised if `test_results_table` is empty or not in the expected table format.
- RuntimeError: Raised if no failure entries are found but the user expects a summary of issues.

### Examples

```python
>>> test_results = """
>>> Test Name | Status
>>> --------- | ------
>>> login_test | PASS
>>> payment_test | FAIL
>>> logout_test | PASS
>>> checkout_test | ERROR: Timeout"""
>>> summary = analyze_results(test_results)
• 4 tests executed: 2 passed, 1 failed, 1 error.
• Most common failure: `ERROR: Timeout` occurred in `checkout_test`.
• No assertion failures detected.
• Recommend investigating network stability for timeout issues.
```

```python
>>> test_results = """
>>> Test Name | Status
>>> --------- | ------
>>> search_test | PASS
>>> filter_test | PASS"""
>>> summary = analyze_results(test_results)
• 2 tests executed: 2 passed.
• No failures detected.
• All tests passed successfully.
```
