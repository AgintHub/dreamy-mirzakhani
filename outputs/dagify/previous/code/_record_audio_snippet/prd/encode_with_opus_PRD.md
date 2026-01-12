# encode_with_opus PRD

## Description
Encodes input audio data using the Opus codec.


## Conceptual Info

This shim node is responsible for encoding raw audio data into the Opus format, which is a highly versatile and efficient audio codec suitable for real-time applications.

## Docstring

### Summary
Encodes raw audio data into Opus format.

### Parameters

- **audio_data** (str): The raw audio data to be encoded.

### Returns

str: The encoded audio data in Opus format.

### Raises

- ValueError: If the input audio data is invalid or corrupted.
- TypeError: If the input audio data is not of type str.

### Examples

```python
>>> encoded_data = encode_with_opus(audio_data='raw_audio_data')
'encoded_audio_data'
```

```python
>>> encoded_data = encode_with_opus(audio_data='another_raw_audio_data')
'another_encoded_audio_data'
```
