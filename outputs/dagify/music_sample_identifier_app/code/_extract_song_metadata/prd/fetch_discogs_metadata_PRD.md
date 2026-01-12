# fetch_discogs_metadata PRD

## Description
Fetches metadata for a given track from Discogs based on track ID, artist, and title.


## Conceptual Info

This shim node is responsible for retrieving metadata for a specific track from the Discogs database. It takes the track ID, artist name, and track title as inputs and returns a dictionary containing the metadata.

## Docstring

### Summary
Fetches Discogs metadata for a track based on its ID, artist, and title.

### Parameters

- **track_id** (str): The unique identifier of the track in the database.
- **artist** (str): The name of the artist of the track.
- **title** (str): The title of the track.

### Returns

str: A string representation of a dictionary containing the Discogs metadata for the track, including details like release date, genre, and other relevant information.

### Raises

- ValueError: If the input track ID, artist name, or title is invalid or missing.
- TypeError: If the input types are not as expected (e.g., track ID is not a string).
- ConnectionError: If there's a failure in connecting to the Discogs API.

### Examples

```python
>>> fetch_discogs_metadata(track_id='12345', artist='Example Artist', title='Example Track')
{'release_date': '2020-01-01', 'genre': 'Electronic', 'style': 'Techno'}
```

```python
>>> fetch_discogs_metadata(track_id='67890', artist='Another Artist', title='Another Track')
{'release_date': '2015-06-01', 'genre': 'Rock', 'style': 'Indie'}
```
