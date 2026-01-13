# extract_provider_functions PRD

## Description
Returns a list of core function descriptions for a given ordered list of service provider names based on a provider mapping dictionary.


## Conceptual Info

The shim translates a mapping of provider names to their function descriptions into an ordered list of functions that match the ordering of provider names supplied by the caller. This facilitates validation of provider completeness and integration with downstream nodes that consume structured provider information.

## Docstring

### Summary
Retrieve ordered provider functions from a mapping.

### Parameters

- **mapping** (str): A JSON-serialised dictionary where keys are provider names and values are strings describing their core functions.
- **providers** (str): A JSON-serialised list of provider names in the desired order. The function will return a list of corresponding function descriptions.

### Returns

str: A JSON-serialised list of function descriptions corresponding to the input providers list.

### Raises

- ValueError: Raised if a provider name in `providers` is missing from `mapping`.
- TypeError: Raised if either `mapping` or `providers` is not a valid JSON string or does not represent a dictionary/list respectively.

### Examples

```python
>>> import json
>>> mapping = json.dumps({"prime broker": "Execute trades", "custodian": "Safeguard assets"})
>>> providers = json.dumps(["prime broker", "custodian"])
>>> result = extract_provider_functions(mapping, providers)
>>> print(json.loads(result))
["Execute trades", "Safeguard assets"]
```

```python
>>> mapping = json.dumps({"prime broker": "Execute trades"})
>>> providers = json.dumps(["prime broker", "custodian"])
>>> extract_provider_functions(mapping, providers)
ValueError: Provider 'custodian' not found in mapping.
```
