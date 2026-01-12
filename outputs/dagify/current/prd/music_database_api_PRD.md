# music_database_api PRD

## Description
Query an external music database to find tracks that match the provided tonal and pitch characteristics.


## Conceptual Info

The node takes key tonal and pitch descriptors produced by audio analysis and uses them to query a music database, returning the most relevant song titles along with a confidence metric for each result.

## Docstring

### Summary
Search a music database for tracks that match given tonal and pitch characteristics.

### Parameters

- **tone** (str): Identified musical key (e.g., 'C Major', 'A Minor').
- **tone_confidence** (float): Confidence score of the tonal detection, ranging from 0.0 to 1.0.
- **fundamental_frequency** (float): Estimated fundamental frequency (Hz) of the audio snippet.
- **pitch_confidence** (float): Confidence score of the pitch detection, ranging from 0.0 to 1.0.

### Returns

Tuple[List[str], List[float]]: A tuple where the first element is a list of matched song titles and the second element is a list of relevance scores corresponding to each title.

### Raises

- ValueError: If any of the input parameters are missing or have invalid types.
- RuntimeError: If the external music database API is unreachable or returns an error.

### Examples

```python
>>> song_matches, relevance_scores = music_database_api(
...     tone='C Major',
...     tone_confidence=0.95,
...     fundamental_frequency=261.63,
...     pitch_confidence=0.92)
>>> print(song_matches)
>>> print(relevance_scores)
["Let It Be", "Here Comes the Sun", "Can't Help Falling in Love"]\n[0.87, 0.82, 0.79]
```

```python
>>> song_matches, relevance_scores = music_database_api(
...     tone='A Minor',
...     tone_confidence=0.88,
...     fundamental_frequency=220.00,
...     pitch_confidence=0.85)
>>> print(len(song_matches))
>>> print(relevance_scores[0])
5\n0.91
```
