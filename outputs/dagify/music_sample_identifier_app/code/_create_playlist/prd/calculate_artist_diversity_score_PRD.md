# calculate_artist_diversity_score PRD

## Description
Calculates a score representing the diversity of artists in a given list of track IDs.


## Conceptual Info

This shim calculates the artist diversity score for a playlist based on the track IDs provided. It plays a crucial role in evaluating the variety of artists represented in the playlist.

## Docstring

### Summary
Calculates the artist diversity score for a given list of track IDs.

### Parameters

- **track_ids** (str): A string containing the list of track IDs separated by commas or another delimiter.

### Returns

float: A float value between 0 and 1 representing the diversity score of artists in the given track IDs.

### Raises

- ValueError: If the input track_ids string is empty or not properly formatted.
- TypeError: If the input track_ids is not a string.

### Examples

```python
>>> calculate_artist_diversity_score(track_ids='track1,track2,track3')
0.85
```

```python
>>> calculate_artist_diversity_score(track_ids='track4,track5')
0.7
```
