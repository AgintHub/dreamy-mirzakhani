# merge_metadata_sources PRD

## Description
Merges metadata from Discogs, MusicBrainz, and Spotify into a unified output.


## Conceptual Info

This shim function is designed to merge metadata from three different music information sources: Discogs, MusicBrainz, and Spotify. It takes the metadata dictionaries from these sources as input and produces a unified metadata dictionary that combines the information.

## Docstring

### Summary
Merges metadata from Discogs, MusicBrainz, and Spotify into a single dictionary.

### Parameters

- **discogs** (str): Metadata dictionary retrieved from Discogs.
- **musicbrainz** (str): Metadata dictionary retrieved from MusicBrainz.
- **spotify** (str): Metadata dictionary retrieved from Spotify.

### Returns

str: A unified metadata dictionary containing merged information from the input sources.

### Raises

- TypeError: If any of the input parameters are not dictionaries.
- ValueError: If the input dictionaries contain conflicting information that cannot be merged.

### Examples

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
