# mfcc_extraction PRD

## Description
Calculate mel-frequency cepstral coefficients (MFCCs) from a spectrogram and compute the first‑order delta of those coefficients.


## Conceptual Info

The MFCC extraction node transforms a flat spectrogram into a compact representation of the audio's spectral envelope (MFCCs) and calculates the first‑order derivative (delta) to capture dynamic changes over time.

## Docstring

### Summary
Transforms a spectrogram into Mel‑Frequency Cepstral Coefficients (MFCCs) and their first‑order delta.

### Parameters

- **spectrogram_data** (list[float]): A one‑dimensional list of floating‑point values representing a time‑frequency spectrogram flattened from a 2‑D matrix.

### Returns

tuple[list[float], list[float]]: A tuple containing:
- `mfcc_coefficients`: list of MFCC values per frame.
- `delta_mfcc`: list of first‑order differences (deltas) of the MFCCs.

### Raises

- ValueError: Raised when `spectrogram_data` is empty, not a list, or contains non‑numeric entries.

### Examples

```python
>>> spectrogram = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
>>> mfcc, delta = mfcc_extraction(spectrogram)
>>> print('MFCC:', mfcc)
>>> print('Delta:', delta)
MFCC: [0.15, 0.35, 0.55]
Delta: [0.2, 0.2]
```

```python
>>> mfcc, delta = mfcc_extraction([0.1, 0.2, 0.3])
>>> print(mfcc, delta)
[0.15, 0.25] [0.1]
```
