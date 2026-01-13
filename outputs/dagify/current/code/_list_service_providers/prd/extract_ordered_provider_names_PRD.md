# extract_ordered_provider_names PRD

## Description
Return a list of mandatory external service provider names in the required order based on an entity‑specific provider mapping.


## Conceptual Info

The shim transforms a provider mapping dictionary into a deterministic, ordered list of provider names required for downstream validation and processing.

## Docstring

### Summary
Extracts the ordered list of mandatory external service provider names from a provider mapping dictionary.

### Parameters

- **mapping** (dict): A dictionary where keys are provider identifiers and values are provider details. The dictionary must contain entries for each of the five mandatory providers: 'prime_broker', 'custodian', 'fund_administrator', 'legal_counsel', and 'compliance_consultant'.

### Returns

List[str]: A list of provider names in the exact order: ['prime broker', 'custodian', 'fund administrator', 'legal counsel', 'compliance consultant'].

### Raises

- ValueError: If any of the required provider keys are missing from the mapping.
- TypeError: If the input mapping is not a dictionary or contains non‑string values.

### Examples

```python
>>> sample_mapping = {
...     'prime_broker': {'name': 'PrimeX'},
...     'custodian': {'name': 'CustodialY'},
...     'fund_administrator': {'name': 'AdminZ'},
...     'legal_counsel': {'name': 'LegalA'},
...     'compliance_consultant': {'name': 'ComplianceB'}
>>> }
[\n    'prime broker',\n    'custodian',\n    'fund administrator',\n    'legal counsel',\n    'compliance consultant'\n]
```

```python
>>> incomplete_mapping = {
...     'prime_broker': {'name': 'PrimeX'},
...     'custodian': {'name': 'CustodialY'}
>>> }
ValueError: Missing required provider keys: fund_administrator, legal_counsel, compliance_consultant
```
