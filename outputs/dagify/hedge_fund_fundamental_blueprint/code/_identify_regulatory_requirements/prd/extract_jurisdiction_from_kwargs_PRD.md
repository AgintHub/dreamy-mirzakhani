# extract_jurisdiction_from_kwargs PRD

## Description
Extracts the jurisdiction value from keyword arguments passed to regulatory requirement functions.


## Conceptual Info

In the regulatory requirement workflow, the jurisdiction is supplied via keyword arguments; this shim standardizes retrieval of that value and validates its presence before further processing.

## Docstring

### Summary
Retrieve the jurisdiction string from a set of keyword arguments used in regulatory requirement functions.

### Parameters

- **kwargs** (dict): A mapping of keyword arguments that should include a key named 'jurisdiction' holding a string value.

### Returns

str: The jurisdiction name extracted from `kwargs`.

### Raises

- ValueError: Raised when the 'jurisdiction' key is missing from `kwargs` or its value is empty.
- TypeError: Raised when the value associated with the 'jurisdiction' key is not a string.

### Examples

```python
>>> result = extract_jurisdiction_from_kwargs(jurisdiction="France")
>>> print(result)
"France"
```

```python
>>> try:
...     extract_jurisdiction_from_kwargs(country="Italy")
>>> except ValueError as e:
...     print(e)
"Missing 'jurisdiction' key in keyword arguments."
```
