# validate_audio_features PRD

## Description
Normalizes and validates spectral, temporal, and deep‑learning features extracted from an audio snippet, ensuring numerical consistency and flagging anomalies before downstream processing.


## Conceptual Info

The node acts as a gatekeeper for audio feature streams, standardising numeric ranges and detecting corrupt or anomalous measurements before they propagate to later stages like spectrogram generation or machine‑learning pipelines.

## Docstring

### Summary
Normalizes and validates spectral, temporal, and deep‑learning audio features, ensuring consistency and correcting outliers.

### Parameters

- **spectral_centroid** (float): Center of gravity of the spectral energy distribution (Hz).
- **spectral_bandwidth** (float): Spread of the spectral energy (Hz).
- **rolloff_frequency** (float): Frequency below which a specified percentage (typically 85%) of the spectral energy lies (Hz).
- **zero_crossing_rate** (float): Rate of sign changes in the waveform per second.
- **energy** (float): Sum of squared sample amplitudes (signal power).
- **entropy** (float): Shannon entropy of the amplitude histogram (dimensionless).
- **cnn_features** (List[float]): High‑level spectral pattern vector produced by the CNN branch.
- **rnn_features** (List[float]): High‑level temporal dynamics vector produced by the RNN branch.

### Returns

Tuple[List[float], List[float], List[str]]: A tuple containing the normalized spectral feature list, the normalized temporal feature list, and a list of validation error messages.

### Raises

- ValueError: Raised if any required input is missing or not a numeric type.

### Examples

```python
>>> validate_audio_features(2000.0, 1000.0, 4000.0, 5.0, 1000.0, 0.5, [0.2, 0.3], [0.1, 0.4])
([0.5, 0.4, 0.8], [0.5, 0.4, 0.5], [])
```

```python
>>> validate_audio_features(2000.0, -10.0, 4000.0, 5.0, 1000.0, 0.5, [0.2, 0.3], [0.1, 0.4])
([0.5, 0.0, 0.8], [0.5, 0.4, 0.5], ['spectral_bandwidth outlier corrected: -10.0 -> 0.0'])
```
