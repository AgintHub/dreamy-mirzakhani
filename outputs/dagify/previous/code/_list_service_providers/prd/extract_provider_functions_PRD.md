# extract_provider_functions PRD

## Description
Retrieves a list of provider function descriptions matching the order of provider names from a mapping dictionary.


## Conceptual Info

The shim fetches the functional descriptions of external service providers from a mapping, ensuring the order aligns with the provider list to support downstream validation and reporting.

## Docstring

### Summary
Return a list of provider function descriptions that correspond to the supplied provider names, preserving order.

### Parameters

- **mapping** (dict): Dictionary mapping provider names to their function descriptions. Keys are provider names; values are strings describing the provider’s core functions.
- **provider_names** (list[str]): Ordered list of provider names for which function descriptions are required.

### Returns

list[str]: A list of function description strings, each matching the provider name at the same index in provider_names.

### Raises

- KeyError: If a provider name in provider_names is not present in the mapping dictionary.
- ValueError: If the mapping values are not strings or if provider_names is empty.

### Examples

```python
>>> mapping = {
...     'prime broker': 'Execute trades and manage securities',
...     'custodian': 'Safeguard assets and provide custody services',
...     'fund administrator': 'Handle accounting and investor reporting',
...     'legal counsel': 'Provide legal advice and compliance oversight',
...     'compliance consultant': 'Ensure regulatory compliance and risk management'}
>>> provider_names = ['prime broker', 'custodian', 'fund administrator', 'legal counsel', 'compliance consultant']
>>> functions = extract_provider_functions(mapping, provider_names)
['Execute trades and manage securities', 'Safeguard assets and provide custody services', 'Handle accounting and investor reporting', 'Provide legal advice and compliance oversight', 'Ensure regulatory compliance and risk management']
```

```python
>>> mapping = {'prime broker': 'Execute trades'}
>>> extract_provider_functions(mapping, ['custodian'])
KeyError: 'custodian'
```
