# extract_spectral_features PRD

## Description
Calculate spectral domain features such as spectral centroid, bandwidth, and rolloff frequency from raw audio samples.


## Conceptual Info

This node extracts key spectral features from raw audio data, enabling analysis of frequency domain characteristics.

## Docstring

### Summary
Calculates spectral centroid, bandwidth, and rolloff frequency from raw audio samples using FFT and spectral analysis.

### Parameters

- **audio_data** (str): Base64-encoded representation of raw audio samples from load_audio_snippet
- **sampling_rate** (int): Sampling frequency of the audio in Hertz from load_audio_snippet

### Returns

tuple[float, float, float]: Contains spectral_centroid, spectral_bandwidth, and rolloff_frequency representing different aspects of the audio's frequency domain characteristics.

### Raises

- ValueError: If audio_data is empty or sampling_rate is non-positive.
- TypeError: If audio_data is not a string or sampling_rate is not an integer.

### Examples

```python
>>> audio_data = 'base64_encoded_audio_data'
>>> sampling_rate = 44100
>>> spectral_centroid, spectral_bandwidth, rolloff_frequency = extract_spectral_features(audio_data, sampling_rate)
(450.0, 200.0, 800.0)
```

```python
>>> invalid_audio_data = ''
>>> sampling_rate = 0
>>> extract_spectral_features(invalid_audio_data, sampling_rate)
ValueError: Audio data cannot be empty and sampling rate must be positive.
```
