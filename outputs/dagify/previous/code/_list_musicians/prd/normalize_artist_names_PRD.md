# normalize_artist_names PRD

## Description
Normalizes a list of artist names by standardizing their format and correcting minor variations in spelling or punctuation.


## Conceptual Info

This node takes a list of artist names, potentially containing variations in spelling, punctuation, or format, and normalizes them to a standard format.

## Docstring

### Summary
Normalizes a list of artist names to a standard format.

### Parameters

- **names** (LIST_STR): A list of artist names that may contain variations in spelling, punctuation, or format.

### Returns

LIST_STR: A list of artist names normalized to a standard format.

### Raises

- TypeError: If the input 'names' is not a list of strings.
- ValueError: If the input list is empty or contains non-string values.

### Examples

```python
>>> normalize_artist_names(names=['John Doe', 'Jane Smith'])
['John Doe', 'Jane Smith']
```

```python
>>> normalize_artist_names(names=['J Doe', 'Jane S.'])
['John Doe', 'Jane Smith']
```
