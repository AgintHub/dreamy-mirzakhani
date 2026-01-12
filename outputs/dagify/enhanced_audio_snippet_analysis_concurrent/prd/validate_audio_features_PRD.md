# validate_audio_features PRD

## Description
Normalize and validate extracted features


## Conceptual Info

Normalizes and validates audio features before downstream processing, ensuring consistent scales and logging any discrepancies.

## Docstring

### Summary
Normalizes spectral and temporal audio features to a common scale, verifies consistency, and records validation errors.

### Parameters

- **spectral_centroid** (float): Spectral centroid value extracted from the audio signal.
- **spectral_bandwidth** (float): Spectral bandwidth value extracted from the audio signal.
- **rolloff_frequency** (float): Rolloff frequency value extracted from the audio signal.
- **zero_crossing_rate** (float): Zero‑crossing rate of the audio waveform.
- **energy** (float): Signal energy computed from squared amplitudes.
- **entropy** (float): Shannon entropy of the amplitude histogram.

### Returns

Tuple[List[float], List[float], List[str]]: A tuple containing a list of normalized spectral features, a list of normalized temporal features, and a list of validation error messages.

### Raises

- ValueError: If any input is None or not a real number.

### Examples

```python
>>> spectral_centroid = 4000.0
>>> spectral_bandwidth = 500.0
>>> rolloff_frequency = 2000.0
>>> zero_crossing_rate = 30.0
>>> energy = 0.02
>>> entropy = 1.2
>>> norm_spectral, norm_temporal, errors = validate_audio_features(

...     spectral_centroid,

...     spectral_bandwidth,

...     rolloff_frequency,

...     zero_crossing_rate,

...     energy,

...     entropy

>>> )
"norm_spectral = [1.0, 0.0, 0.4286],\n" +
"norm_temporal = [1.0, 0.0, 0.0399],\n" +
"errors = []"
```

```python
>>> # Example that triggers a validation error
>>> try:
...     validate_audio_features(None, 500, 2000, 30, 0.02, 1.2)
>>> except ValueError as e:
...     print(e)
"One or more inputs is not a valid float."
```
