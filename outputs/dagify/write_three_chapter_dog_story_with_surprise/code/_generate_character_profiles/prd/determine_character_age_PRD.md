# determine_character_age PRD

## Description
Determine the age of a character given their data.


## Conceptual Info

This shim functions calculates the age of a character based on provided data, ensuring accuracy and consistency.

## Docstring

### Summary
Determine the age of a character given their data.

### Parameters

- **character_data** (dict): A dictionary containing the character's data, including birthdate, for accurate age calculation.

### Returns

float: The calculated age of the character

### Raises

- ValueError: When invalid or missing data is provided, or when date calculations fail.
- TypeError: When the input data is of an incorrect type, causing calculation errors.

### Examples

```python
>>> character_data = {'birthdate': '1990-01-01'}
>>> character_age = determine_character_age(character_data)
30
```

```python
>>> character_data = {'birthdate': '1980-01-01'}
>>> character_age = determine_character_age(character_data)
42
```
