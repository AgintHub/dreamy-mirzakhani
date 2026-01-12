# process_song_metadata PRD

## Description
Extract key metadata fields from database and web‑scraped results and collate them into four ordered lists: titles, artists, albums, and genre tags.


## Conceptual Info

Takes raw match strings and confidence scores from both the music database and web scraping engines, normalizes and merges them, then produces four clean lists of titles, artists, albums, and genres for downstream HTML generation.

## Docstring

### Summary
Collates and normalises song metadata from the music database and web sources.

### Parameters

- **song_matches** (List[str]): Exact song titles returned by the music database API.
- **relevance_scores** (List[float]): Confidence scores corresponding to each entry in ``song_matches``.
- **additional_matches** (List[str]): Supplementary song titles scraped from web sources.
- **web_scores** (List[float]): Confidence scores for each web‑scraped match.

### Returns

Dict[str, List[str]]: Dictionary with keys ``song_titles``, ``artist_names``, ``album_names`` and ``genre_tags``.

### Raises

- ValueError: If all input match lists are empty or lengths of score lists do not match the corresponding match lists.

### Examples

```python
>>> song_matches = ['The Midnight Hour', 'The Midnight Hour (Live)'],
>>> relevance_scores = [0.95, 0.60],
>>> additional_matches = ['The Midnight Hour – Acoustic'],
>>> web_scores = [0.80],
>>> metadata = process_song_metadata(song_matches, relevance_scores, additional_matches, web_scores)
{
  'song_titles': ['The Midnight Hour', 'The Midnight Hour (Live)', 'The Midnight Hour – Acoustic'],
  'artist_names': ['Unknown Artist'],
  'album_names': ['Midnight Collection'],
  'genre_tags': ['Jazz', 'Blues']
}
```

```python
>>> try:
...     process_song_metadata([], [], [], [])
>>> except ValueError as e:
...     print(e)
'All input match lists must contain at least one element.'
```
