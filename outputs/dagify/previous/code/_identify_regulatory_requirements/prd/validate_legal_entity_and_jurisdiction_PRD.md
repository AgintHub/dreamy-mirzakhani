# validate_legal_entity_and_jurisdiction PRD

## Description
Validates a legal entity type against a jurisdiction and returns a dictionary of normalized entity information.


## Conceptual Info

This shim abstracts the validation logic for legal entity types across jurisdictions, ensuring downstream modules receive consistent, normalized data.

## Docstring

### Summary
Validate a legal entity type against a jurisdiction and return normalized entity information.

### Parameters

- **entity_type** (str): The raw legal entity type provided by the user (e.g., 'lp', 'LLC', 'SICAV').
- **jurisdiction** (str): The jurisdiction code or name where the entity will operate (e.g., 'US', 'DE', 'FR').

### Returns

str: A JSON-formatted string containing `legal_entity_type` and `jurisdiction` keys with normalized values.

### Raises

- ValueError: If the entity type is not supported in the specified jurisdiction.
- TypeError: If either `entity_type` or `jurisdiction` is not a string.

### Examples

```python
>>> result = validate_legal_entity_and_jurisdiction(entity_type='LLC', jurisdiction='US')
>>> print(result)
"{\"legal_entity_type\": \"LLC\", \"jurisdiction\": \"US\"}"
```

```python
>>> try:
...     validate_legal_entity_and_jurisdiction(entity_type='XYZ', jurisdiction='US')
>>> except ValueError as e:
...     print(e)
"Entity type 'XYZ' is not supported in jurisdiction 'US'."
```
