# get_provider_mapping_for_entity PRD

## Description
This shim function retrieves a dictionary mapping of service providers for a given legal entity type.


## Conceptual Info

The get_provider_mapping_for_entity shim function acts as an interface to retrieve service provider mappings for different legal entity types, playing a crucial role in the system's operational workflow.

## Docstring

### Summary
This function takes a legal entity type as input and returns a dictionary mapping of service providers, including their core functions, specific to the given entity type.

### Parameters

- **entity_type** (str): The legal entity type for which the service provider mapping is required, e.g., 'LP', 'LLC', 'SICAV'.

### Returns

dict: A dictionary containing service provider names as keys and their respective core functions as values, specific to the given legal entity type.

### Raises

- ValueError: If the input entity type is not recognized or supported.
- TypeError: If the input entity type is not a string.

### Examples

```python
>>> provider_mapping = get_provider_mapping_for_entity(entity_type='LP')
>>> print(provider_mapping)
{'Prime Broker': 'Custody and Trading', 'Custodian': 'Asset Safekeeping', 'Fund Administrator': 'Accounting and Compliance'}
```

```python
>>> provider_mapping = get_provider_mapping_for_entity(entity_type='LLC')
>>> print(provider_mapping)
{'Legal Counsel': 'Regulatory Compliance', 'Compliance Consultant': 'Risk Management', 'Fund Administrator': 'Accounting and Tax'}
```
