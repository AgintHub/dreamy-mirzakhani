# validate_audio_features PRD

## Description
Normalizes and validates spectral, temporal, and deep‑learning features extracted from an audio snippet, ensuring numerical consistency and flagging anomalies before downstream processing.


## Conceptual Info

The node validates and normalizes audio feature vectors to provide a clean, consistent input set for spectrogram generation and downstream analytics.

## Docstring

### Summary
Validate and normalize audio features extracted from an audio snippet.

### Parameters

- **spectral_centroid** (float): Frequency band center of gravity.
- **spectral_bandwidth** (float): Spread of frequency energy.
- **rolloff_frequency** (float): Frequency cutoff point.
- **zero_crossing_rate** (float): Rate of sign changes in the audio waveform per second.
- **energy** (float): Sum of squared sample amplitudes, representing signal power.
- **entropy** (float): Shannon entropy of the amplitude histogram.
- **cnn_features** (float): Convolutional network output summarizing learned spectral patterns.
- **rnn_features** (float): Recurrent network output summarizing learned temporal dynamics.

### Returns

Dict[str, List[float] | List[str]]: Dictionary with keys 'normalized_spectral', 'normalized_temporal', and 'validation_errors'.

### Raises

- ValueError: Raised if any required feature is missing or NaN.
- TypeError: Raised if input types are not float.

### Examples

```python
>>> validate_audio_features(
...     spectral_centroid=1200.0,
...     spectral_bandwidth=300.0,
...     rolloff_frequency=8000.0,
...     zero_crossing_rate=0.05,
...     energy=5000.0,
...     entropy=2.3,
...     cnn_features=0.85,
...     rnn_features=0.65)
>>> )
{'normalized_spectral': [0.0, 0.2, 0.8], 'normalized_temporal': [0.05, 0.5, 0.7], 'validation_errors': []}
```

```python
>>> validate_audio_features(
...     spectral_centroid=99999.0,  # unrealistic outlier
...     spectral_bandwidth=300.0,
...     rolloff_frequency=8000.0,
...     zero_crossing_rate=0.05,
...     energy=5000.0,
...     entropy=2.3,
...     cnn_features=0.85,
...     rnn_features=0.65)
>>> )
{'normalized_spectral': [1.0, 0.2, 0.8], 'normalized_temporal': [0.05, 0.5, 0.7], 'validation_errors': ['spectral_centroid out of expected range, clipped to 1.0']}
```
