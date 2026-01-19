# simple_test_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'simple_test_workflow' module.

## Table of Contents

- [define_test_case_1](#define_test_case_1)

- [define_test_case_2](#define_test_case_2)

- [execute_test_case_1](#execute_test_case_1)

- [execute_test_case_2](#execute_test_case_2)

- [generate_test_report](#generate_test_report)

- [setup_test_environment](#setup_test_environment)

- [verify_test_results_1](#verify_test_results_1)

- [verify_test_results_2](#verify_test_results_2)



---

## define_test_case_1

### Description
Create a specific test case with defined inputs and expected outcomes

### Conceptual Info

This node defines a specific test case with input data, expected output, and success criteria.

### Docstring

**Summary:** Define a test case with input data, expected output, and success criteria.

**Parameters:**

- input_data (List[str]): List of input data items
- expected_output (List[int]): List of expected output values
- success_criteria (bool): Whether the test case meets the success criteria
**Returns:** dict - Test case defined with input data, expected output, and success criteria.

**Raises:**

- ValueError: If input data is invalid or expected output is not a list of integers.
**Examples:**

```python
>>> input_data = ['data1', 'data2', 'data3']
>>> expected_output = [1, 2, 3]
>>> success_criteria = True
{'input_data': ['data1', 'data2', 'data3'], 'expected_output': [1, 2, 3], 'success_criteria': True}
```

```python
>>> input_data = ['data4', 'data5', 'data6']
>>> expected_output = [4, 5, 6]
>>> success_criteria = False
{'input_data': ['data4', 'data5', 'data6'], 'expected_output': [4, 5, 6], 'success_criteria': False}
```



---

## define_test_case_2

### Description
Create a second specific test case with defined inputs and expected outcomes

### Conceptual Info

This node creates a second specific test case with defined inputs and expected outcomes.

### Docstring

**Summary:** Creates a new test case definition with distinct inputs, expected outputs, and success criteria.

**Parameters:**

- test_case_inputs (PrimitiveType.LIST_STR): List of input values or data for the test case
- expected_outputs (PrimitiveType.LIST_INT): List of expected output values
- success_criteria (PrimitiveType.BOOL): Whether the test case meets the success criteria
**Returns:** dict - A dictionary with keys 'test_case_name', 'input_data', and 'expected_output'

**Examples:**

```python
>>> define_test_case_2(test_case_inputs=['input1', 'input2'], expected_outputs=[1, 2], success_criteria=True)
{'test_case_name': 'test_case_2', 'input_data': 'input1,input2', 'expected_output': '1,2'}
```



---

## execute_test_case_1

### Description
Run the first defined test case in the prepared environment.

### Conceptual Info

Run the first defined test case in the prepared environment, recording actual outputs and behaviours.

### Docstring

**Summary:** Execute the first test case using the defined inputs and expected outcomes.

**Parameters:**

- test_case inputs (object): The inputs to the first test case, including input data and expected outcomes.
- environment_setup (object): The prepared environment for the test case, including setup description, steps, and dependencies.
**Returns:** tuple - test_case_result, actual_outputs, behavioural_results

**Examples:**

```python
>>> test_case_inputs = {'input_data': ['data1', 'data2'], 'expected_output': [1, 2]}
>>> environment_setup = {'setup_description': 'setup 1', 'setup_steps': ['step1', 'step2'], 'dependencies': ['dep1', 'dep2']}
>>> result, actual_outputs, behavioural_results = execute_test_case_1(test_case_inputs, environment_setup)
result: 'pass', actual_outputs: ['output1', 'output2'], behavioural_results: ['behaviour1', 'behaviour2']
```



---

## execute_test_case_2

### Description
Run the second defined test case in the prepared environment

### Conceptual Info

Execute the second test case defined by inputs in a prepared environment, recording all actual outputs and behaviors.

### Docstring

**Summary:** Execute a test case using the defined inputs, recording actual outputs and behaviors.

**Parameters:**

- test_case_definition (dict): Output structure of a test case definition.
- prepared_environment (dict): Output structure of a prepared test environment.
**Returns:** dict - {test_case_name: Name of the executed test case, inputs_tested: List of inputs used for the test case, actual_outputs: Recorded actual outputs from the test case execution, pass_fail_status: Whether the test case passed or failed, verifier_notes: Notes from the verifier regarding the test case results}

**Raises:**

- Exception: Raised when there is an error in test case execution.
**Examples:**

```python
>>> result = execute_test_case_2(test_case_definition, prepared_environment)
>>> print(result['test_case_name'])
>>> print(result['actual_outputs'])
{'test_case_name': 'Test Case 2', 'actual_outputs': ['output1', 'output2']}
```

```python
>>> result = execute_test_case_2(test_case_definition, prepared_environment)
>>> if result['pass_fail_status'] == True:
...   print('Test Case Passed')
{'test_case_name': 'Test Case 2', 'pass_fail_status': True}
```



---

## generate_test_report

### Description
Create documentation summarizing all test execution and verification results

### Conceptual Info

This node collects and summarizes the test results from the previous test cases, providing a comprehensive report.

### Docstring

**Summary:** Compilation of test case names, inputs, pass/fail status, and key verification notes.

**Parameters:**

- test_results_1 (dict): Output of the verify_test_results_1 node
- test_results_2 (dict): Output of the verify_test_results_2 node
**Returns:** dict - A dictionary containing the compiled test case information, with keys corresponding to each test case.

**Raises:**

- ValueError: If either test_results_1 or test_results_2 is empty or invalid.
**Examples:**

```python
>>> test_results_1 = {'test_case_name': 'Test Case 1', 'input_data': 'Data 1', 'expected_output': 'Output 1', 'actual_output': 'Output 1', 'pass_fail_status': 'Passed'}
>>> test_results_2 = {'test_case_name': 'Test Case 2', 'input_data': 'Data 2', 'expected_output': 'Output 2', 'actual_output': 'Output 2', 'pass_fail_status': 'Passed'}
>>> generate_test_report(test_results_1, test_results_2)
''
{
  "test_case_name": "Test Case 1",
  "input_data": "Data 1",
  "expected_output": "Output 1",
  "actual_output": "Output 1",
  "pass_fail_status": "Passed"
}
{
  "test_case_name": "Test Case 2",
  "input_data": "Data 2",
  "expected_output": "Output 2",
  "actual_output": "Output 2",
  "pass_fail_status": "Passed"
}''
```



---

## setup_test_environment

### Description
Prepare prerequisite environment or resources required for testing

### Conceptual Info

This node is responsible for setting up the environment for testing by providing a clear description of the necessary steps, tools, and dependencies.

### Docstring

**Summary:** Setup the environment for testing by executing the necessary setup steps and providing a clear record of dependencies.

**Returns:** dict - A dictionary containing environment setup description, setup steps, and dependencies.

**Raises:**

- ValueError: If the required environment setup steps are not provided or if the necessary tools and dependencies are missing.
**Examples:**

```python
>>> setup_description = 'Test environment setup for data analysis'
>>> setup_steps = ['Create a test database', 'Install relevant libraries', 'Configure test data']
>>> dependencies = ['Python 3.9', 'numpy', 'pandas']
{'setup_description': 'Test environment setup for data analysis', 'setup_steps': ['Create a test database', 'Install relevant libraries', 'Configure test data'], 'dependencies': ['Python 3.9', 'numpy', 'pandas']}
```



---

## verify_test_results_1

### Description
Validate the first test's actual outputs against expected outcomes

### Conceptual Info

Validate the first test's actual outputs against expected outcomes to determine if they match without discrepancies.

### Docstring

**Summary:** Verify test results against expected outcomes for the first test case.

**Parameters:**

- test_case_result (str): Test case result from the first test execution.
- actual_outputs (list[str]): List of actual outputs from the first test execution.
- expected_output (list[int]): List of expected output values from the test case definition.
**Returns:** (list[str], bool) - Returns a tuple containing a list of discrepancy descriptions and a boolean indicating if the test passed.

**Raises:**

- ValueError: If the actual outputs do not match the expected outcomes.
**Examples:**

```python
>>> test_case_result = 'pass'
>>> actual_outputs = ['output1', 'output2']
>>> expected_output = [1, 2]
>>> discrepancies, test_passed = verify_test_results_1(test_case_result, actual_outputs, expected_output)
>>> print(discrepancies)
>>> print(test_passed)
[] False
```

```python
>>> test_case_result = 'fail'
>>> actual_outputs = ['output1', 'output2']
>>> expected_output = [1, 2]
>>> discrepancies, test_passed = verify_test_results_1(test_case_result, actual_outputs, expected_output)
>>> print(discrepancies)
>>> print(test_passed)
['Test failed'] False
```



---

## verify_test_results_2

### Description
Validate the second test's actual outputs against expected outcomes

### Conceptual Info

Validate actual test outputs against expected outcomes to identify discrepancies.

### Docstring

**Summary:** Validate actual test outputs against expected outcomes.

**Parameters:**

- execute_test_case_2 (dict): Second test case execution results
**Returns:** dict - Validation results including actual and expected outputs, discrepancies and pass status.

**Raises:**

- ValueError: If actual or expected outputs are not valid.
**Examples:**

```python
>>> execute_test_case_2 = {'test_case_name': 'test-case-1', 'inputs_tested': ['input1', 'input2'], 'actual_outputs': ['output1', 'output2'], 'pass_fail_status': 'pass'}
>>> verify_test_results_2(execute_test_case_2)
{"test_case_name": 'test-case-1', "actual_outputs": ['output1', 'output2'], "expected_outputs": ['expected_output1', 'expected_output2'], "discrepancies": [], "pass_status": true}
```

