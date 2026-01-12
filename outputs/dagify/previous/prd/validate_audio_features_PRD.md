# validate_audio_features PRD

## Description
Normalize and validate extracted features


## Conceptual Info

The node consolidates raw spectral, temporal, and deep‑learning features, normalizes them to a common scale, and flags any inconsistencies or missing values so downstream steps receive clean, consistent inputs.

## Docstring

### Summary
Normalize and validate spectral and temporal features.

### Parameters

- **spectral_centroid** (float): Frequency band center of gravity.
- **spectral_bandwidth** (float): Spread of frequency energy.
- **rolloff_frequency** (float): Frequency cutoff point.
- **zero_crossing_rate** (float): Rate of sign change in the signal.
- **energy** (float): Signal energy measurement.
- **entropy** (float): Signal disorder measurement.
- **cnn_features** (List[float]): Convolutional network outputs.
- **rnn_features** (List[float]): Recurrent network outputs.

### Returns

Tuple[List[float], List[float], List[str]]: A tuple containing the normalized spectral feature list, the normalized temporal feature list, and a list of any validation error messages.

### Raises

- ValueError: Raised if any required input is missing or non‑numeric.
- TypeError: Raised if input types do not match expected primitives.

### Examples

```python
>>> normalized_spectral, normalized_temporal, validation_errors = validate_audio_features(
...     spectral_centroid=4000.0,
...     spectral_bandwidth=1500.0,
...     rolloff_frequency=8000.0,
...     zero_crossing_rate=0.05,
...     energy=0.3,
...     entropy=0.7,
...     cnn_features=[0.2, 0.3, 0.4],
...     rnn_features=[0.1, 0.5]"
                ")
(
  [0.8, 0.3, 1.0],
  [0.05, 0.3, 0.7],
  []
)
```

```python
>>> normalized_spectral, normalized_temporal, validation_errors = validate_audio_features(
...     spectral_centroid=4000.0,
...     spectral_bandwidth=None,
...     rolloff_frequency=8000.0,
...     zero_crossing_rate=0.05,
...     energy=0.3,
...     entropy=0.7,
...     cnn_features=[0.2, 0.3, 0.4],
...     rnn_features=[0.1, 0.5]"
                ")
(
  [0.8, 0.0, 1.0],
  [0.05, 0.3, 0.7],
  ['spectral_bandwidth is None or not numeric']
)
```
