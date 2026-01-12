# _extract_song_metadata - Complete PRD Documentation

## Overview
PRDs for nodes in the '_extract_song_metadata' module.

## Table of Contents

- [validate_track_data](#validate_track_data)

- [fetch_discogs_metadata](#fetch_discogs_metadata)

- [fetch_musicbrainz_metadata](#fetch_musicbrainz_metadata)

- [fetch_spotify_metadata](#fetch_spotify_metadata)

- [merge_metadata_sources](#merge_metadata_sources)

- [extract_audio_features](#extract_audio_features)

- [normalize_artist_names](#normalize_artist_names)

- [extract_album_info](#extract_album_info)

- [classify_genres](#classify_genres)

- [validate_metadata_consistency](#validate_metadata_consistency)



---

## validate_track_data

### Description
Validates the input track data for consistency and correctness.

### Conceptual Info

This shim node is responsible for validating the input track data, ensuring it is consistent and correct before proceeding with further processing.

### Docstring

**Summary:** Validates the input track data for required fields and format consistency.

**Parameters:**

- track_data (IdentifySampledSongsOutput): Input object containing track data to be validated.
**Returns:** str - Output indicating the validation result.

**Raises:**

- ValueError: When the input track data is missing required fields or has incorrect format.
- TypeError: When the input track data is not of the expected type.
**Examples:**

```python
>>> from pydantic import BaseModel, Field
>>> class IdentifySampledSongsOutput(BaseModel):
...     track_id: str = Field(..., description='Unique identifier for the candidate track')
...     artist_name: str = Field(..., description='Name of the artist of the candidate track')
>>> validate_track_data(track_data=IdentifySampledSongsOutput(track_id='123', artist_name='Artist', track_title='Title', start_time=0.0, end_time=10.0, confidence=0.8, release_date='2020-01-01'))
'Track data is valid'
```

```python
>>> validate_track_data(track_data=IdentifySampledSongsOutput(track_id='', artist_name='Artist', track_title='Title', start_time=0.0, end_time=10.0, confidence=0.8, release_date='2020-01-01'))
'Error: track_id is required'
```



---

## fetch_discogs_metadata

### Description
Fetches metadata for a given track from Discogs based on track ID, artist, and title.

### Conceptual Info

This shim node is responsible for retrieving metadata for a specific track from the Discogs database. It takes the track ID, artist name, and track title as inputs and returns a dictionary containing the metadata.

### Docstring

**Summary:** Fetches Discogs metadata for a track based on its ID, artist, and title.

**Parameters:**

- track_id (str): The unique identifier of the track in the database.
- artist (str): The name of the artist of the track.
- title (str): The title of the track.
**Returns:** str - A string representation of a dictionary containing the Discogs metadata for the track, including details like release date, genre, and other relevant information.

**Raises:**

- ValueError: If the input track ID, artist name, or title is invalid or missing.
- TypeError: If the input types are not as expected (e.g., track ID is not a string).
- ConnectionError: If there's a failure in connecting to the Discogs API.
**Examples:**

```python
>>> fetch_discogs_metadata(track_id='12345', artist='Example Artist', title='Example Track')
{'release_date': '2020-01-01', 'genre': 'Electronic', 'style': 'Techno'}
```

```python
>>> fetch_discogs_metadata(track_id='67890', artist='Another Artist', title='Another Track')
{'release_date': '2015-06-01', 'genre': 'Rock', 'style': 'Indie'}
```



---

## fetch_musicbrainz_metadata

### Description
Fetches MusicBrainz metadata for a given track ID, artist name, and track title, returning the result as a JSON string.

### Conceptual Info

The shim retrieves structured metadata from MusicBrainz, enabling downstream nodes to enrich song information.

### Docstring

**Summary:** Retrieve MusicBrainz metadata for a track.

**Parameters:**

- track_id (str): Unique identifier for the track in MusicBrainz.
- artist (str): Name of the artist performing the track.
- title (str): Title of the track.
**Returns:** str - A JSON-formatted string containing the retrieved MusicBrainz metadata.

**Raises:**

- ValueError: If any required parameter is missing or empty.
- TypeError: If a parameter is not of type str.
**Examples:**

```python
>>> metadata = fetch_musicbrainz_metadata(track_id='12345', artist='The Beatles', title='Hey Jude')
{"artist": "The Beatles", "title": "Hey Jude", "release_date": "1968-08-26", "genres": ["Rock"]}
```

```python
>>> metadata = fetch_musicbrainz_metadata(track_id='99999', artist='Unknown Artist', title='Unknown Song')
{}
```



---

## fetch_spotify_metadata

### Description
Fetches metadata for a given track from Spotify based on track ID, artist, and title.

### Conceptual Info

This shim is responsible for retrieving metadata for a specific track from Spotify using the track ID, artist name, and track title. The retrieved metadata is crucial for further processing and merging with data from other sources.

### Docstring

**Summary:** Fetches and returns Spotify metadata for a given track based on its ID, artist, and title.

**Parameters:**

- track_id (str): Unique identifier for the track.
- artist (str): Name of the artist associated with the track.
- title (str): Title of the track.
**Returns:** str - A JSON-formatted string containing the Spotify metadata for the track.

**Raises:**

- ValueError: If the input parameters (track_id, artist, title) are invalid or missing.
- TypeError: If the input parameters are of incorrect type.
- Exception: If there's an issue with the Spotify API request or response parsing.
**Examples:**

```python
>>> fetch_spotify_metadata(track_id='12345', artist='Example Artist', title='Example Track')
{'album': {'name': 'Example Album'}, 'artists': [{'name': 'Example Artist'}], 'name': 'Example Track'}
```

```python
>>> fetch_spotify_metadata(track_id='67890', artist='Another Artist', title='Another Track')
{'album': {'name': 'Another Album'}, 'artists': [{'name': 'Another Artist'}], 'name': 'Another Track'}
```



---

## merge_metadata_sources

### Description
Merges metadata from Discogs, MusicBrainz, and Spotify into a unified output.

### Conceptual Info

This shim function is designed to merge metadata from three different music information sources: Discogs, MusicBrainz, and Spotify. It takes the metadata dictionaries from these sources as input and produces a unified metadata dictionary that combines the information.

### Docstring

**Summary:** Merges metadata from Discogs, MusicBrainz, and Spotify into a single dictionary.

**Parameters:**

- discogs (str): Metadata dictionary retrieved from Discogs.
- musicbrainz (str): Metadata dictionary retrieved from MusicBrainz.
- spotify (str): Metadata dictionary retrieved from Spotify.
**Returns:** str - A unified metadata dictionary containing merged information from the input sources.

**Raises:**

- TypeError: If any of the input parameters are not dictionaries.
- ValueError: If the input dictionaries contain conflicting information that cannot be merged.
**Examples:**

```python
>>> discogs_data = {'artist': 'Example Artist', 'title': 'Example Title', 'year': '2020'}
>>> musicbrainz_data = {'artist': 'Example Artist', 'title': 'Example Title', 'release-group': {'first-release-date': '2020-01-01'}}
>>> spotify_data = {'artists': [{'name': 'Example Artist'}], 'name': 'Example Title', 'release_date': '2020'}
>>> merged_data = merge_metadata_sources(discogs=discogs_data, musicbrainz=musicbrainz_data, spotify=spotify_data)
{'artist': 'Example Artist', 'title': 'Example Title', 'release_date': '2020-01-01'}
```

```python
>>> empty_data = {}
>>> merged_data = merge_metadata_sources(discogs=empty_data, musicbrainz=empty_data, spotify=empty_data)
{}
```



---

## extract_audio_features

### Description
Extracts audio features from a given track segment defined by start and end times.

### Conceptual Info

This shim node is responsible for extracting relevant audio features from a specified segment of an audio track. It plays a crucial role in music analysis and metadata extraction pipelines.

### Docstring

**Summary:** Extracts audio features from a specified track segment.

**Parameters:**

- track_id (str): Unique identifier for the audio track.
- start_time (str): Start time of the segment in seconds.
- end_time (str): End time of the segment in seconds.
**Returns:** str - A JSON string representing a dictionary of extracted audio features, including tempo, key, and loudness.

**Raises:**

- ValueError: If the track_id is invalid, or if start_time is greater than end_time.
- TypeError: If the input parameters are not of the expected type.
**Examples:**

```python
>>> extract_audio_features(track_id='TR12345', start_time='0.0', end_time='30.0')
{"tempo": 120.0, "key": "C major", "loudness": -6.0}
```

```python
>>> extract_audio_features(track_id='TR67890', start_time='10.5', end_time='40.5')
{"tempo": 128.0, "key": "G minor", "loudness": -3.0}
```



---

## normalize_artist_names

### Description
Normalizes artist names by standardizing formatting and handling variations in artist name representations.

### Conceptual Info

This shim node is responsible for taking raw artist names from metadata and normalizing them into a consistent format. It handles variations in naming conventions, punctuation, and other discrepancies across different data sources.

### Docstring

**Summary:** Normalizes artist names to achieve consistency across different metadata sources.

**Parameters:**

- raw_artists (str): The raw artist names that need to be normalized, potentially containing multiple artists separated by various delimiters.
**Returns:** str - A string containing the normalized artist names, formatted consistently.

**Raises:**

- ValueError: If the input raw_artists is not a string or is empty.
- TypeError: If the input type is not str.
**Examples:**

```python
>>> normalize_artist_names(raw_artists='John Doe, Jane Doe')
'John Doe & Jane Doe'
```

```python
>>> normalize_artist_names(raw_artists='The Beatles, The Rolling Stones')
'The Beatles & The Rolling Stones'
```



---

## extract_album_info

### Description
Extracts album information from the provided metadata.

### Conceptual Info

This shim is responsible for extracting relevant album information from a given metadata object, which is expected to contain details about a music track or album.

### Docstring

**Summary:** Extracts and formats album information from the provided metadata.

**Parameters:**

- metadata (dict): Dictionary containing metadata about a music track or album, including album title, artist, release date, etc.
**Returns:** str - Formatted string containing the extracted album information.

**Raises:**

- KeyError: If required keys are missing from the metadata dictionary.
- TypeError: If the input metadata is not a dictionary.
**Examples:**

```python
>>> metadata = {'album': 'Thriller', 'artist': 'Michael Jackson', 'release_date': '1982'}
>>> album_info = extract_album_info(metadata=metadata)
'Thriller by Michael Jackson (1982)'
```

```python
>>> metadata = {'album': 'Bad', 'artist': 'Michael Jackson', 'release_date': '1987'}
>>> album_info = extract_album_info(metadata=metadata)
'Bad by Michael Jackson (1987)'
```



---

## classify_genres

### Description
This shim node classifies a song into various genres based on its metadata and audio features.

### Conceptual Info

The classify_genres shim node is responsible for determining the genres of a song by analyzing its metadata and audio features. It plays a crucial role in music classification and recommendation systems.

### Docstring

**Summary:** Classify the genres of a song based on its metadata and audio features.

**Parameters:**

- metadata (str): A string containing song metadata, potentially in JSON format, that includes information such as artist name, album title, and release date.
- audio_features (str): A string containing audio features of the song, potentially in JSON format, that includes information such as tempo, key, and loudness.
**Returns:** str - A string representing a list of genres classified for the song, potentially in a comma-separated format.

**Raises:**

- ValueError: When the input metadata or audio features are not in the expected format or are missing required information.
- TypeError: When the input types are not as expected (e.g., not strings).
**Examples:**

```python
>>> metadata = '{\"artist\": \"Example Artist\", \"album\": \"Example Album\"}'
>>> audio_features = '{\"tempo\": 120, \"key\": \"C major\"}'
>>> classify_genres(metadata=metadata, audio_features=audio_features)
'Pop, Rock'
```

```python
>>> metadata = '{\"artist\": \"Another Artist\", \"album\": \"Another Album\"}'
>>> audio_features = '{\"tempo\": 100, \"key\": \"A minor\"}'
>>> classify_genres(metadata=metadata, audio_features=audio_features)
'Jazz, Blues'
```



---

## validate_metadata_consistency

### Description
Validates the consistency of metadata across different sources and audio features.

### Conceptual Info

This shim node is responsible for validating the consistency of metadata across different sources (like Discogs, MusicBrainz, and Spotify) and audio features extracted from a song sample.

### Docstring

**Summary:** Validates metadata consistency by comparing information from different metadata sources and audio features.

**Parameters:**

- metadata (str): Merged metadata from various sources like Discogs, MusicBrainz, and Spotify as a string representation of a dictionary.
- audio_features (str): Audio features extracted from the song sample as a string representation of a dictionary.
**Returns:** str - Validated metadata in dictionary format as a string, ensuring consistency across different sources and with audio features.

**Raises:**

- ValueError: If the input metadata or audio features are not valid or cannot be parsed into dictionaries.
- TypeError: If the input types are not strings or if the parsed dictionaries contain inconsistent or missing data.
**Examples:**

```python
>>> metadata = '{\"title\": \"Song Title\", \"artist\": \"Artist Name\"}'
>>> audio_features = '{\"tempo\": 120.0, \"key\": \"C major\"}'
>>> validated_metadata = validate_metadata_consistency(metadata=metadata, audio_features=audio_features)
'{\"title\": \"Song Title\", \"artist\": \"Artist Name\", \"tempo\": 120.0, \"key\": \"C major\"}'
```

```python
>>> metadata = '{\"title\": \"Different Title\", \"artist\": \"Artist Name\"}'
>>> audio_features = '{\"tempo\": 120.0, \"key\": \"C major\"}'
>>> validated_metadata = validate_metadata_consistency(metadata=metadata, audio_features=audio_features)
'{\"title\": \"Different Title\", \"artist\": \"Artist Name\", \"tempo\": 120.0, \"key\": \"C major\"}' # or raises an error depending on validation logic
```

