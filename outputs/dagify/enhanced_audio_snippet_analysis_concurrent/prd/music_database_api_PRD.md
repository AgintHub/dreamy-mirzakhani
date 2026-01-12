# music_database_api PRD

## Description
Query an external music database to find tracks that match the provided tonal and pitch characteristics.


## Conceptual Info

This node queries an external music database to find tracks that match the provided tonal and pitch characteristics, returning a list of matching song titles along with their relevance scores.

## Docstring

### Summary
Searches a music database for tracks matching the given tonal and pitch characteristics.

### Parameters

- **tone** (str): Identified musical key from tonal analysis.
- **tone_confidence** (float): Tonal detection reliability score between 0.0 and 1.0.
- **fundamental_frequency** (float): Primary pitch frequency in Hertz. Zero indicates no reliable pitch detected.
- **pitch_confidence** (float): Reliability score of the pitch estimate, ranging from 0.0 (unreliable) to 1.0 (highly reliable).

### Returns

Tuple[List[str], List[float]]: A tuple containing a list of song titles that match the query and a corresponding list of relevance scores indicating the quality of each match.

### Raises

- ValueError: If the input parameters are invalid or out of expected ranges.
- ConnectionError: If there's a failure connecting to the external music database.

### Examples

```python
>>> tone = 'C Major'
>>> tone_confidence = 0.9
>>> fundamental_frequency = 440.0
>>> pitch_confidence = 0.95
>>> song_matches, relevance_scores = music_database_api(tone, tone_confidence, fundamental_frequency, pitch_confidence)
song_matches = ['Song 1', 'Song 2'], relevance_scores = [0.85, 0.78]
```

```python
>>> tone = 'A Minor'
>>> tone_confidence = 0.8
>>> fundamental_frequency = 220.0
>>> pitch_confidence = 0.9
>>> song_matches, relevance_scores = music_database_api(tone, tone_confidence, fundamental_frequency, pitch_confidence)
song_matches = ['Song 3', 'Song 4'], relevance_scores = [0.82, 0.75]
```
