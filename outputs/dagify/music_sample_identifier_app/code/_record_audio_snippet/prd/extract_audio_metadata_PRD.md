# extract_audio_metadata PRD

## Description
Extracts metadata information from the given audio data.


## Conceptual Info

This shim function is designed to extract relevant metadata from a given audio data input, playing a crucial role in audio processing pipelines.

## Docstring

### Summary
Extracts metadata from the provided audio data and returns it as a string.

### Parameters

- **audio_data** (str): The input audio data encoded as a string from which metadata will be extracted.

### Returns

str: A string representing the metadata extracted from the audio data.

### Raises

- ValueError: If the input audio data is not in the expected format or is corrupted.
- TypeError: If the input audio data is not a string.

### Examples

```python
>>> audio_data = 'base64_encoded_audio_data'
>>> metadata = extract_audio_metadata(audio_data=audio_data)
'duration: 10s, sample_rate: 44.1kHz, codec: Opus'
```

```python
>>> invalid_audio_data = 12345
>>> extract_audio_metadata(audio_data=invalid_audio_data)
TypeError: Input audio data must be a string.
```
