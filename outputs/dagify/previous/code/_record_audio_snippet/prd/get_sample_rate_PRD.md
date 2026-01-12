# get_sample_rate PRD

## Description
Extracts the sample rate from the provided audio data.


## Conceptual Info

This shim function is designed to extract the sample rate from a given audio data input, playing a crucial role in audio processing pipelines by providing essential metadata for further processing or analysis.

## Docstring

### Summary
Extracts the sample rate from the provided audio data.

### Parameters

- **audio_data** (str): The input audio data encoded as a string from which the sample rate will be extracted.

### Returns

int: The sample rate of the audio data in Hz, represented as an integer.

### Raises

- ValueError: If the input audio data is not in the expected format or is corrupted.
- TypeError: If the input audio data is not of type string.

### Examples

```python
>>> get_sample_rate(audio_data='encoded_audio_string')
48000
```

```python
>>> get_sample_rate(audio_data='another_encoded_audio_string')
44100
```
