# generate_musician_links PRD

## Description
Create artist navigation links by aggregating database search results and web‑scraped metadata.


## Conceptual Info

This node consolidates and normalises artist link information gathered from the music database and web scraping stages, producing a curated set of profile URLs and official website links for downstream HTML generation.

## Docstring

### Summary
Generate deep links to musician profiles by merging and filtering results from the music database API and web scraping results.

### Parameters

- **song_matches** (List[str]): List of artist profile URLs returned by the music database API.
- **relevance_scores** (List[float]): Relevance scores associated with each entry in `song_matches`.
- **additional_matches** (List[str]): Artist profile URLs scraped from external web sources.
- **web_scores** (List[float]): Relevance scores for each entry in `additional_matches`.

### Returns

Dict[str, List[str]]: A dictionary with two keys:
- `musician_urls`: deduplicated list of all profile URLs.
- `official_websites`: list of URLs identified as official band or artist websites.

### Raises

- ValueError: Raised if any of the input lists are empty.
- ValueError: Raised if the lengths of `song_matches` and `relevance_scores` differ, or if `additional_matches` and `web_scores` differ.
- TypeError: Raised if any argument is not of the expected list type.

### Examples

```python
>>> song_matches = ["https://musicdb.com/artist/123", "https://musicdb.com/artist/456"],
>>> relevance_scores = [0.95, 0.80],
>>> additional_matches = ["https://artistpage.com/123", "https://artistpage.com/789"],
>>> web_scores = [0.90, 0.85],
>>> links = generate_musician_links(song_matches, relevance_scores, additional_matches, web_scores)
>>> print(links["musician_urls"])
>>> print(links["official_websites"])
["https://musicdb.com/artist/123", "https://musicdb.com/artist/456", "https://artistpage.com/123", "https://artistpage.com/789"]
["https://musicdb.com/artist/123", "https://artistpage.com/123"]
```

```python
>>> # Handling a mismatch in list lengths
>>> try:
...     generate_musician_links(["url1"], [0.9, 0.8], [], [])
>>> except ValueError as e:
...     print(e)
"Relevance scores list length does not match song_matches list length."
```
