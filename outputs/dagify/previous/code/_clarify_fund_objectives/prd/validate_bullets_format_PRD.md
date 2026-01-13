# validate_bullets_format PRD

## Description
Validates the format of bullet points to ensure they meet the required criteria, returning a list of formatted bullet points.


## Conceptual Info

This shim function is responsible for validating the format of bullet points, ensuring they meet the required criteria, and returning a list of formatted bullet points.

## Docstring

### Summary
Validates the format of bullet points and returns a list of formatted bullet points.

### Parameters

- **bullets** (List[str]): A list of bullet points to be validated.
- **max_count** (int): The maximum number of allowed bullet points.

### Returns

List[str]: A list of formatted bullet points.

### Raises

- ValueError: When the number of bullet points exceeds the maximum allowed count.
- TypeError: When the input parameters are of incorrect type.

### Examples

```python
>>> bullets = ['point1', 'point2', 'point3']
>>> max_count = 3
>>> validated_bullets = validate_bullets_format(bullets, max_count)
['point1', 'point2', 'point3']
```

```python
>>> bullets = ['point1', 'point2', 'point3', 'point4']
>>> max_count = 3
>>> validated_bullets = validate_bullets_format(bullets, max_count)
ValueError: Number of bullet points exceeds the maximum allowed count.
```
