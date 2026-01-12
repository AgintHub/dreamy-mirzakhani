# calculate_duration PRD

## Description
Calculates the duration of an audio snippet from its audio data.


## Conceptual Info

This shim function is designed to calculate the duration of an audio snippet. It takes audio data as input and returns the duration in seconds.

## Docstring

### Summary
Calculates the duration of an audio snippet from its audio data.

### Parameters

- **audio_data** (str): The binary payload of the audio snippet encoded with Opus, represented as a base64 string.

### Returns

float: The duration of the audio snippet in seconds.

### Raises

- ValueError: If the input audio data is invalid or corrupted.
- TypeError: If the input audio data is not a string.

### Examples

```python
>>> audio_data = 'base64_encoded_audio_data'
>>> duration = calculate_duration(audio_data)
>>> print(duration)
3.45
```

```python
>>> invalid_audio_data = 12345
>>> try:
...     calculate_duration(invalid_audio_data)
>>> except TypeError as e:
...     print(e)
Input audio data must be a string.
```
