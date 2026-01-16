# generic_test_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'generic_test_workflow' module.

## Table of Contents

- [analyze_failures](#analyze_failures)

- [capture_test_results](#capture_test_results)

- [create_test_cases](#create_test_cases)

- [define_test_objectives](#define_test_objectives)

- [execute_test_cases](#execute_test_cases)

- [identify_test_scope](#identify_test_scope)

- [prepare_test_environment](#prepare_test_environment)

- [report_test_results](#report_test_results)



---

## analyze_failures

### Description
Investigate why tests failed.

### Conceptual Info

The analyze_failures node investigates the root causes of failed test cases and suggests potential fixes.

### Docstring

**Summary:** Analyze failed test cases to determine their root causes and suggest fixes.

**Parameters:**

- test_results (dict): Test results from the capture_test_results node, including test_case_ids, pass_fail_status, execution_times, failure_details, total_tests, total_passed, and total_failed.
**Returns:** List[dict] - A list of dictionaries containing the test_id, root_cause_hypothesis, and fix_suggestion for each failed test case.

**Raises:**

- ValueError: If the input test results are invalid or incomplete.
**Examples:**

```python
>>> test_results = {
...   'test_case_ids': ['test1', 'test2', 'test3'],
...   'pass_fail_status': [True, False, True],
...   'execution_times': [1.0, 2.0, 3.0],
...   'failure_details': ['', 'AssertionError', ''],
...   'total_tests': 3,
...   'total_passed': 2,
...   'total_failed': 1
>>> }
>>> analyze_failures(test_results)
[{'test_id': 'test2', 'root_cause_hypothesis': 'Assertion error in test2', 'fix_suggestion': 'Verify the assertion in test2'}]
```



---

## capture_test_results

### Description
Aggregate raw results from the test run.

### Conceptual Info

This node aggregates raw results from the test run, collecting data on pass/fail status, execution time, and failure details for each test case.

### Docstring

**Summary:** Captures and aggregates test execution data from the output of execute_test_cases node.

**Parameters:**

- test_case_results (List[Dict[str, Any]]): List of dictionaries containing test case execution results, each with 'test_case_id', 'passed', 'failure_reason', 'execution_time' keys.
**Returns:** Dict[str, Any] - Dictionary containing aggregated test results, including lists of test case IDs, pass/fail status, execution times, failure details, and totals for tests, passed, and failed.

**Raises:**

- ValueError: If the input test_case_results is empty or contains invalid data.
**Examples:**

```python
>>> capture_test_results([
...     {'test_case_id': 'TC1', 'passed': True, 'failure_reason': None, 'execution_time': 10.0},
...     {'test_case_id': 'TC2', 'passed': False, 'failure_reason': 'Assertion error', 'execution_time': 5.0}
>>> ])
{'test_case_ids': ['TC1', 'TC2'], 'pass_fail_status': [True, False], 'execution_times': [10.0, 5.0], 'failure_details': [None, 'Assertion error'], 'total_tests': 2, 'total_passed': 1, 'total_failed': 1}
```



---

## create_test_cases

### Description
Develop individual test cases that will be executed.

### Conceptual Info

This node generates individual test cases based on the defined test objectives and identified test scope.

### Docstring

**Summary:** Creates a list of test cases with their respective IDs, titles, preconditions, steps, expected results, and priority levels.

**Parameters:**

- test_objectives (List[str]): List of primary objectives of the test suite
- test_scope (Dict[str, List[str]]): Dictionary containing the test scope features, modules, user flows, and boundary conditions
**Returns:** Dict[str, List[str] or List[int]] - Dictionary containing the test case IDs, titles, preconditions, steps, expected results, and priority levels

**Raises:**

- ValueError: If the test objectives or test scope are invalid or empty
**Examples:**

```python
>>> test_objectives = ['Verify functionality', 'Verify performance']
>>> test_scope = {'features': ['feature1', 'feature2'], 'modules': ['module1', 'module2']}
>>> test_cases = create_test_cases(test_objectives, test_scope)
{'test_case_ids': ['TC-1', 'TC-2'], 'test_case_titles': ['Test Case 1', 'Test Case 2'], 'preconditions': ['Precondition 1', 'Precondition 2'], 'test_steps': ['Step 1', 'Step 2'], 'expected_results': ['Result 1', 'Result 2'], 'priority_levels': [1, 2]}
```



---

## define_test_objectives

### Description
Establish the main goals that the test suite should achieve.

### Conceptual Info

This node defines the strategic objectives that guide the entire testing effort, ensuring that all subsequent test cases, scopes, and environments are aligned with these high‑level goals.

### Docstring

**Summary:** Generate a list of primary test objectives from a concise natural‑language prompt.

**Parameters:**

- prompt_text (str): Human‑readable instruction asking for the main objectives of the test suite.
**Returns:** List[str] - A list of bullet‑point strings, each describing a primary test objective such as functionality verification, performance assessment, or security validation.

**Raises:**

- ValueError: If `prompt_text` is empty or does not contain any actionable instruction.
**Examples:**

```python
>>> objective_list = define_test_objectives("List the primary objectives of the test in concise bullet points.")
['Verify functional correctness', 'Assess performance under load', 'Validate security controls']
```

```python
>>> objective_list = define_test_objectives("Identify core goals for the test suite.")
['Ensure feature parity with specifications', 'Confirm regression safety', 'Detect potential security vulnerabilities']
```



---

## execute_test_cases

### Description
Perform the actual test execution.

### Conceptual Info

Executes a sequence of pre‑defined test cases in a prepared environment, capturing detailed pass/fail data, diagnostics, and visual evidence for any failures.

### Docstring

**Summary:** Run each test case and record detailed execution results.

**Parameters:**

- test_cases (List[Dict[str, Any]]): List of test case dictionaries produced by the `create_test_cases` node. Each dictionary must contain `test_case_id`, `title`, `preconditions`, `steps`, `expected_results`, and `priority` keys.
- environment_ready (bool): Flag indicating that the environment setup from `prepare_test_environment` is complete. If False, execution is aborted.
- capture_screenshots (bool): Whether to capture screenshots on failure. If True, a screenshot path or URL is stored in the `screenshot` field.
**Returns:** List[Dict[str, Any]] - A list of result dictionaries, one per test case, matching the node's output structure.

**Raises:**

- RuntimeError: If `environment_ready` is False, indicating the test environment is not prepared.
- ValueError: If any required key is missing from a test case definition.
**Examples:**

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



---

## identify_test_scope

### Description
Determine the boundaries and focus areas of the testing effort.

### Conceptual Info

This node determines the scope of the testing effort based on the defined test objectives.

### Docstring

**Summary:** Identify the test scope by analyzing the test objectives and specifying features, modules, user flows, and boundary conditions.

**Parameters:**

- test_objectives (List[str]): A list of concise bullet points describing the primary objectives of the test suite.
**Returns:** Dict[str, List[str]] - A dictionary containing the test scope, including features, modules, user flows, and boundary conditions.

**Raises:**

- ValueError: If the test objectives are empty or invalid.
**Examples:**

```python
>>> test_objectives = ['Verify functionality', 'Test performance']
>>> test_scope = identify_test_scope(test_objectives)
{'scope_features': ['feature1', 'feature2'], 'scope_modules': ['module1', 'module2'], 'scope_user_flows': ['user_flow1', 'user_flow2'], 'scope_boundary_conditions': ['boundary_condition1', 'boundary_condition2']}
```



---

## prepare_test_environment

### Description
Set up the necessary test environment.

### Conceptual Info

Prepares a complete, reproducible test environment by enumerating all necessary hardware, software, data, and configuration steps, and signals readiness for execution.

### Docstring

**Summary:** Generate a checklist of environment setup steps required for executing the test suite.

**Parameters:**

- scope_features (List[str]): List of feature names that will be included in the test scope.
- scope_modules (List[str]): List of module or component identifiers that fall within the test scope.
- scope_user_flows (List[str]): List of high‑level user flow identifiers that are covered by the tests.
- scope_boundary_conditions (List[str]): List of boundary or edge case conditions that the tests will exercise.
**Returns:** Dict[str, Any] - A dictionary containing five keys: hardware_requirements, software_requirements, data_setup_steps, configuration_steps, and environment_ready.

**Raises:**

- ValueError: If any of the scope inputs are empty or None, indicating insufficient context to determine environment needs.
**Examples:**

```python
>>> env = prepare_test_environment(
...     scope_features=["Login", "Checkout"],
...     scope_modules=["auth_service", "payment_gateway"],
...     scope_user_flows=["user_login_flow", "user_checkout_flow"],
...     scope_boundary_conditions=["max_session_time", "zero_payment_amount"]
>>> )
>>> print(env["hardware_requirements"])
["NVIDIA RTX 3080 GPU", "8x Intel Xeon CPUs"]
```

```python
>>> env = prepare_test_environment(
...     scope_features=[],
...     scope_modules=[],
...     scope_user_flows=[],
...     scope_boundary_conditions=[]
>>> )
ValueError: Scope inputs cannot be empty.
```



---

## report_test_results

### Description
Create the final test report.

### Conceptual Info

Aggregates summarized metrics from raw test execution data to produce a concise, human‑readable test report.

### Docstring

**Summary:** Generate a summary report of test execution results.

**Parameters:**

- test_case_ids (list[str]): List of test case identifiers.
- pass_fail_status (list[bool]): Boolean list indicating pass (True) or fail (False) for each test case.
- execution_times (list[float]): Execution time in seconds for each test case.
- failure_details (list[str]): Failure details for each failed test case; empty strings for passed cases.
- total_tests (int): Total number of tests executed.
- total_passed (int): Total number of tests passed.
- total_failed (int): Total number of tests failed.
**Returns:** dict - A dictionary containing summarized test metrics.

**Raises:**

- ValueError: Raised if input lists are of mismatched lengths or if total_counts do not match list lengths.
**Examples:**

```python
>>> report = report_test_results(

...     test_case_ids=['TC1', 'TC2', 'TC3'],

...     pass_fail_status=[True, False, True],

...     execution_times=[0.12, 0.45, 0.08],

...     failure_details=['', 'AssertionError: expected 5, got 3', ''],

...     total_tests=3,

...     total_passed=2,

...     total_failed=1

>>> )
{
  "total_tests": 3,
  "passed_tests": 2,
  "failed_tests": 1,
  "pass_rate": 66.66666666666666,
  "observations": "2 tests passed, 1 failed. Majority of failures due to assertion errors."
}
```

```python
>>> report = report_test_results(

...     test_case_ids=['A', 'B'],

...     pass_fail_status=[False, False],

...     execution_times=[0.5, 0.6],

...     failure_details=['Timeout', 'NullPointerException'],

...     total_tests=2,

...     total_passed=0,

...     total_failed=2

>>> )
{
  "total_tests": 2,
  "passed_tests": 0,
  "failed_tests": 2,
  "pass_rate": 0.0,
  "observations": "All tests failed. Common issues: timeouts and null references."
}
```

