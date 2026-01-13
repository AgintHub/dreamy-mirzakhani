# extract_key_disadvantages PRD

## Description
Extracts key disadvantages from a given jurisdiction data.


## Conceptual Info

The extract_key_disadvantages shim function is used to extract key disadvantages from a given jurisdiction data. This function plays a crucial role in evaluating the pros and cons of a jurisdiction for a fund.

## Docstring

### Summary
Extracts key disadvantages from a given jurisdiction data.

### Parameters

- **jurisdiction_data** (str): The jurisdiction data to extract disadvantages from.
- **count** (str): The number of disadvantages to extract.

### Returns

List[str]: A list of key disadvantages of the given jurisdiction.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> extract_key_disadvantages(jurisdiction_data='{"name": "Singapore", "disadvantages": ["high taxes", "complex regulations"]}', count='2')
['high taxes', 'complex regulations']
```

```python
>>> extract_key_disadvantages(jurisdiction_data='{"name": "Cayman Islands", "disadvantages": ["limited investor protection", "reputation risks"]}', count='1')
['limited investor protection']
```
