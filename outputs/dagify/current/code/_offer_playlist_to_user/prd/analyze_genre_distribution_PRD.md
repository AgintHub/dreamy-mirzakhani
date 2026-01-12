# analyze_genre_distribution PRD

## Description
Analyzes genre distribution in track details and compares it with existing genres, returning a summary of genre representation.


## Conceptual Info

This shim analyzes the genre distribution of tracks in a playlist and compares it with existing genres to provide a summary of genre representation.

## Docstring

### Summary
Analyzes genre distribution in track details against existing genres, returning a summary of genre representation.

### Parameters

- **track_details** (str): A JSON string representing a list of dictionaries containing track metadata, including genre information.
- **existing_genres** (str): A JSON string representing a list of existing genre representations in the playlist.

### Returns

str: A JSON string containing 'genre_list' and 'genre_counts', representing the genres present and their respective counts.

### Raises

- ValueError: If the input JSON strings are malformed or cannot be parsed.
- TypeError: If the parsed JSON does not match the expected structure (list of dictionaries for track_details and list for existing_genres).

### Examples

```python
>>> import json
>>> track_details = json.dumps([{'genre': 'rock'}, {'genre': 'pop'}, {'genre': 'rock'}])
>>> existing_genres = json.dumps(['rock', 'pop'])
>>> analyze_genre_distribution(track_details=track_details, existing_genres=existing_genres)
"{'genre_list': ['rock', 'pop'], 'genre_counts': [2, 1]}"
```

```python
>>> import json
>>> track_details = json.dumps([{'genre': 'jazz'}, {'genre': 'classical'}])
>>> existing_genres = json.dumps(['jazz', 'rock'])
>>> analyze_genre_distribution(track_details=track_details, existing_genres=existing_genres)
"{'genre_list': ['jazz', 'classical'], 'genre_counts': [1, 1]}"
```
