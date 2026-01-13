# validate_legal_entity_type PRD

## Description
Validates a given legal entity type and returns a standardized string representation.


## Conceptual Info

The validate_legal_entity_type shim function plays a crucial role in standardizing and validating legal entity types, ensuring consistency across the system.

## Docstring

### Summary
Validates a given legal entity type and returns a standardized string representation.

### Parameters

- **entity_type** (str): The input legal entity type to be validated (e.g., LP, LLC, SICAV)

### Returns

str: The validated legal entity type

### Raises

- ValueError: When the input entity type is not recognized or is invalid
- TypeError: When the input entity type is not a string

### Examples

```python
>>> validate_legal_entity_type(entity_type='LLC')
'LLC'
```

```python
>>> validate_legal_entity_type(entity_type=' invalid_type')
raises ValueError
```
