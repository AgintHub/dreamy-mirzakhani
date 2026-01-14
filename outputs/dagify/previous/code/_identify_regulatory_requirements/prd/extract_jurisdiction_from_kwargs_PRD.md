# extract_jurisdiction_from_kwargs PRD

## Description
Extracts the jurisdiction from the provided keyword arguments.


## Conceptual Info

This shim function is responsible for extracting the jurisdiction from a set of keyword arguments. It plays a crucial role in validating and processing legal entity information.

## Docstring

### Summary
Extracts the jurisdiction from the provided keyword arguments.

### Parameters

- **kwargs** (dict): A dictionary of keyword arguments containing the jurisdiction information.

### Returns

str: The extracted jurisdiction as a string.

### Raises

- ValueError: When the jurisdiction is not found in the keyword arguments.
- TypeError: When the input keyword arguments are not of type dict.

### Examples

```python
>>> extract_jurisdiction_from_kwargs(country='USA', state='California')
>>> extract_jurisdiction_from_kwargs(jurisdiction='New York')
'California, USA'
'New York'
```
