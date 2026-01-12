# generate_musician_links PRD

## Description
Create artist navigation links by aggregating database search results and web‑scraped metadata.


## Conceptual Info

Aggregates and normalizes artist URLs from multiple data sources, ensuring that every matched track is represented by a consistent set of profile links and official websites for downstream HTML rendering.

## Docstring

### Summary
Generate deep links to musician profiles by merging database and web‑scraped results.

### Parameters

- **song_matches** (List[str]): List of song titles returned by the external music database.
- **relevance_scores** (List[float]): Relevance scores corresponding to each entry in *song_matches*.
- **additional_matches** (List[str]): List of additional song titles obtained from web scraping.
- **web_scores** (List[float]): Relevance scores from the web scraping source.

### Returns

Dict[str, List[str]]: A dictionary with two keys:

* *musician_urls* – a list of artist profile links constructed from the merged search results.
* *official_websites* – a list of official band or artist websites extracted from the same data.

Both lists are deduplicated and ordered by combined relevance.

### Raises

- ValueError: If any of the input lists are empty or if their lengths do not match.
- TypeError: If an input is not of the expected type.

### Examples

```python
>>> result = generate_musician_links(
...     song_matches=['Song A', 'Song B'],
...     relevance_scores=[0.95, 0.80],
...     additional_matches=['Song A', 'Song C'],
...     web_scores=[0.90, 0.70])
{'musician_urls': ['https://artistA.com', 'https://artistB.com', 'https://artistC.com'], 'official_websites': ['https://artistA.com', 'https://artistB.com', 'https://artistC.com']}
```

```python
>>> result = generate_musician_links(
...     song_matches=['Hit 1'],
...     relevance_scores=[0.88],
...     additional_matches=['Hit 1'],
...     web_scores=[0.85])
{'musician_urls': ['https://artistX.com'], 'official_websites': ['https://artistX.com']}
```
