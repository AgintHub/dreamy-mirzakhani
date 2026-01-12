# process_song_metadata PRD

## Description
Extract key metadata fields from database and web‑scraped results and collate them into four ordered lists: titles, artists, albums, and genre tags.


## Conceptual Info

The node consolidates metadata from multiple sources, normalises it, and outputs four aligned lists that can be rendered into an HTML page or used for further analytics.

## Docstring

### Summary
Combines song metadata obtained from the music database API and web scraping results into four synchronized lists of titles, artists, albums, and genre tags.

### Parameters

- **song_matches** (List[str]): Song titles returned by the music_database_api.
- **relevance_scores** (List[float]): Relevance scores corresponding to each entry in song_matches.
- **additional_matches** (List[str]): Additional song titles scraped from the web.
- **web_scores** (List[float]): Web‑source relevance scores corresponding to each entry in additional_matches.

### Returns

Tuple[List[str], List[str], List[str], List[str]]: A tuple containing four lists: song_titles, artist_names, album_names, and genre_tags, all aligned by index.

### Raises

- ValueError: If any input list is empty or the lengths of the paired lists do not match.
- RuntimeError: If metadata extraction from the supplied titles fails (e.g., no match found in either source).

### Examples

```python
>>> song_titles, artist_names, album_names, genre_tags = process_song_metadata(
    ['Song A', 'Song B'],
    [0.92, 0.85],
    ['Song A (Live)', 'Song B (Remix)'],
    [0.97, 0.83]
)
>>> print(song_titles)
>>> print(artist_names)
>>> print(album_names)
>>> print(genre_tags)
['Song A', 'Song B']
['Artist X', 'Artist Y']
['Album X', 'Album Y']
['Pop', 'Rock']
```

```python
>>> try:
...     process_song_metadata([], [], [], [])
>>> except ValueError as e:
...     print(e)
Input lists cannot be empty.
```
