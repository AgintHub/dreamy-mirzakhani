# expand_musician_aliases PRD

## Description
Expands musician data by combining IDs, names, and alias lists into a dictionary mapping each musician ID to its name and aliases.


## Conceptual Info

This shim serves as a data normalization step, aligning raw musician identifiers, names, and alias metadata into a unified structure required by downstream playlist generation and recommendation modules.

## Docstring

### Summary
Combines lists of musician IDs, names, and aliases into a single dictionary mapping each ID to its name and list of aliases.

### Parameters

- **musician_ids** (str): JSON-encoded list of unique musician identifiers.
- **musician_names** (str): JSON-encoded list of musician names corresponding to the IDs.
- **aliases** (str): JSON-encoded list where each element is a list of aliases for the corresponding musician.

### Returns

str: A JSON string representing a dictionary where each key is a musician ID and the value is a dictionary with keys 'name' (str) and 'aliases' (list of str).

### Raises

- ValueError: If the three input lists are not of the same length.
- TypeError: If any input string cannot be parsed as a JSON list.

### Examples

```python
>>> musician_ids = '["m1", "m2"]'
>>> musician_names = '["Artist One", "Artist Two"]'
>>> aliases = '["[A", "A1"]", ["B", "B1", "B2"]]'
>>> output = expand_musician_aliases(musician_ids, musician_names, aliases)
{"m1": {"name": "Artist One", "aliases": ["A", "A1"]}, "m2": {"name": "Artist Two", "aliases": ["B", "B1", "B2"]}}
```

```python
>>> expand_musician_aliases('[]', '[]', '[]')
{}
```
