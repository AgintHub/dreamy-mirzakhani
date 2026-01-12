# generate_audio_fingerprint PRD

## Description
Generates a unique audio fingerprint from a given base64-encoded audio and its sample rate.


## Conceptual Info

This shim generates a unique identifier (fingerprint) for an audio sample, which can be used for identification purposes in music recognition tasks.

## Docstring

### Summary
Generates an audio fingerprint from base64-encoded audio data and its sample rate.

### Parameters

- **audio_base64** (str): Base64-encoded binary payload of the audio data.
- **sample_rate** (str): Sampling rate of the audio in Hertz.

### Returns

str: The generated audio fingerprint as a string.

### Raises

- ValueError: If the input audio_base64 is not a valid base64-encoded string or if sample_rate is not a positive integer.
- TypeError: If the input types are incorrect (e.g., audio_base64 is not str or sample_rate is not str representing an integer).

### Examples

```python
>>> generate_audio_fingerprint(audio_base64='SGVsbG8gd29ybGQ=', sample_rate='44100')
'audio_fingerprint_example'
```

```python
>>> generate_audio_fingerprint(audio_base64='QmFzZTY0IGVuY29kZWQ=', sample_rate='48000')
'another_audio_fingerprint'
```
