# fetch_sampled_songs_metadata PRD

## Description
Retrieves metadata for a sampled set of songs based on expanded musician data, returning a list of song metadata dictionaries.


## Conceptual Info

This shim serves as the bridge between musician data expansion and the downstream playlist creation pipeline by providing a curated set of song metadata that can be used for feature extraction and recommendation scoring.

## Docstring

### Summary
Fetch sampled songs metadata from an external service or database based on the provided expanded musician data.

### Parameters

- **musician_data** (str): JSON string representing a dictionary with keys 'musician_ids', 'musician_names', and 'aliases', used to sample songs.

### Returns

str: A JSON string that can be parsed into a List[dict] where each dictionary contains metadata fields such as 'song_id', 'title', 'artist_id', 'genre', and 'duration'.

### Raises

- ValueError: If the input JSON does not contain required keys or has malformed structure.
- TypeError: If the input parameter is not a string.
- RuntimeError: If the external service fails to return data or returns an unexpected format.

### Examples

```python
>>> musician_data = '{"musician_ids":["id1"],"musician_names":["Artist"],"aliases":[["Alias1"]]}'
>>> result = fetch_sampled_songs_metadata(musician_data=musician_data)
>>> print(result)
[{"song_id": "s1", "title": "Song One", "artist_id": "id1", "genre": "Pop", "duration": 210}, {"song_id": "s2", "title": "Song Two", "artist_id": "id1", "genre": "Pop", "duration": 195}]
```

```python
>>> musician_data = '{"musician_ids":["id2"],"musician_names":["Band"],"aliases":[["BandAlias"]]}'
>>> result = fetch_sampled_songs_metadata(musician_data=musician_data)
>>> print(result)
[{"song_id": "s3", "title": "Track Three", "artist_id": "id2", "genre": "Rock", "duration": 240}]
```
