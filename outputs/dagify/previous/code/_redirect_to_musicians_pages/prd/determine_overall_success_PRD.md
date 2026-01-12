# determine_overall_success PRD

## Description
Determines the overall success of the redirection process based on the number of successful redirections and total count.


## Conceptual Info

This shim node assesses the overall success of the redirection process by comparing the number of successful redirections to the total number of redirections attempted.

## Docstring

### Summary
Evaluates the overall success of the redirection process based on the successful count and total count.

### Parameters

- **successful_count** (str): The number of successful redirections as a string.
- **total_count** (str): The total number of redirections attempted as a string.
- **exceptions** (List[str]): A list of exceptions or errors encountered during the redirection process.

### Returns

bool: A boolean indicating whether the overall redirection process was successful.

### Raises

- ValueError: If the successful count or total count cannot be converted to integers.
- TypeError: If the input types are incorrect.

### Examples

```python
>>> successful_count = '8'
>>> total_count = '10'
>>> exceptions = []
>>> result = determine_overall_success(successful_count, total_count, exceptions)
True
```

```python
>>> successful_count = '0'
>>> total_count = '10'
>>> exceptions = ['error1', 'error2']
>>> result = determine_overall_success(successful_count, total_count, exceptions)
False
```
