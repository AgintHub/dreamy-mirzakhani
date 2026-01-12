# mfcc_extraction PRD

## Description
Calculate mel-frequency cepstral coefficients


## Conceptual Info

This node transforms a time‑frequency spectrogram into a compact representation suitable for audio analysis and machine‑learning pipelines. It computes Mel‑frequency cepstral coefficients (MFCCs) and their first‑order derivatives (delta MFCCs) which capture perceptual spectral envelopes and temporal dynamics of the signal.

## Docstring

### Summary
Convert a spectrogram into MFCCs and delta MFCCs.

### Parameters

- **spectrogram_data** (List[float]): 1‑D flattened array representing the magnitude of the short‑time Fourier transform. The array is expected to be in the same shape produced by the spectrogram_creation node.

### Returns

Tuple[List[float], List[float]]: A tuple containing: (mfcc_coefficients, delta_mfcc). Both are 1‑D lists of floats where each element corresponds to a time frame.

### Raises

- ValueError: Raised if spectrogram_data is empty or not a list.
- RuntimeError: Raised if the internal MFCC transform fails (e.g., due to insufficient data length).

### Examples

```python
>>> # A minimal 3‑frame spectrogram (flattened)
>>> spectrogram = [0.10, 0.20, 0.30,
...                0.40, 0.50, 0.60,
...                0.70, 0.80, 0.90]
>>> # Compute MFCCs
>>> mfcc, delta = mfcc_extraction(spectrogram)
>>> print(mfcc)
>>> print(delta)
['0.12', '0.23', '0.34']
['0.01', '-0.02', '0.00']
```

```python
>>> # Invalid input triggers error
>>> try:
...     mfcc_extraction([])
>>> except ValueError as e:
...     print(e)
"spectrogram_data must be a non‑empty list of floats"
```
