# deduplicate_artist_list PRD

## Description
Removes duplicate artist names from a given list while preserving the original order.


## Conceptual Info

This shim function is designed to remove duplicate artist names from a list, ensuring that the original order of artists is maintained. It plays a crucial role in data preprocessing for music metadata analysis.

## Docstring

### Summary
Deduplicates a list of artist names while preserving their original order.

### Parameters

- **names** (LIST_STR): A list of artist names that may contain duplicates.

### Returns

LIST_STR: A list of artist names with duplicates removed, maintaining the original order.

### Raises

- TypeError: If the input 'names' is not a list or if the list contains non-string elements.
- ValueError: If the input list is empty or contains only whitespace strings.

### Examples

```python
>>> deduplicate_artist_list(names=['John Doe', 'Jane Doe', 'John Doe'])
['John Doe', 'Jane Doe']
```

```python
>>> deduplicate_artist_list(names=['Artist1', 'Artist2', 'Artist1', 'Artist3'])
['Artist1', 'Artist2', 'Artist3']
```
