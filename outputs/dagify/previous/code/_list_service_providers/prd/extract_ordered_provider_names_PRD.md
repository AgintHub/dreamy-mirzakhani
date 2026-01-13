# extract_ordered_provider_names PRD

## Description
This shim extracts the ordered list of provider names from a given provider mapping.


## Conceptual Info

The extract_ordered_provider_names shim is responsible for extracting a list of provider names in a specific order from a provider mapping, which is crucial for the list_service_providers function.

## Docstring

### Summary
Extracts the ordered list of provider names from a given provider mapping.

### Parameters

- **mapping** (dict): A dictionary containing the provider mapping.

### Returns

List[str]: A list of provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.

### Raises

- ValueError: If the provider mapping is invalid or missing required providers.
- TypeError: If the input provider mapping is not a dictionary.

### Examples

```python
>>> provider_mapping = {'prime_broker': 'Provider A', 'custodian': 'Provider B', 'fund_administrator': 'Provider C', 'legal_counsel': 'Provider D', 'compliance_consultant': 'Provider E'}
>>> ordered_providers = extract_ordered_provider_names(provider_mapping)
['Provider A', 'Provider B', 'Provider C', 'Provider D', 'Provider E']
```

```python
>>> invalid_mapping = 'invalid provider mapping'
>>> try:
...     extract_ordered_provider_names(invalid_mapping)
>>> except TypeError as e:
...     print(e)
Input provider mapping must be a dictionary.
```
