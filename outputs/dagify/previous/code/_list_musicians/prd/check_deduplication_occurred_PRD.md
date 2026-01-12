# check_deduplication_occurred PRD

## Description
Checks if deduplication occurred between the original and deduplicated lists of artist names.


## Conceptual Info

This shim function compares the original list of artist names with the deduplicated list to determine if any deduplication occurred.

## Docstring

### Summary
Compares original and deduplicated lists of artist names to check if deduplication occurred.

### Parameters

- **original** (str): The original list of artist names before deduplication.
- **deduplicated** (str): The list of artist names after deduplication.

### Returns

bool: True if deduplication occurred, False otherwise.

### Raises

- TypeError: If either 'original' or 'deduplicated' is not of type str.
- ValueError: If the input strings are not valid representations of lists.

### Examples

```python
>>> check_deduplication_occurred(original='["Artist1", "Artist2", "Artist1"]', deduplicated='["Artist1", "Artist2"]')
>>> # Expected output: True
True
```

```python
>>> check_deduplication_occurred(original='["Artist1", "Artist2"]', deduplicated='["Artist1", "Artist2"]')
>>> # Expected output: False
False
```
