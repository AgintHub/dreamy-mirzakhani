# fetch_spotify_metadata PRD

## Description
Fetches metadata for a given track from Spotify based on track ID, artist, and title.


## Conceptual Info

This shim is responsible for retrieving metadata for a specific track from Spotify using the track ID, artist name, and track title. The retrieved metadata is crucial for further processing and merging with data from other sources.

## Docstring

### Summary
Fetches and returns Spotify metadata for a given track based on its ID, artist, and title.

### Parameters

- **track_id** (str): Unique identifier for the track.
- **artist** (str): Name of the artist associated with the track.
- **title** (str): Title of the track.

### Returns

str: A JSON-formatted string containing the Spotify metadata for the track.

### Raises

- ValueError: If the input parameters (track_id, artist, title) are invalid or missing.
- TypeError: If the input parameters are of incorrect type.
- Exception: If there's an issue with the Spotify API request or response parsing.

### Examples

```python
>>> fetch_spotify_metadata(track_id='12345', artist='Example Artist', title='Example Track')
{'album': {'name': 'Example Album'}, 'artists': [{'name': 'Example Artist'}], 'name': 'Example Track'}
```

```python
>>> fetch_spotify_metadata(track_id='67890', artist='Another Artist', title='Another Track')
{'album': {'name': 'Another Album'}, 'artists': [{'name': 'Another Artist'}], 'name': 'Another Track'}
```
