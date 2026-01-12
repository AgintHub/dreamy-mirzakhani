# extract_spectral_features PRD

## Description
Calculate spectral domain features such as spectral centroid, bandwidth, and rolloff frequency from raw audio samples.


## Conceptual Info

The node transforms raw PCM audio (encoded as a Base64 string) into three core spectral descriptors that summarize the distribution of energy over frequency.

## Docstring

### Summary
Compute spectral centroid, bandwidth, and roll‑off from a Base64‑encoded raw audio signal.

### Parameters

- **audio_data** (str): Base64‑encoded representation of the raw audio samples (IEEE‑754 float32).
- **sampling_rate** (int): Sampling frequency of the audio in Hertz.

### Returns

Dict[str, float]: Dictionary with keys 'spectral_centroid', 'spectral_bandwidth', and 'rolloff_frequency', each mapping to a float value.

### Raises

- ValueError: If `audio_data` is empty or cannot be decoded.
- TypeError: If `sampling_rate` is not an integer or is <= 0.
- RuntimeError: If the FFT computation fails or produces NaNs.

### Examples

```python
>>> import base64, numpy as np
>>> fs = 8000
>>> t = np.arange(0, 1, 1/fs)
>>> s = 0.5 * np.sin(2 * np.pi * 440 * t)
>>> audio_bytes = s.astype(np.float32).tobytes()
>>> audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
>>> result = extract_spectral_features(audio_b64, fs)
{'spectral_centroid': 440.0, 'spectral_bandwidth': 0.0, 'rolloff_frequency': 220.0}
```

```python
>>> import base64, numpy as np
>>> fs = 8000
>>> t = np.arange(0, 1, 1/fs)
>>> s = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.05 * np.random.randn(len(t))
>>> audio_bytes = s.astype(np.float32).tobytes()
>>> audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
>>> result = extract_spectral_features(audio_b64, fs)
{'spectral_centroid': 448.3, 'spectral_bandwidth': 50.7, 'rolloff_frequency': 350.1}
```
