# validate_objectives_bullets PRD

## Description
Validates the input objectives bullets to ensure they meet the required criteria.


## Conceptual Info

The validate_objectives_bullets shim is responsible for verifying that the input objectives bullets meet the required criteria, including checking for completeness, format, and content.

## Docstring

### Summary
Validates the input objectives bullets to ensure they meet the required criteria.

### Parameters

- **objectives_bullets** (str): Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets).

### Returns

str: Output message indicating the validation result.

### Raises

- ValueError: When the input objectives bullets are incomplete, poorly formatted, or exceed the maximum allowed number of bullets.
- TypeError: When the input objectives bullets are not a string.

### Examples

```python
>>> validate_objectives_bullets(objectives_bullets='This is a valid bullet point.')
'Validation successful.'
```

```python
>>> validate_objectives_bullets(objectives_bullets='This is an invalid bullet point with too much information. This is another invalid bullet point.')
'Validation failed: exceeded maximum allowed number of bullets or invalid format.'
```
