# mfcc_extraction PRD

## Description
Calculate mel-frequency cepstral coefficients (MFCCs) from a spectrogram and compute the first‑order delta of those coefficients.


## Conceptual Info

The MFCC extraction node transforms a flat spectrogram into a compact spectral descriptor by applying a Mel filterbank, logarithm, and discrete cosine transform (DCT). It then calculates the temporal derivative (delta) of the resulting coefficients.

## Docstring

### Summary
Extracts MFCC coefficients and their delta from a flattened spectrogram.

### Parameters

- **spectrogram_data** (List[float]): Flat list of magnitude values from an STFT (time‑frequency matrix flattened into one dimension).

### Returns

Dict[str, float]: A dictionary with two entries:

* ``mfcc_coefficients`` – the mean MFCC value over all time frames.
* ``delta_mfcc`` – the mean delta MFCC value over all time frames.

### Raises

- ValueError: Raised if ``spectrogram_data`` is empty or not a list.

### Examples

```python
>>> mfcc_extraction([0.1, 0.2, 0.15, 0.3, 0.25, 0.35])
{'mfcc_coefficients': 0.208, 'delta_mfcc': 0.013}
```

```python
>>> mfcc_extraction([])
ValueError: Input spectrogram_data must be a non‑empty list of floats.
```
