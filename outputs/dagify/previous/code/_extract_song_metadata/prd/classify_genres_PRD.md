# classify_genres PRD

## Description
This shim node classifies a song into various genres based on its metadata and audio features.


## Conceptual Info

The classify_genres shim node is responsible for determining the genres of a song by analyzing its metadata and audio features. It plays a crucial role in music classification and recommendation systems.

## Docstring

### Summary
Classify the genres of a song based on its metadata and audio features.

### Parameters

- **metadata** (str): A string containing song metadata, potentially in JSON format, that includes information such as artist name, album title, and release date.
- **audio_features** (str): A string containing audio features of the song, potentially in JSON format, that includes information such as tempo, key, and loudness.

### Returns

str: A string representing a list of genres classified for the song, potentially in a comma-separated format.

### Raises

- ValueError: When the input metadata or audio features are not in the expected format or are missing required information.
- TypeError: When the input types are not as expected (e.g., not strings).

### Examples

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
