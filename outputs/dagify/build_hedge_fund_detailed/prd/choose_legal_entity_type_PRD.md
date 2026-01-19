# choose_legal_entity_type PRD

## Description
Define fund legal structure


## Conceptual Info

This node determines the most suitable legal entity for the hedge fund based on the previously selected jurisdiction, providing a concise justification.

## Docstring

### Summary
Selects an appropriate legal entity type for the fund and returns a one‑sentence explanation.

### Parameters

- **selected_jurisdiction** (str): The fund domicile chosen in the preceding node (e.g., "Cayman", "Delaware", "Luxembourg").

### Returns

dict: A dictionary with keys `legal_entity_type` (str) and `explanation` (str) describing the chosen entity.

### Raises

- ValueError: If `selected_jurisdiction` is not one of the supported jurisdictions.

### Examples

```python
>>> choose_legal_entity_type('Cayman')
{'legal_entity_type': 'LP', 'explanation': 'A Cayman Limited Partnership offers tax neutrality and flexibility for limited partners.'}
```

```python
>>> choose_legal_entity_type('Luxembourg')
{'legal_entity_type': 'SICAV', 'explanation': 'A Luxembourg SICAV provides an efficient structure for investment funds with a broad EU investor base.'}
```
