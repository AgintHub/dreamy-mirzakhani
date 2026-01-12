# web_scraping_results PRD

## Description
Scrape additional music metadata from web sources using tonal and pitch characteristics as search criteria.


## Conceptual Info

The node performs a targeted web search for music tracks by using the detected tonal key and fundamental frequency as query constraints, returning a list of best‑matching titles and a confidence score for each match.

## Docstring

### Summary
Scrape web sources for music tracks that match the given tonal key and fundamental frequency.

### Parameters

- **tone** (str): Identified musical key from tonal analysis (e.g., 'C# Major').
- **tone_confidence** (float): Reliability score (0.0–1.0) of the tonal key detection.
- **fundamental_frequency** (float): Estimated fundamental pitch in Hz from pitch analysis.
- **pitch_confidence** (float): Reliability score (0.0–1.0) of the pitch detection.

### Returns

(str, float): A tuple containing a comma‑separated string of matching song titles and a single float representing the average relevance score from the web source.

### Raises

- ValueError: Raised if any of the required input parameters are missing or not within the expected ranges.
- RuntimeError: Raised when the web request fails or returns an unexpected response format.

### Examples

```python
>>> titles, score = scrape_web_sources('C Major', 0.92, 261.63, 0.88)
>>> print(titles)
>>> print(score)
"song A, song B, song C"\n0.89
```

```python
>>> titles, score = scrape_web_sources('G# Minor', 0.85, 220.00, 0.80)
>>> print(titles)
>>> print(score)
"song X, song Y"\n0.75
```
