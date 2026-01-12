# extract_temporal_features PRD

## Description
Calculate temporal domain features from raw audio data, returning the zero‑crossing rate, signal energy, entropy, and a list of raw temporal metrics.


## Conceptual Info

Computes time‑domain descriptors from raw audio samples, providing insight into waveform complexity and power.

## Docstring

### Summary
Extract key temporal metrics (zero‑crossing rate, energy, entropy) from raw audio samples.

### Parameters

- **audio_data** (str): Raw audio samples typically returned by `load_audio_snippet`. The function expects a contiguous sequence of PCM sample values encoded as a string or byte array.
- **sampling_rate** (int): Sampling rate (samples per second) of the audio data, used to convert raw counts into time‑based rates.
- **metadata** (list[str] | None): Optional list of metadata strings from `load_audio_snippet`. Ignored by the function but accepted for API consistency.

### Returns

dict: Dictionary containing the computed temporal features:

```python
{
    "zero_crossing_rate": float,
    "energy": float,
    "entropy": float,
    "temporal_features": List[float],
}
```

### Raises

- ValueError: If `audio_data` is empty or contains no valid samples.
- TypeError: If inputs are of incompatible types (e.g., non‑numeric samples).

### Examples

```python
>>> # Example 1: Simple 5‑sample signal
>>> audio_data = "\x00\x01\x00\xff\x00"  # 0, 1, 0, -1, 0 (little‑endian bytes)
>>> sampling_rate = 1
>>> features = extract_temporal_features(audio_data, sampling_rate)
>>> print(features)
{'zero_crossing_rate': 2.0, 'energy': 2.0, 'entropy': 1.0, 'temporal_features': [2.0, 2.0, 1.0]}
```

```python
>>> # Example 2: Silence – zero energy and entropy
>>> audio_data = "\x00\x00\x00\x00"  # four zero samples
>>> sampling_rate = 4
>>> features = extract_temporal_features(audio_data, sampling_rate)
>>> print(features)
{'zero_crossing_rate': 0.0, 'energy': 0.0, 'entropy': 0.0, 'temporal_features': [0.0, 0.0, 0.0]}
```
