# extract_temporal_features PRD

## Description
Calculate temporal domain features from raw audio data, returning the zero‑crossing rate, signal energy, entropy, and a list of raw temporal metrics.


## Conceptual Info

This node extracts temporal features from raw audio data, providing insights into the signal's time-domain characteristics.

## Docstring

### Summary
Extract temporal domain features from raw audio data.

### Parameters

- **audio_data** (str): Base64-encoded representation of the raw audio samples.
- **sampling_rate** (int): Sampling frequency of the audio in Hertz.

### Returns

Tuple[float, float, float, List[float]]: Contains zero_crossing_rate, energy, entropy, and a list of raw temporal metrics.

### Raises

- ValueError: If audio_data is empty or sampling_rate is non-positive.

### Examples

```python
>>> audio_data = 'base64_encoded_audio_data'
>>> sampling_rate = 44100
>>> zero_crossing_rate, energy, entropy, temporal_features = extract_temporal_features(audio_data, sampling_rate)
(0.5, 0.8, 0.2, [0.5, 0.8, 0.2])
```
