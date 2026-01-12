# extract_spectral_features PRD

## Description
Calculate spectral domain features


## Conceptual Info

Extracts key spectral attributes from raw audio, such as centroid, bandwidth, and rolloff frequency, which are critical for timbral analysis and downstream processing.

## Docstring

### Summary
Computes spectral domain features from raw audio samples using FFT.

### Parameters

- **audio_data** (str): Raw audio samples encoded as a byte string or base64 string.
- **sampling_rate** (int): Sampling rate in Hz of the audio data.
- **file_format** (str): Encoding format of the audio file (e.g., 'wav', 'mp3').
- **metadata** (List[str]): Additional signal characteristics extracted during audio loading.

### Returns

Dict[str, float]: Dictionary with keys 'spectral_centroid', 'spectral_bandwidth', and 'rolloff_frequency'.

### Raises

- ValueError: If audio_data is empty or sampling_rate <= 0.
- RuntimeError: If the FFT computation fails or the audio data cannot be parsed.

### Examples

```python
>>> audio_data = 'raw_bytes_placeholder'
>>> sampling_rate = 44100
>>> features = extract_spectral_features(audio_data, sampling_rate, 'wav', ['sample'])
{'spectral_centroid': 2500.0, 'spectral_bandwidth': 4000.0, 'rolloff_frequency': 7500.0}
```

```python
>>> audio_data = 'empty'
>>> sampling_rate = 8000
>>> try:
...     extract_spectral_features(audio_data, sampling_rate, 'wav', [])
>>> except ValueError as e:
...     print(e)
'audio_data must not be empty or invalid'
```
