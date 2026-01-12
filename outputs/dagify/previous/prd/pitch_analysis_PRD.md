# pitch_analysis PRD

## Description
Detect pitch characteristics by analyzing the Mel‑Frequency Cepstral Coefficients (MFCCs) and their first‑order deltas to estimate the dominant sinusoid frequency (fundamental_frequency) and the confidence of the detection (pitch_confidence).


## Conceptual Info

The node transforms the spectral envelope representation (MFCCs) into a pitch domain estimate, enabling downstream tasks such as key detection, database searching, and web scraping based on tonal and pitch signatures.

## Docstring

### Summary
Estimate the fundamental frequency and confidence of a pitch from MFCC features.

### Parameters

- **mfcc_coefficients** (List[float]): Sequence of Mel‑Frequency Cepstral Coefficients extracted from a spectrogram. These values capture the spectral envelope of the audio signal.
- **delta_mfcc** (List[float]): First‑order time‑derivative of the MFCC coefficients, representing the rate of change of the spectral envelope.

### Returns

Tuple[float, float]: A tuple containing (fundamental_frequency, pitch_confidence). Both values are floats.

### Raises

- ValueError: Raised if either `mfcc_coefficients` or `delta_mfcc` is empty or contains non‑finite values.
- RuntimeError: Raised if the underlying pitch extraction algorithm fails to converge or encounters numerical instability.

### Examples

```python
>>> mfcc = [12.3, 10.1, 9.8, 8.7, 7.6, 6.5]
>>> delta = [0.5, -0.3, 0.1, -0.2, 0.0, 0.1]
>>> pitch_analysis(mfcc, delta)
(110.2, 0.91)
```

```python
>>> mfcc = [0.0, 0.0, 0.0, 0.0]
>>> delta = [0.0, 0.0, 0.0, 0.0]
>>> pitch_analysis(mfcc, delta)
(0.0, 0.0)
```
