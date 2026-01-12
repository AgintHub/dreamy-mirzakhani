# process_song_metadata PRD

## Description
Extract key metadata fields from database and web‑scraped results and collate them into four ordered lists: titles, artists, albums, and genre tags.


## Conceptual Info

Aggregates and normalises song metadata from the music database and web scraping sources into parallel lists that are ready for HTML rendering.

## Docstring

### Summary
Collects and aligns metadata from the database and web‑scraped results into four ordered lists: titles, artists, albums, and genre tags.

### Parameters

- **song_matches** (List[str]): Song titles returned by the music database search.
- **relevance_scores** (List[float]): Relevance scores from the music database, corresponding to each title.
- **additional_matches** (List[str]): Song titles scraped from web sources.
- **web_scores** (List[float]): Relevance scores from the web scraping, corresponding to each scraped title.

### Returns

Tuple[List[str], List[str], List[str], List[str]]: Four ordered lists:
- `song_titles`: combined titles from database and web.
- `artist_names`: artist names for each title.
- `album_names`: album names for each title.
- `genre_tags`: aggregated genre tags for each title.

### Raises

- ValueError: If input lists have mismatched lengths or contain None values.
- KeyError: If required metadata fields are missing from the input data.

### Examples

```python
>>> song_matches = ['Song A', 'Song B']
>>> relevance_scores = [0.92, 0.88]
>>> additional_matches = ['Song C']
>>> web_scores = [0.75]
>>> # Assume the function aggregates data from both sources
>>> titles, artists, albums, genres = process_song_metadata(song_matches, relevance_scores, additional_matches, web_scores)
[['Song A', 'Song B', 'Song C'],
 ['Artist X', 'Artist Y', 'Artist Z'],
 ['Album 1', 'Album 2', 'Album 3'],
 ['Pop', 'Rock', 'Jazz']]
```

```python
>>> song_matches = ['Track 1']
>>> relevance_scores = [0.95]
>>> additional_matches = []
>>> web_scores = []
>>> # Single match from the database only
>>> titles, artists, albums, genres = process_song_metadata(song_matches, relevance_scores, additional_matches, web_scores)
[['Track 1'],
 ['Artist A'],
 ['Album X'],
 ['Electronic']]
```
