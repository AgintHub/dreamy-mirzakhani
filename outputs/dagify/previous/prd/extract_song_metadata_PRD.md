# extract_song_metadata PRD

## Description
Extracts comprehensive metadata for the identified sampled songs, leveraging advanced audio analysis and metadata retrieval techniques.


## Conceptual Info

The extract_song_metadata node enriches the candidate tracks identified by identify_sampled_songs with detailed, structured metadata. It combines audio feature extraction, external music‑database lookups, and data validation to produce a consistent set of attributes (title, artists, album, release date, genre, tempo, key, loudness) for each sampled song, enabling downstream processes such as playlist creation, musician deduplication, and UI display.

## Docstring

### Summary
Extracts detailed metadata for each sampled song candidate.

### Parameters

- **candidate_tracks** (List[dict]): List of candidate track objects returned by identify_sampled_songs. Each object must contain at least 'track_id', 'confidence', 'start_time', 'end_time', and 'metadata' (which includes 'artist_name', 'track_title', 'release_date').

### Returns

List[dict]: A list of metadata dictionaries, each containing the fields: song_title (str), artist_names (List[str]), album_info (str), release_date (str), genre_classifications (List[str]), tempo (float), key (str), loudness (float).

### Raises

- ValueError: If candidate_tracks is empty or missing required fields.
- RuntimeError: If external API calls (Discogs, MusicBrainz, Spotify) fail or return inconsistent data.

### Examples

```python
>>> candidate_tracks = [{
...   'track_id': '12345',
...   'confidence': 0.92,
...   'start_time': 12.3,
...   'end_time': 45.6,
...   'metadata': {
...     'artist_name': 'The Sample Artists',
...     'track_title': 'Sample Tune',
...     'release_date': '2020-07-15'
...   }
>>> }
[{\n  'song_title': 'Sample Tune',\n  'artist_names': ['The Sample Artists'],\n  'album_info': 'Unknown Album',\n  'release_date': '2020-07-15',\n  'genre_classifications': ['Electronic', 'House'],\n  'tempo': 128.0,\n  'key': 'C minor',\n  'loudness': -5.2\n}]
```

```python
>>> candidate_tracks = [{
...   'track_id': '67890',
...   'confidence': 0.85,
...   'start_time': 0.0,
...   'end_time': 30.0,
...   'metadata': {
...     'artist_name': 'Another Artist',
...     'track_title': 'Another Sample',
...     'release_date': '2018-03-22'
...   }
>>> }
[{\n  'song_title': 'Another Sample',\n  'artist_names': ['Another Artist'],\n  'album_info': 'Unknown Album',\n  'release_date': '2018-03-22',\n  'genre_classifications': ['Pop'],\n  'tempo': 110.0,\n  'key': 'G major',\n  'loudness': -7.8\n}]
```
