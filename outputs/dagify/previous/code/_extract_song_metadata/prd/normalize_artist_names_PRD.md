# normalize_artist_names PRD

## Description
Normalizes artist names by standardizing formatting and handling variations in artist name representations.


## Conceptual Info

This shim node is responsible for taking raw artist names from metadata and normalizing them into a consistent format. It handles variations in naming conventions, punctuation, and other discrepancies across different data sources.

## Docstring

### Summary
Normalizes artist names to achieve consistency across different metadata sources.

### Parameters

- **raw_artists** (str): The raw artist names that need to be normalized, potentially containing multiple artists separated by various delimiters.

### Returns

str: A string containing the normalized artist names, formatted consistently.

### Raises

- ValueError: If the input raw_artists is not a string or is empty.
- TypeError: If the input type is not str.

### Examples

```python
>>> normalize_artist_names(raw_artists='John Doe, Jane Doe')
'John Doe & Jane Doe'
```

```python
>>> normalize_artist_names(raw_artists='The Beatles, The Rolling Stones')
'The Beatles & The Rolling Stones'
```
