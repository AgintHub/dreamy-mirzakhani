# extract_temporal_features PRD

## Description
Calculate temporal domain features from raw audio data, returning the zero‑crossing rate, signal energy, entropy, and a list of raw temporal metrics.


## Conceptual Info

This node transforms raw waveform samples into a compact set of descriptive statistics that capture the signal’s time‑domain behaviour.

## Docstring

### Summary
Extracts zero‑crossing rate, energy, and entropy from a raw audio buffer and returns them as a tuple and a consolidated list.

### Parameters

- **audio_data** (str): Base64‑ or hex‑encoded representation of the raw audio samples.
- **sampling_rate** (int): Sampling frequency of the audio in Hertz.
- **file_format** (str): Encoding format of the audio file (e.g., WAV, MP3, FLAC).
- **metadata** (list[str]): Additional metadata extracted by the loader; unused by this function but provided for consistency.

### Returns

tuple[float, float, float, list[float]]: A four‑element tuple containing zero_crossing_rate, energy, entropy, and a list of these three metrics.

### Raises

- ValueError: If audio_data cannot be decoded or is empty.
- TypeError: If sampling_rate is not an integer or less than or equal to zero.

### Examples

```python
>>> # Example 1 – simple 4‑sample waveform encoded as hex
>>> audio_hex = '01020304'
>>> # bytes: 1
>>> 2
>>> 3
>>> 4"
>>> result = extract_temporal_features(audio_hex, 1, 'raw', [])
>>> print(result)
(0.0, 30.0, 0.0, [0.0, 30.0, 0.0])
```

```python
>>> # Example 2 – a sine wave (encoded in base64 for brevity)
>>> import numpy as np, base64
>>> t = np.linspace(0, 1, 44100, endpoint=False)
>>> samples = np.int16(32767 * np.sin(2 * np.pi * 440 * t))
>>> audio_b64 = base64.b64encode(samples.tobytes()).decode('ascii')
>>> result = extract_temporal_features(audio_b64, 44100, 'wav', [])
>>> print(result[0])  # zero crossing rate per second
≈ 880.0
```
