# extract_agency_citation PRD

## Description
Extracts the agency citation from a given regulatory mapping.


## Conceptual Info

The extract_agency_citation shim function is responsible for extracting the agency citation from a given regulatory mapping. This function plays a crucial role in identifying regulatory requirements and providing the necessary citation for compliance.

## Docstring

### Summary
Extracts the agency citation from a given regulatory mapping.

### Parameters

- **mapping** (str): The input regulatory mapping.

### Returns

str: The extracted agency citation.

### Raises

- ValueError: When the input mapping is invalid or empty.
- TypeError: When the input mapping is not a string.

### Examples

```python
>>> extract_agency_citation(mapping={'agency_citation': 'Example Citation'})
'Example Citation'
```

```python
>>> extract_agency_citation(mapping={})
''
```
