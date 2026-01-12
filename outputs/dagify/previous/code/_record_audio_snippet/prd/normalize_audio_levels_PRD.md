# normalize_audio_levels PRD

## Description
Normalizes the levels of the input audio data to a standard format.


## Conceptual Info

This shim node is responsible for adjusting the audio levels of the input data to ensure consistency and compatibility with subsequent processing steps.

## Docstring

### Summary
Normalizes the audio levels of the input audio data.

### Parameters

- **audio_data** (str): The input audio data encoded as a string.

### Returns

str: The normalized audio data encoded as a string.

### Raises

- ValueError: If the input audio data is not in the expected format.
- TypeError: If the input audio data is not of type string.

### Examples

```python
>>> normalized_audio = normalize_audio_levels(audio_data='raw_audio_data')
>>> print(normalized_audio)
'normalized_audio_data'
```

```python
>>> try:
...     normalize_audio_levels(audio_data=123)
>>> except TypeError as e:
...     print(e)
'Input audio data must be of type string.'
```
