# fetch_track_metadata PRD

## Description
Fetches metadata for a list of track IDs using a provided authentication token.


## Conceptual Info

This shim node is responsible for retrieving detailed metadata for a list of music tracks identified by their unique IDs. It uses an authentication token to authenticate the request.

## Docstring

### Summary
Fetches and returns track metadata for the given track IDs using the provided authentication token.

### Parameters

- **track_ids** (str): A comma-separated string of track identifiers for which metadata is to be fetched.
- **token** (str): An authentication token used to authorize the metadata fetch request.

### Returns

List[dict]: A list of dictionaries where each dictionary contains metadata for a track, including details such as title, artist, genre, and duration.

### Raises

- ValueError: If the track_ids string is empty or malformed.
- TypeError: If the input types are incorrect, such as track_ids not being a string or token not being a string.
- RuntimeError: If the metadata fetch operation fails due to network issues or authentication errors.

### Examples

```python
>>> track_ids = 'track1,track2,track3'
>>> token = 'auth_token_123'
>>> metadata = fetch_track_metadata(track_ids, token)
[{'id': 'track1', 'title': 'Song 1'}, {'id': 'track2', 'title': 'Song 2'}, {'id': 'track3', 'title': 'Song 3'}]
```

```python
>>> track_ids = ''
>>> token = 'auth_token_123'
>>> try: fetch_track_metadata(track_ids, token)
>>> except ValueError as e: print(e)
Track IDs cannot be empty.
```
