# extract_spectral_features PRD

## Description
Calculate spectral domain features


## Conceptual Info

Computes key spectral metrics (centroid, bandwidth, roll‑off) from raw audio samples using FFT‑based analysis.

## Docstring

### Summary
Computes spectral features from raw audio samples.

### Parameters

- **audio_data** (str): Raw audio samples as a string or byte buffer.
- **sampling_rate** (int): Sampling rate (samples per second) of the audio signal.

### Returns

dict: Dictionary with keys 'spectral_centroid', 'spectral_bandwidth', and 'rolloff_frequency', each a float representing the computed metric.

### Raises

- ValueError: Raised when `audio_data` is empty or contains no valid samples.
- TypeError: Raised when `sampling_rate` is not a positive integer.

### Examples

```python
>>> result = extract_spectral_features(audio_data=b'\x00\x01\x02...', sampling_rate=44100)
>>> print(result['spectral_centroid'])
2500.0
```

```python
>>> result = extract_spectral_features(audio_data=b'\x00\x00\x00...', sampling_rate=48000)
>>> print(result['rolloff_frequency'])
12000.0
```
