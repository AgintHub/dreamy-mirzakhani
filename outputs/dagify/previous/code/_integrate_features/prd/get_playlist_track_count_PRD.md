# get_playlist_track_count PRD

## Description
Returns the number of tracks included in a given playlist specified by a unique string input.


## Conceptual Info

This shim function abstracts the retrieval of the track count from a playlist, allowing other system components to query and utilize the number of tracks associated with a specific playlist without exposing underlying playlist structure or data source logic.

## Docstring

### Summary
Returns the total number of tracks in the playlist identified by the provided input string.

### Parameters

- **playlist_input** (str): A string representing the unique identifier or access information for the target playlist whose track count is to be determined.

### Returns

int: An integer representing the total number of tracks contained in the referenced playlist.

### Raises

- ValueError: Raised if the playlist_input is invalid, empty, or does not correspond to an existing playlist.
- TypeError: Raised if the playlist_input is not a string.

### Examples

```python
>>> get_playlist_track_count('abcd1234')
23
```

```python
>>> get_playlist_track_count('empty_playlist')
0
```
