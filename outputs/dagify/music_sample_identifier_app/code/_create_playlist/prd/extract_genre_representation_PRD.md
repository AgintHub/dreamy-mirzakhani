# extract_genre_representation PRD

## Description
Extracts a list of genres represented in a playlist based on the provided track identifiers.


## Conceptual Info

This shim function plays a crucial role in the playlist generation pipeline by determining the genre representation of the created playlist based on the selected track IDs.

## Docstring

### Summary
Extracts a list of genres represented in a playlist based on the track identifiers provided as input.

### Parameters

- **track_ids** (str): A string containing the track identifiers, expected to be a list or comma-separated values.

### Returns

List[str]: A list of unique genre names represented in the playlist.

### Raises

- ValueError: If the input track_ids is not a valid string or cannot be processed.
- TypeError: If the input type is not a string.

### Examples

```python
>>> extract_genre_representation(track_ids='track1,track2,track3')
['pop', 'rock', 'electronic']
```

```python
>>> extract_genre_representation(track_ids='track4')
['hip-hop']
```
