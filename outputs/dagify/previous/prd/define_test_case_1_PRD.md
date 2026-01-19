# define_test_case_1 PRD

## Description
Create a specific test case with defined inputs and expected outcomes


## Conceptual Info

This node defines a specific test case with input data, expected output, and success criteria.

## Docstring

### Summary
Define a test case with input data, expected output, and success criteria.

### Parameters

- **input_data** (List[str]): List of input data items
- **expected_output** (List[int]): List of expected output values
- **success_criteria** (bool): Whether the test case meets the success criteria

### Returns

dict: Test case defined with input data, expected output, and success criteria.

### Raises

- ValueError: If input data is invalid or expected output is not a list of integers.

### Examples

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
