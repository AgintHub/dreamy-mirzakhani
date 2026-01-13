# validate_entity_type PRD

## Description
Validates the given entity type to ensure it meets the required criteria.


## Conceptual Info

The validate_entity_type shim function is responsible for verifying that a given entity type is valid and meets the necessary requirements. It plays a crucial role in ensuring data consistency and accuracy within the system.

## Docstring

### Summary
Validates the given entity type to ensure it meets the required criteria.

### Parameters

- **entity_type** (str): The entity type to be validated (e.g., LP, LLC, SICAV)

### Returns

str: Validation result or an error message

### Raises

- ValueError: When the input entity type is invalid or does not meet the required criteria.
- TypeError: When the input entity type is not a string.

### Examples

```python
>>> validate_entity_type(entity_type='LLC')
'Validation successful'
```

```python
>>> validate_entity_type(entity_type='InvalidType')
'Validation failed: Invalid entity type'
```
