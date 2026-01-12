# calculate_segment_timing PRD

## Description
Calculates the start and end times of a matched audio segment within a given audio duration.


## Conceptual Info

This shim node calculates the timing of a matched audio segment within a given audio duration, providing start and end times as output.

## Docstring

### Summary
Calculates the start and end times of a matched audio segment based on the match information and audio duration.

### Parameters

- **match** (str): A string containing information about the matched audio segment, expected to be in a JSON format with relevant details.
- **audio_duration** (str): A string representing the total duration of the audio in seconds.

### Returns

str: A JSON string containing the start and end times of the matched audio segment, with keys 'start_time' and 'end_time'.

### Raises

- ValueError: When the input 'match' or 'audio_duration' is not in the expected format or contains invalid values.
- TypeError: When the input types are not as expected (e.g., 'match' is not a string, 'audio_duration' is not a numeric string).

### Examples

```python
>>> import json
>>> match_info = json.dumps({'track_id': '123', 'start_time': 10.0, 'end_time': 20.0})
>>> audio_duration = '30.0'
>>> result = calculate_segment_timing(match=match_info, audio_duration=audio_duration)
"{'start_time': 10.0, 'end_time': 20.0}"
```

```python
>>> match_info = json.dumps({'track_id': '456', 'start_time': 5.0, 'end_time': 15.0})
>>> audio_duration = '25.0'
>>> result = calculate_segment_timing(match=match_info, audio_duration=audio_duration)
"{'start_time': 5.0, 'end_time': 15.0}"
```
