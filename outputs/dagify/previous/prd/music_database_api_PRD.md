# music_database_api PRD

## Description
Query an external music database to find tracks that match the provided tonal and pitch characteristics.


## Conceptual Info

The node acts as a bridge between low‑level audio analysis (tonal and pitch) and high‑level semantic information by querying a music database to retrieve candidate tracks.

## Docstring

### Summary
Queries a music database using tonal and pitch information and returns candidate song titles with relevance scores.

### Parameters

- **tone** (str): Identified musical key from tonal_analysis.
- **tone_confidence** (float): Confidence value (0‑1) for the identified key.
- **fundamental_frequency** (float): Fundamental pitch frequency in Hz from pitch_analysis.
- **pitch_confidence** (float): Confidence value (0‑1) for the pitch estimation.

### Returns

Tuple[List[str], List[float]]: A tuple containing a list of matching song titles and a parallel list of relevance scores.

### Raises

- ValueError: Raised if any confidence input is outside the range [0, 1] or if tone is empty.
- RuntimeError: Raised if the external database query fails or times out.

### Examples

```python
>>> matches, scores = music_database_api('C', 0.95, 440.0, 0.90)
(['Song A', 'Song B'], [0.98, 0.92])
```

```python
>>> matches, scores = music_database_api('G', 0.60, 220.0, 0.50)
([], [])
```
