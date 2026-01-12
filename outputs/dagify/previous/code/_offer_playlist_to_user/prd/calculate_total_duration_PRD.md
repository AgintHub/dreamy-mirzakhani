# calculate_total_duration PRD

## Description
Calculates the total duration of a playlist by summing the durations of all tracks.


## Conceptual Info

This shim node is responsible for calculating the total duration of a playlist by aggregating the durations of individual tracks provided in the input.

## Docstring

### Summary
Calculates the total duration of a playlist in seconds by summing the durations of all tracks.

### Parameters

- **track_details** (str): A string containing track details, expected to be in a format that can be parsed to extract track durations.

### Returns

int: The total duration of the playlist in seconds.

### Raises

- ValueError: If the input track details are malformed or cannot be parsed to extract durations.
- TypeError: If the input type is not as expected.

### Examples

```python
>>> track_details = '[{"duration": 180}, {"duration": 240}]'
>>> total_duration = calculate_total_duration(track_details=track_details)
420
```

```python
>>> track_details = '[{"duration": 300}, {"duration": 120}]'
>>> total_duration = calculate_total_duration(track_details=track_details)
420
```
