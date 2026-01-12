# music_database_api PRD

## Description
Query an external music database to find tracks that match the provided tonal and pitch characteristics.


## Conceptual Info

This node performs an external lookup of tracks that best match the tonal key and fundamental pitch detected from an audio snippet.  It serves as the bridge between low‑level audio analysis and high‑level music metadata retrieval, feeding subsequent nodes that assemble artist links and render the final HTML.

## Docstring

### Summary
Query an external music database for songs matching a given musical key and pitch.

### Parameters

- **tone** (str): Identified musical key (e.g., 'C major', 'A minor').
- **fundamental_frequency** (float): Estimated fundamental frequency in hertz.

### Returns

Tuple[List[str], List[float]]: A tuple where the first element is a list of matched song titles and the second element is a list of corresponding relevance scores.

### Raises

- ValueError: If either `tone` or `fundamental_frequency` is missing or empty.
- ConnectionError: If the external music database API cannot be reached.

### Examples

```python
>>> matches, scores = music_database_api('C major', 440.0)
(['Song A', 'Song B'], [0.95, 0.88])
```

```python
>>> try:
...     music_database_api('', 440.0)
>>> except ValueError as e:
...     print(e)
"tone is required and cannot be empty."
```
