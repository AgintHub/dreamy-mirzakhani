# validate_bullet_constraints PRD

## Description
Validates a list of bullet points against a maximum count constraint.


## Conceptual Info

The validate_bullet_constraints shim ensures that a list of bullet points conforms to a specified maximum count constraint, providing a validated output list.

## Docstring

### Summary
Validates a list of bullet points against a maximum count constraint.

### Parameters

- **bullets** (str): Input list of bullet points as a string
- **max_count** (str): Maximum allowed count of bullet points as a string

### Returns

List[str]: Validated list of bullet points

### Raises

- ValueError: When the input list exceeds the maximum allowed count
- TypeError: When input types are incorrect

### Examples

```python
>>> validate_bullet_constraints(bullets='a\nb\nc', max_count='2')
['a', 'b']
```

```python
>>> validate_bullet_constraints(bullets='a\nb\nc\nd', max_count='5')
['a', 'b', 'c', 'd']
```
