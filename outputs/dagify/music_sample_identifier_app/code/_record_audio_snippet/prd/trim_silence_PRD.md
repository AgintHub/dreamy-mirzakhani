# trim_silence PRD

## Description
Removes silence from the beginning and end of an audio signal.


## Conceptual Info

This shim function is designed to remove silence from the beginning and end of an audio signal, improving the quality of the audio for further processing or analysis.

## Docstring

### Summary
Trim silence from the beginning and end of an audio signal represented as a string.

### Parameters

- **audio_data** (str): The input audio data encoded as a string.

### Returns

str: The audio data with silence removed from the start and end.

### Raises

- ValueError: If the input audio data is empty or not properly encoded.
- TypeError: If the input audio data is not of type string.

### Examples

```python
>>> audio_data = 'encoded_audio_string'
>>> trimmed_audio = trim_silence(audio_data=audio_data)
'trimmed_encoded_audio_string'
```

```python
>>> invalid_audio_data = ''
>>> try:
...     trim_silence(audio_data=invalid_audio_data)
>>> except ValueError as e:
...     print(e)
'Input audio data is empty'
```
