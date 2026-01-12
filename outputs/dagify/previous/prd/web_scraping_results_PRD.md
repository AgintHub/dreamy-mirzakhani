# web_scraping_results PRD

## Description
Scrape additional music metadata from web sources using tonal and pitch characteristics as search criteria.


## Conceptual Info

This node performs web scraping to find additional music metadata based on tonal and pitch characteristics provided by its parent nodes.

## Docstring

### Summary
Scrape web sources for music metadata matching the tonal and pitch characteristics of an audio sample.

### Parameters

- **tonal_analysis** (dict): Output from tonal_analysis node containing 'tone' and 'tone_confidence'.
- **pitch_analysis** (dict): Output from pitch_analysis node containing 'fundamental_frequency' and 'pitch_confidence'.

### Returns

Tuple[str, float]: A tuple containing a comma-separated string of additional song matches and a float representing the relevance score of these matches.

### Raises

- ConnectionError: If the web scraping request fails due to network issues.
- ValueError: If the input tonal or pitch analysis data is invalid or missing required fields.

### Examples

```python
>>> tonal_data = {'tone': 'C Major', 'tone_confidence': 0.8}
>>> pitch_data = {'fundamental_frequency': 440.0, 'pitch_confidence': 0.9}
>>> additional_matches, web_scores = web_scraping_results(tonal_data, pitch_data)
('song1,song2,song3', 0.85)
```

```python
>>> tonal_data = {'tone': 'A Minor', 'tone_confidence': 0.7}
>>> pitch_data = {'fundamental_frequency': 220.0, 'pitch_confidence': 0.8}
>>> additional_matches, web_scores = web_scraping_results(tonal_data, pitch_data)
('songA,songB', 0.78)
```
