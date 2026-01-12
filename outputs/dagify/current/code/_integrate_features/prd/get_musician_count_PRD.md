# get_musician_count PRD

## Description
Calculates the total number of musicians based on the provided list of musician IDs.


## Conceptual Info

This shim function is designed to count the number of musicians given their IDs. It plays a crucial role in the integrate_features function by providing the total count of musicians involved in the identified tracks.

## Docstring

### Summary
Returns the count of musicians from the given list of musician IDs.

### Parameters

- **musician_ids** (str): A string representing a list of musician IDs.

### Returns

int: The total count of musicians.

### Raises

- ValueError: If the input string is not a valid representation of a list.
- TypeError: If the input is not a string.

### Examples

```python
>>> get_musician_count(musician_ids='["id1", "id2", "id3"]')
3
```

```python
>>> get_musician_count(musician_ids='[]')
0
```
