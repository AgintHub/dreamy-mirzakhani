# fetch_musicbrainz_metadata PRD

## Description
Fetches MusicBrainz metadata for a given track ID, artist name, and track title, returning the result as a JSON string.


## Conceptual Info

The shim retrieves structured metadata from MusicBrainz, enabling downstream nodes to enrich song information.

## Docstring

### Summary
Retrieve MusicBrainz metadata for a track.

### Parameters

- **track_id** (str): Unique identifier for the track in MusicBrainz.
- **artist** (str): Name of the artist performing the track.
- **title** (str): Title of the track.

### Returns

str: A JSON-formatted string containing the retrieved MusicBrainz metadata.

### Raises

- ValueError: If any required parameter is missing or empty.
- TypeError: If a parameter is not of type str.

### Examples

```python
>>> metadata = fetch_musicbrainz_metadata(track_id='12345', artist='The Beatles', title='Hey Jude')
{"artist": "The Beatles", "title": "Hey Jude", "release_date": "1968-08-26", "genres": ["Rock"]}
```

```python
>>> metadata = fetch_musicbrainz_metadata(track_id='99999', artist='Unknown Artist', title='Unknown Song')
{}
```
