# tonal_analysis PRD

## Description
Identify tonal characteristics


## Conceptual Info

The tonal_analysis node uses a deep‑learning model trained on MFCC representations to infer the dominant musical key of an audio snippet. It outputs the key name and a confidence score reflecting the model’s certainty.

## Docstring

### Summary
Detects the musical key from MFCC inputs using a pretrained deep learning model.

### Parameters

- **mfcc_coefficients** (float): Mel‑frequency cepstral coefficient features extracted from the audio snippet.
- **delta_mfcc** (float): First‑order differences of the MFCCs, capturing temporal dynamics.

### Returns

Tuple[str, float]: A tuple containing the detected key (`tone`) and a confidence value (`tone_confidence`).

### Raises

- ValueError: If either `mfcc_coefficients` or `delta_mfcc` is None or NaN.
- RuntimeError: If the deep‑learning inference engine fails or the model file is missing.

### Examples

```python
>>> tone, conf = tonal_analysis(0.58, 0.12)
>>> print(f"Key: {tone}, Confidence: {conf:.2f}")
"Key: C Major, Confidence: 0.93"
```

```python
>>> tone, conf = tonal_analysis(0.42, -0.03)
>>> print(tone, conf)
"F Minor 0.76"
```
