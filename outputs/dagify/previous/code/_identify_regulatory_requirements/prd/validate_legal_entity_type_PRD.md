# validate_legal_entity_type PRD

## Description
Validates a given legal entity type to ensure it meets specific criteria.


## Conceptual Info

The validate_legal_entity_type shim function plays a crucial role in ensuring that the provided legal entity type is valid and recognized within the system. This function is essential for maintaining data consistency and accuracy.

## Docstring

### Summary
Validates a given legal entity type to ensure it meets specific criteria.

### Parameters

- **entity_type** (str): The legal entity type to be validated (e.g., LP, LLC, SICAV).

### Returns

str: The validated legal entity type.

### Raises

- ValueError: When the input entity type is not recognized or does not meet the required criteria.
- TypeError: When the input entity type is not a string.

### Examples

```python
>>> validate_legal_entity_type(entity_type='LLC')
'LLC'
```

```python
>>> validate_legal_entity_type(entity_type='Invalid Entity Type')
raises ValueError
```
