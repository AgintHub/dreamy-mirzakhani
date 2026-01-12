# apply_collaborative_filtering PRD

## Description
Applies collaborative filtering to compute similarity scores between musicians and songs based on provided metadata.


## Conceptual Info

This shim computes collaborative filtering scores that capture the affinity between musicians and songs, enabling downstream graph-based recommendation models.

## Docstring

### Summary
Computes collaborative filtering scores from musician data and song metadata.

### Parameters

- **musician_data** (str): JSON string containing expanded musician information (ids, names, aliases).
- **songs_metadata** (str): JSON string containing metadata for each song (e.g., title, artist, genre, features).

### Returns

str: JSON string that maps musician IDs to song IDs with associated similarity scores.

### Raises

- ValueError: Raised when the input JSON does not contain required fields or is malformed.
- TypeError: Raised when either musician_data or songs_metadata is not a string.

### Examples

```python
>>> musician_data = '{"musician_ids": ["m1"], "musician_names": ["Artist A"], "musician_aliases": [[]]}'
>>> songs_metadata = '{"songs": [{"song_id": "s1", "title": "Song X"}]}'
>>> apply_collaborative_filtering(musician_data, songs_metadata)
{"m1": {"s1": 0.85}}
```

```python
>>> apply_collaborative_filtering('invalid json', '{}')
ValueError: Invalid JSON format for musician_data.
```
