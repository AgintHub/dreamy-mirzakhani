# choose_legal_entity_type PRD

## Description
Determine appropriate legal structure


## Conceptual Info

This node determines the most suitable legal entity type for a hedge fund based on the selected jurisdiction.

## Docstring

### Summary
Choose a legal entity type based on the selected jurisdiction and provide operational advantages and compliance considerations.

### Parameters

- **jurisdiction** (str): The selected jurisdiction (e.g., Cayman Islands, Delaware, Luxembourg)

### Returns

dict: A dictionary containing the chosen legal entity type, operational advantages, and compliance consideration.

### Raises

- ValueError: If the selected jurisdiction is not supported.

### Examples

```python
>>> choose_legal_entity_type('Cayman Islands')
>>> # Output: {'legal_entity_type': 'LP', 'operational_advantages': ['Tax efficiency', 'Flexibility in ownership structure', 'Limited liability protection'], 'compliance_consideration': 'Registration with the Cayman Islands Monetary Authority'}
{'legal_entity_type': 'LP', 'operational_advantages': ['Tax efficiency', 'Flexibility in ownership structure', 'Limited liability protection'], 'compliance_consideration': 'Registration with the Cayman Islands Monetary Authority'}
```
