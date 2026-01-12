# get_identified_tracks_count PRD

## Description
Returns the number of tracks identified from a sample identification result dictionary.


## Conceptual Info

This shim extracts and returns the count of identified tracks from a sample identification process's result data, enabling downstream components to react to successful or failed identification attempts.

## Docstring

### Summary
Extracts the number of tracks identified from a sample identification result dictionary.

### Parameters

- **result** (str): A JSON-encoded string representation of the sample identification result; must contain an identifiable 'tracks' field that is a list or object with countable entries.

### Returns

int: An integer representing the number of identified tracks found in the input result.

### Raises

- ValueError: If the input string cannot be parsed as JSON or lacks a valid 'tracks' field.
- TypeError: If the 'result' parameter is not a string or if the parsed value of 'tracks' is not countable.

### Examples

```python
>>> result = '{"tracks": ["trackA", "trackB", "trackC"]}'
>>> get_identified_tracks_count(result)
3
```

```python
>>> result = '{"tracks": []}'
>>> get_identified_tracks_count(result)
0
```
