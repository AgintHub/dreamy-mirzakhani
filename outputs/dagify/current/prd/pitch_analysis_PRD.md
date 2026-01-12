# pitch_analysis PRD

## Description
Detect pitch characteristics


## Conceptual Info

The pitch_analysis node transforms the time‑domain audio signal into a set of pitch‑specific metrics.  It consumes the MFCC representation produced by the preceding mfcc_extraction node and applies a harmonic‑analysis algorithm (typically a combination of autocorrelation, YIN or cepstral‑based pitch‑tracking) to estimate the fundamental frequency (f0) and a confidence score indicating the reliability of that estimate.

## Docstring

### Summary
Estimate the fundamental frequency and pitch confidence from MFCC features.

### Parameters

- **mfcc_coefficients** (List[float]): Temporal MFCC coefficients obtained from the spectrogram.  Each entry corresponds to a short‑time window and contains the mel‑frequency cepstral coefficients for that window.
- **delta_mfcc** (List[float]): Delta (first‑derivative) MFCC coefficients representing the rate of change of the spectral envelope across successive windows.  These are used to improve pitch stability.

### Returns

Tuple[float, float]: A tuple containing the estimated fundamental frequency in hertz and a confidence score between 0.0 and 1.0.

### Raises

- ValueError: Raised if either input list is empty or contains non‑numeric values.
- RuntimeError: Raised if the pitch‑tracking algorithm fails to converge or cannot produce a reliable estimate.

### Examples

```python
>>> mfcc = [0.1, 0.3, 0.2, 0.4, 0.5]
>>> delta = [0.02, 0.03, -0.01, 0.00, 0.04]
>>> f0, conf = pitch_analysis(mfcc, delta)
>>> print(f"f0={f0:.2f} Hz, confidence={conf:.2f}")
f0=220.00 Hz, confidence=0.89
```

```python
>>> f0, conf = pitch_analysis([], [])
>>> print('This line will not execute')
ValueError: Input MFCC lists must contain at least one numeric element.
```
