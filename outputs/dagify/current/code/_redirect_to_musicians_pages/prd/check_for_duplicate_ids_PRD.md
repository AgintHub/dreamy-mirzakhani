# check_for_duplicate_ids PRD

## Description
Checks if there are duplicate musician IDs in the given list of musician IDs.


## Conceptual Info

This shim function is designed to validate the uniqueness of musician IDs within a given list, ensuring data consistency before further processing.

## Docstring

### Summary
Checks for duplicate musician IDs in the provided list and returns a message indicating the presence or absence of duplicates.

### Parameters

- **musician_ids** (str): A list of musician IDs to be checked for duplicates, passed as a string representation of a list.

### Returns

str: A message indicating whether duplicates were found ('Duplicate IDs found') or not ('No duplicate IDs found').

### Raises

- ValueError: If the input is not a valid string representation of a list.
- TypeError: If the input is not a string.

### Examples

```python
>>> check_for_duplicate_ids(musician_ids='["id1", "id2", "id3"]')
'No duplicate IDs found'
```

```python
>>> check_for_duplicate_ids(musician_ids='["id1", "id2", "id1"]')
'Duplicate IDs found'
```
