# extract_nlp_features PRD

## Description
Extracts NLP features from the given songs metadata.


## Conceptual Info

This shim node is responsible for extracting NLP features from the provided songs metadata, which is crucial for further processing in the playlist generation pipeline.

## Docstring

### Summary
Extracts NLP features from the given songs metadata and returns them as a string representation of a dictionary.

### Parameters

- **songs_metadata** (str): A string representation of a list of dictionaries containing songs metadata.

### Returns

str: A string representation of a dictionary containing the extracted NLP features.

### Raises

- ValueError: If the input songs metadata is not in the expected format or is empty.
- TypeError: If the input type is not a string or if the input string cannot be parsed into a list of dictionaries.

### Examples

```python
>>> songs_metadata = '[{"title": "Song 1", "lyrics": "Lyrics 1"}, {"title": "Song 2", "lyrics": "Lyrics 2"}]'
>>> extract_nlp_features(songs_metadata=songs_metadata)
'{"song1": {"feature1": 0.5, "feature2": 0.3}, "song2": {"feature1": 0.2, "feature2": 0.7}}'
```

```python
>>> songs_metadata = '[{"title": "Invalid Song", "lyrics": null}]'
>>> extract_nlp_features(songs_metadata=songs_metadata)
ValueError: Input songs metadata contains invalid or missing data.
```
