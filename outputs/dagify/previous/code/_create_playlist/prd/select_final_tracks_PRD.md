# select_final_tracks PRD

## Description
Selects final tracks based on ranked tracks and diversity threshold.


## Conceptual Info

This shim function is responsible for selecting the final tracks from a list of ranked tracks based on a specified diversity threshold. It plays a crucial role in generating a playlist by ensuring that the selected tracks meet certain diversity criteria.

## Docstring

### Summary
Selects final tracks from ranked tracks based on a diversity threshold.

### Parameters

- **ranked_tracks** (str): A string representation of a list of track IDs ranked according to their relevance or score.
- **diversity_threshold** (str): A string representation of a float value between 0 and 1 that determines the minimum diversity required among the selected tracks.

### Returns

List[str]: A list of track IDs that have been selected based on the ranked tracks and the diversity threshold.

### Raises

- ValueError: If the diversity threshold is not within the range 0 to 1.
- TypeError: If the input types are incorrect.

### Examples

```python
>>> ranked_tracks = '["track1", "track2", "track3"]'
>>> diversity_threshold = '0.7'
>>> select_final_tracks(ranked_tracks=ranked_tracks, diversity_threshold=diversity_threshold)
['track1', 'track3']
```

```python
>>> ranked_tracks = '["track4", "track5", "track6"]'
>>> diversity_threshold = '0.5'
>>> select_final_tracks(ranked_tracks=ranked_tracks, diversity_threshold=diversity_threshold)
['track4', 'track6']
```
