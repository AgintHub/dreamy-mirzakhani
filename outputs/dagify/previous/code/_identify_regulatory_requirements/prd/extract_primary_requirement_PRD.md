# extract_primary_requirement PRD

## Description
Extracts the primary regulatory requirement from a given regulatory mapping.


## Conceptual Info

The extract_primary_requirement shim function plays a crucial role in identifying the primary regulatory requirement from a given regulatory mapping. This function is essential in determining the specific regulatory filing or registration required.

## Docstring

### Summary
Extracts the primary regulatory requirement from a given regulatory mapping.

### Parameters

- **mapping** (str): The regulatory mapping from which to extract the primary requirement.

### Returns

str: The primary regulatory requirement.

### Raises

- ValueError: When the input mapping is invalid or empty.
- TypeError: When the input mapping is not a string.

### Examples

```python
>>> regulatory_mapping = {'primary_requirement': 'File Form 10-K with the SEC', 'agency_citation': 'SEC'}
>>> extract_primary_requirement(mapping=regulatory_mapping)
'File Form 10-K with the SEC'
```

```python
>>> regulatory_mapping = {}
>>> extract_primary_requirement(mapping=regulatory_mapping)
''
```
