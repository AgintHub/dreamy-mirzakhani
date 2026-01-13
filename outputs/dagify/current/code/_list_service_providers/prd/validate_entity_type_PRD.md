# validate_entity_type PRD

## Description
Validates the given entity type to ensure it meets specific requirements.


## Conceptual Info

The validate_entity_type shim function plays a crucial role in ensuring that the provided entity type is valid and consistent with the system's requirements. It acts as a gatekeeper, preventing invalid or unsupported entity types from being processed further.

## Docstring

### Summary
Validates the given entity type to ensure it meets specific requirements.

### Parameters

- **entity_type** (str): The entity type to be validated (e.g., LP, LLC, SICAV)

### Returns

str: Validation result or an error message

### Raises

- ValueError: When the input entity type is invalid or unsupported
- TypeError: When the input entity type is not a string

### Examples

```python
>>> validate_entity_type(entity_type='LLC')
'LLC' is a valid entity type
```

```python
>>> validate_entity_type(entity_type='InvalidType')
'InvalidType' is not a supported entity type
```
