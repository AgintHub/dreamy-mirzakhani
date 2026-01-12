# music_database_api PRD

## Description
Query an external music database to find tracks that match the provided tonal and pitch characteristics.


## Conceptual Info

The node interfaces with an external music database service, using the tonal key and fundamental frequency extracted from an audio snippet to retrieve a ranked list of potential matches. It serves as the bridge between low‑level acoustic analysis and high‑level music information retrieval.

## Docstring

### Summary
Query an external music database to find tracks matching the specified key and pitch.

### Parameters

- **tone** (str): Identified musical key (e.g., 'C major', 'A minor') produced by tonal_analysis.
- **tone_confidence** (float): Reliability of the key detection, ranging from 0.0 to 1.0.
- **fundamental_frequency** (float): Primary pitch frequency in Hz extracted by pitch_analysis.
- **pitch_confidence** (float): Reliability of the pitch detection, ranging from 0.0 to 1.0.

### Returns

Tuple[List[str], List[float]]: A two‑element tuple where the first element is a list of matched song titles and the second is a list of relevance scores aligned with those titles.

### Raises

- ValueError: Raised if either confidence value is below 0.5, indicating unreliable input features.
- ConnectionError: Raised if the external database service is unreachable or returns an error.

### Examples

```python
>>> song_matches, relevance_scores = music_database_api('C major', 0.92, 440.0, 0.88)
(['Song A', 'Song B', 'Song C'], [0.95, 0.87, 0.80])
```

```python
>>> try:
...     music_database_api('D minor', 0.45, 392.0, 0.90)
>>> except ValueError as e:
...     print(e)
"Confidence too low: key detection confidence is 0.45"
```
