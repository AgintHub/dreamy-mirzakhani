# generate_musician_ids PRD

## Description
Generates unique identifiers for musicians based on their names.


## Conceptual Info

This shim generates unique identifiers for musicians based on their names, serving as a crucial step in organizing and referencing musician data within the larger system.

## Docstring

### Summary
Generates unique identifiers for musicians based on the provided names.

### Parameters

- **names** (str): A string containing musician names, likely comma-separated or in a specific format.

### Returns

List[str]: A list of unique identifiers corresponding to the input musician names.

### Raises

- ValueError: If the input string is empty or contains invalid characters.
- TypeError: If the input is not a string.

### Examples

```python
>>> generate_musician_ids(names='John Lennon,Paul McCartney')
['id1', 'id2']
```

```python
>>> generate_musician_ids(names='Michael Jackson')
['id3']
```
