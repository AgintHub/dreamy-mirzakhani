# generate_test_report PRD

## Description
Create documentation of test results


## Conceptual Info

The node aggregates the findings from analyze_results into a human‑readable report that highlights overall success, key performance indicators, and actionable observations.

## Docstring

### Summary
Generate a concise, numbered test report from the analysis of test execution results.

### Parameters

- **analysis_bullet_points** (List[str]): Bullet‑point list produced by the analyze_results node, each point describing a key finding (e.g., failures, error patterns, trends).

### Returns

Tuple[str, List[str], str]: A tuple containing the test results summary, a list of key metrics, and a string of observations.

### Raises

- ValueError: Raised if the input list is empty or contains non‑string items.

### Examples

```python
>>> analysis_bullet_points = [
...     '- 10 test cases executed, 8 passed, 2 failed.',
...     '- Failure type: AssertionError in TestLogin, occurred 2 times.',
...     '- Error pattern: Timeout in API calls observed in 3 tests.',
...     '- Performance: Average response time 250ms.',
...     '- Coverage: Code coverage 85%.',
>>> ]
>>> summary, metrics, obs = generate_test_report(analysis_bullet_points)
>>> print(summary)
>>> print(metrics)
>>> print(obs)
"Test Execution Summary:\n- 10 test cases executed, 8 passed, 2 failed.\n"\n["Total Tests: 10", "Pass Rate: 80%", "Fail Rate: 20%", "Avg Response Time: 250ms", "Coverage: 85%"]\n"Observations:\n- AssertionErrors indicate potential login logic issues.\n- Timeouts suggest network instability.\n- Overall coverage acceptable but can be improved in authentication module."
```

```python
>>> analysis_bullet_points = [
...     '- No failures detected.',
...     '- Performance within acceptable limits.',
...     '- Code coverage 92%.',
>>> ]
>>> summary, metrics, obs = generate_test_report(analysis_bullet_points)
>>> print(summary)
>>> print(metrics)
>>> print(obs)
"Test Execution Summary:\n- No failures detected.\n"\n["Total Tests: 0", "Pass Rate: 100%", "Coverage: 92%"]\n"Observations:\n- All tests passed successfully.\n- Performance metrics meet thresholds."
```
