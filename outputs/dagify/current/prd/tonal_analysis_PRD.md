# tonal_analysis PRD

## Description
Identify tonal characteristics


## Conceptual Info

Transforms MFCC and delta‑MFCC features into a musical key classification and confidence score using a pre‑trained deep‑learning model.

## Docstring

### Summary
Detects the key of an audio snippet from its MFCC representation.

### Parameters

- **mfcc_coefficients** (List[float]): Sequence of mel‑frequency cepstral coefficients extracted from the spectrogram.
- **delta_mfcc** (List[float]): First‑order delta of the MFCC coefficients, indicating the rate of change of the spectral envelope.

### Returns

Tuple[str, float]: A tuple containing the inferred musical key (e.g., "C major") and a confidence value between 0 and 1.

### Raises

- ValueError: Raised if either input list is empty or not of numeric type.

### Examples

```python
>>> tone, conf = tonal_analysis([0.12, 0.34, 0.56, 0.78], [0.02, 0.04, 0.03, 0.01])
('C major', 0.92)
```

```python
>>> tone, conf = tonal_analysis([0.1, 0.2, 0.3], [0.01, 0.02, 0.03])
('G minor', 0.85)
```
