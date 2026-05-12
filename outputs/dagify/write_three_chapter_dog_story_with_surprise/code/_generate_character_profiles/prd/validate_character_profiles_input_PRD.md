# validate_character_profiles_input PRD

## Description
This shim function validates the structure and integrity of character profile data extracted from input text.


## Conceptual Info

This shim function checks the correctness, completeness, and consistency of character profile data before further processing in the story generation pipeline.

## Docstring

### Summary
Validate the structure and content of character profile data extracted from input, raising errors if validation fails.

### Parameters

- **character_profiles** (str): A JSON string representing a list of character profile dictionaries extracted from user input.

### Returns

str: A success message if validation passes, or raises an error if validation fails.

### Raises

- ValueError: Raised when validation detects missing required fields or inconsistent data in character profiles.
- TypeError: Raised when character_profiles is not a correctly formatted JSON string or contains data of unexpected types.

### Examples

```python
>>> validate_character_profiles_input(character_profiles='[{"name": "Alice", "age": 30}]')
'Validation successful: character profiles are valid.'
```

```python
>>> validate_character_profiles_input(character_profiles='[{"name": 123, "age": "unknown"}]')
ValueError: Invalid data types in character profiles.
```
