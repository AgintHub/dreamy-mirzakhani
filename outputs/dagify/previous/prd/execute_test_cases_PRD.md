# execute_test_cases PRD

## Description
Perform the actual test execution.


## Conceptual Info

Executes a sequence of pre‑defined test cases in a prepared environment, capturing detailed pass/fail data, diagnostics, and visual evidence for any failures.

## Docstring

### Summary
Run each test case and record detailed execution results.

### Parameters

- **test_cases** (List[Dict[str, Any]]): List of test case dictionaries produced by the `create_test_cases` node. Each dictionary must contain `test_case_id`, `title`, `preconditions`, `steps`, `expected_results`, and `priority` keys.
- **environment_ready** (bool): Flag indicating that the environment setup from `prepare_test_environment` is complete. If False, execution is aborted.
- **capture_screenshots** (bool): Whether to capture screenshots on failure. If True, a screenshot path or URL is stored in the `screenshot` field.

### Returns

List[Dict[str, Any]]: A list of result dictionaries, one per test case, matching the node's output structure.

### Raises

- RuntimeError: If `environment_ready` is False, indicating the test environment is not prepared.
- ValueError: If any required key is missing from a test case definition.

### Examples

```python
>>> test_cases = [
...     {
...         'test_case_id': 'TC001',
...         'title': 'Login success',
...         'preconditions': 'User exists',
...         'steps': 'Enter credentials, click login',
...         'expected_results': 'Redirect to dashboard',
...         'priority': 1
...     }
>>> ]
>>> results = execute_test_cases(test_cases, environment_ready=True, capture_screenshots=False)
>>> print(results[0]['passed'])
True
```

```python
>>> test_cases = [
...     {
...         'test_case_id': 'TC002',
...         'title': 'Password reset',
...         'preconditions': 'User registered',
...         'steps': 'Click forgot password, submit email',
...         'expected_results': 'Email sent with reset link',
...         'priority': 2
...     }
>>> ]
>>> results = execute_test_cases(test_cases, environment_ready=False, capture_screenshots=True)
>>> print(results)
RuntimeError: Test environment not prepared.
```
