# validate_objectives_input PRD

## Description
Validates the input objectives for selecting a jurisdiction, ensuring they are properly formatted and contain the required information.


## Conceptual Info

The validate_objectives_input shim plays a crucial role in the jurisdiction selection process by verifying that the provided objectives are valid and properly structured, which is essential for the subsequent steps in the process.

## Docstring

### Summary
Validate the input objectives to ensure they are correctly formatted and contain the necessary information for jurisdiction selection.

### Parameters

- **objectives** (str): A string representing the objectives input, which should be a list of bullet points summarizing the investment purpose, competitive advantages, target return profiles, and long-term vision.

### Returns

str: A string indicating the validation result, which can be either a success message or an error message detailing the issues with the objectives input.

### Raises

- ValueError: Raised when the objectives input is invalid, such as when it is not a list of bullet points or when it contains insufficient information.
- TypeError: Raised when the objectives input is not a string.

### Examples

```python
>>> validate_objectives_input(objectives="['Investment purpose', 'Competitive advantages', 'Target return profiles', 'Long-term vision']")
'Objectives input is valid.'
```

```python
>>> validate_objectives_input(objectives="Invalid input")
'Error: Objectives input must be a list of bullet points.'
```
