# process_song_metadata PRD

## Description
Extract key metadata fields from database and web‑scraped results and collate them into four ordered lists: titles, artists, albums, and genre tags.


## Conceptual Info

Aggregates song metadata from multiple sources into a structured format for downstream HTML rendering.

## Docstring

### Summary
Collects and organizes song metadata (titles, artists, albums, genre tags) from database search results and web‑scraped data.

### Parameters

- **song_matches** (List[str]): List of song titles returned by the music database API.
- **relevance_scores** (List[float]): Relevance scores corresponding to each title in song_matches.
- **additional_matches** (str): Comma‑separated list of song titles retrieved via web scraping.
- **web_scores** (float): Confidence metric indicating the quality of the web‑scraped matches.

### Returns

Dict[str, List[str]]: A dictionary with keys 'song_titles', 'artist_names', 'album_names', and 'genre_tags', each mapping to a list of strings.

### Raises

- ValueError: If the length of song_matches does not match relevance_scores.
- TypeError: If any input is of an incorrect type.

### Examples

```python
>>> result = process_song_metadata(
...     song_matches=["Bohemian Rhapsody"],
...     relevance_scores=[0.97],
...     additional_matches="Bohemian Rhapsody",
...     web_scores=0.92)
>>> print(result)
{'song_titles': ['Bohemian Rhapsody'], 'artist_names': ['Queen'], 'album_names': ['A Night at the Opera'], 'genre_tags': ['Rock', 'Classic Rock']}
```

```python
>>> result = process_song_metadata(
...     song_matches=["Imagine", "Let It Be"],
...     relevance_scores=[0.88, 0.85],
...     additional_matches="Imagine, Let It Be",
...     web_scores=0.90)
>>> print(result)
{'song_titles': ['Imagine', 'Let It Be'], 'artist_names': ['John Lennon', 'The Beatles'], 'album_names': ['Imagine', 'Let It Be'], 'genre_tags': ['Pop', 'Rock']}
```
