# define_test_case_2 PRD

## Description
Create a second specific test case with defined inputs and expected outcomes


## Conceptual Info

This node creates a second specific test case with defined inputs and expected outcomes.

## Docstring

### Summary
Creates a new test case definition with distinct inputs, expected outputs, and success criteria.

### Parameters

- **test_case_inputs** (PrimitiveType.LIST_STR): List of input values or data for the test case
- **expected_outputs** (PrimitiveType.LIST_INT): List of expected output values
- **success_criteria** (PrimitiveType.BOOL): Whether the test case meets the success criteria

### Returns

dict: A dictionary with keys 'test_case_name', 'input_data', and 'expected_output'

### Examples

```python
>>> define_test_case_2(test_case_inputs=['input1', 'input2'], expected_outputs=[1, 2], success_criteria=True)
{'test_case_name': 'test_case_2', 'input_data': 'input1,input2', 'expected_output': '1,2'}
```
