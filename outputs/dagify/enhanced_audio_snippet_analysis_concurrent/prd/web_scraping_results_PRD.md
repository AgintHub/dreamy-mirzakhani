# web_scraping_results PRD

## Description
Scrape additional music metadata from web sources using tonal and pitch characteristics as search criteria.


## Conceptual Info

The node takes tonal and pitch data, queries web‑based music information sources (e.g., lyric sites, streaming APIs, fan forums), and returns a consolidated list of matching tracks along with a relevance score.

## Docstring

### Summary
Collects music metadata from the web using tonal and pitch cues.

### Parameters

- **tone** (str): Identified musical key from tonal_analysis (e.g., "C major").
- **tone_confidence** (float): Reliability of the tonal detection (0.0‑1.0).
- **fundamental_frequency** (float): Primary pitch frequency extracted by pitch_analysis, in Hz.
- **pitch_confidence** (float): Reliability of the pitch detection (0.0‑1.0).

### Returns

Tuple[str, float]: A tuple containing the web‑sourced matches string and a relevance score float.

### Raises

- ValueError: Raised if any input is missing or invalid (e.g., empty tone, negative frequency).
- ConnectionError: Raised if the web query fails due to network issues.

### Examples

```python
>>> matches, score = web_scraping_results('C major', 0.95, 110.0, 0.92)
('Song A, Song B, Song C', 0.88)
```

```python
>>> matches, score = web_scraping_results('A minor', 0.80, 98.5, 0.75)
('Track X, Track Y', 0.70)
```
