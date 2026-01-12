# extract_spectral_features PRD

## Description
Calculate spectral domain features such as spectral centroid, bandwidth, and rolloff frequency from raw audio samples.


## Conceptual Info

Computes key spectral descriptors that summarize the frequency distribution of an audio snippet, enabling downstream tasks like classification or similarity assessment.

## Docstring

### Summary
Computes spectral features from raw audio samples.

### Parameters

- **audio_data** (str): Base64-encoded (or hex) representation of raw PCM audio samples.
- **sampling_rate** (int): Sample rate of the audio in Hz.
- **file_format** (str): Audio file encoding format (e.g., WAV, MP3, FLAC). Optional; used for logging.

### Returns

dict: Dictionary containing spectral_centroid, spectral_bandwidth, and rolloff_frequency as floats.

### Raises

- ValueError: Raised if audio_data is empty or cannot be decoded.
- RuntimeError: Raised if FFT computation fails.

### Examples

```python
>>> audio_b64 = 'dGhpcyBpcyBhIHNhbXBsZSBhdmFpbGFibGUgd2F5'
>>> features = extract_spectral_features(audio_b64, 44100, 'WAV')
{'spectral_centroid': 2150.3, 'spectral_bandwidth': 180.7, 'rolloff_frequency': 3600.1}
```

```python
>>> # Using a short sine wave snippet (encoded manually for illustration)
>>> audio_b64 = 'AAECAwQFBgcICQoLDA0ODxAREhM='
>>> features = extract_spectral_features(audio_b64, 8000, 'WAV')
{'spectral_centroid': 2000.0, 'spectral_bandwidth': 0.0, 'rolloff_frequency': 4000.0}
```
