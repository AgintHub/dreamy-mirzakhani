# process_song_metadata PRD

## Description
Extract key metadata fields from database and web‑scraped results and collate them into four ordered lists: titles, artists, albums, and genre tags.


## Conceptual Info

This node processes metadata from multiple sources to organize song information into structured categories.

## Docstring

### Summary
Extracts and organizes song metadata from database and web sources into four lists: song titles, artist names, album names, and genre tags.

### Parameters

- **music_database_api_results** (Tuple[List[str], List[float]]): Tuple containing song matches and their relevance scores from the music database API.
- **web_scraping_results** (Tuple[str, float]): Tuple containing additional song matches from web scraping and their relevance scores.

### Returns

Tuple[List[str], List[str], List[str], List[str]]: Tuple containing four lists: song titles, artist names, album names, and genre tags.

### Raises

- ValueError: If the input data from either source is malformed or inconsistent.

### Examples

```python
>>> song_matches = ['Song1', 'Song2']
>>> relevance_scores = [0.9, 0.8]
>>> additional_matches = 'Song3,Song4'
>>> web_scores = 0.85
>>> process_song_metadata((song_matches, relevance_scores), (additional_matches, web_scores))
(['Song1', 'Song2', 'Song3', 'Song4'], ['Artist1', 'Artist2', 'Artist3', 'Artist4'], ['Album1', 'Album2', 'Album3', 'Album4'], ['Rock', 'Pop', 'Jazz', 'Classical'])
```
