# validate_legal_entity_type PRD

## Description
Validates that the provided legal entity type is supported and returns a confirmation string.


## Conceptual Info

This shim ensures that downstream nodes receive a verified legal entity type, preventing propagation of invalid values through the governance structure pipeline.

## Docstring

### Summary
Validate the supplied legal entity type against an internal list of supported types and return a confirmation string.

### Parameters

- **entity_type** (str): The legal entity type to validate (e.g., 'LP', 'LLC', 'SICAV').

### Returns

str: A confirmation string such as "Entity type 'LLC' validated."

### Raises

- ValueError: If the entity_type is not in the list of supported legal entity types.
- TypeError: If entity_type is not a string.

### Examples

```python
>>> validate_legal_entity_type('LLC')
"Entity type 'LLC' validated."
```

```python
>>> validate_legal_entity_type('Unknown')
ValueError: Unsupported entity type 'Unknown'.
```
