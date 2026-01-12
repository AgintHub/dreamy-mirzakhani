# extract_temporal_features PRD

## Description
Calculate temporal domain features from raw audio data, returning the zero‑crossing rate, signal energy, entropy, and a list of raw temporal metrics.


## Conceptual Info

The node extracts key temporal characteristics from raw audio samples, providing foundational metrics for subsequent validation and analysis.

## Docstring

### Summary
Extracts temporal domain features from an audio snippet.

### Parameters

- **audio_data** (str): Base64‑encoded raw audio samples as produced by `load_audio_snippet`.
- **sampling_rate** (int): Sampling frequency of the audio in Hertz, required to convert zero‑crossing counts to a per‑second rate.

### Returns

Tuple[float, float, float, List[float]]: A 4‑tuple containing zero_crossing_rate, energy, entropy, and a list of the three raw metrics.

### Raises

- ValueError: Raised if `audio_data` is empty, cannot be decoded, or if `sampling_rate` is non‑positive.
- RuntimeError: Raised if internal decoding or calculation fails.

### Examples

```python
>>> # Example 1: Simple 4‑sample waveform (1, -1, 1, -1) encoded in base64
>>> import base64
>>> raw_samples = bytes([1, 255, 1, 255])  # 255 interpreted as -1 in signed 8‑bit
>>> b64_audio = base64.b64encode(raw_samples).decode('ascii')
>>> zcr, energy, entropy, feats = extract_temporal_features(b64_audio, 2)
>>> print(zcr, energy, entropy, feats)
1.5 4.0 0.0 [1.5, 4.0, 0.0]
```

```python
>>> # Example 2: Realistic audio snippet (placeholder base64 string)
>>> b64_audio = 'U29tZSBwcm9kdWN0ZWRvbmUgYXR0YWNobWVudA=='
>>> zcr, energy, entropy, feats = extract_temporal_features(b64_audio, 44100)
>>> print(zcr, energy, entropy, feats)
0.021 1234.5 1.23 [0.021, 1234.5, 1.23]
```
