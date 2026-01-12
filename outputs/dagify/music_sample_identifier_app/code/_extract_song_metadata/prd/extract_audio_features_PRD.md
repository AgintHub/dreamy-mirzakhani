# extract_audio_features PRD

## Description
Extracts audio features from a given track segment defined by start and end times.


## Conceptual Info

This shim node is responsible for extracting relevant audio features from a specified segment of an audio track. It plays a crucial role in music analysis and metadata extraction pipelines.

## Docstring

### Summary
Extracts audio features from a specified track segment.

### Parameters

- **track_id** (str): Unique identifier for the audio track.
- **start_time** (str): Start time of the segment in seconds.
- **end_time** (str): End time of the segment in seconds.

### Returns

str: A JSON string representing a dictionary of extracted audio features, including tempo, key, and loudness.

### Raises

- ValueError: If the track_id is invalid, or if start_time is greater than end_time.
- TypeError: If the input parameters are not of the expected type.

### Examples

```python
>>> extract_audio_features(track_id='TR12345', start_time='0.0', end_time='30.0')
{"tempo": 120.0, "key": "C major", "loudness": -6.0}
```

```python
>>> extract_audio_features(track_id='TR67890', start_time='10.5', end_time='40.5')
{"tempo": 128.0, "key": "G minor", "loudness": -3.0}
```
