# validate_prompt_text PRD

## Description
Validates the input prompt text to ensure it meets the required criteria.


## Conceptual Info

The validate_prompt_text shim function is responsible for validating the input prompt text to ensure it meets the required criteria, which is essential for generating accurate and relevant output.

## Docstring

### Summary
Validates the input prompt text to ensure it meets the required criteria.

### Parameters

- **prompt_text** (str): The input prompt text to be validated.

### Returns

str: The validated prompt text.

### Raises

- ValueError: When the input prompt text is empty or too long.
- TypeError: When the input prompt text is not a string.

### Examples

```python
>>> validate_prompt_text(prompt_text='This is a valid prompt.')
'This is a valid prompt.'
```

```python
>>> validate_prompt_text(prompt_text='')
''
```
