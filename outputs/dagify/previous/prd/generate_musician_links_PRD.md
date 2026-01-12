# generate_musician_links PRD

## Description
Create artist navigation links by aggregating database search results and web‑scraped metadata.


## Conceptual Info

The node synthesises music metadata from two upstream services—an external music database and a web‑scraping engine—into user‑friendly hyperlinks. The resulting URLs enable seamless navigation from the HTML report to external artist pages.

## Docstring

### Summary
Builds artist profile URLs and official website links from database matches and web‑scraped data.

### Parameters

- **song_matches** (List[str]): List of song titles returned by the music database API.
- **relevance_scores** (List[float]): Relevance scores corresponding to each entry in song_matches.
- **additional_matches** (List[str]): List of URLs or titles obtained through web scraping.
- **web_scores** (List[float]): Relevance scores for each web‑scraped match.

### Returns

dict: Dictionary containing two lists:
- musician_urls: List of artist profile links.
- official_websites: List of official band or artist web presences.

### Raises

- ValueError: Raised when input lists are of mismatched lengths or contain None values.

### Examples

```python
>>> musician_urls, official_websites = generate_musician_links(
...     song_matches=['Song A', 'Song B'],
...     relevance_scores=[0.95, 0.88],
...     additional_matches=['https://artist.com', 'https://band.org'],
...     web_scores=[0.92, 0.85])
>>> print('musician_urls:', musician_urls)
>>> print('official_websites:', official_websites)
musician_urls: ['https://musicdb.com/song_a', 'https://musicdb.com/song_b']
official_websites: ['https://artist.com', 'https://band.org']
```

```python
>>> # Handling inconsistent input lengths
>>> try:
...     generate_musician_links(song_matches=['Song A'],
...                              relevance_scores=[0.95, 0.88],
...                              additional_matches=['https://artist.com'],
...                              web_scores=[0.92])
>>> except ValueError as e:
...     print('Error:', e)
Error: Input list lengths do not match.
```
