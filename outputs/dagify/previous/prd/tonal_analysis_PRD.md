# tonal_analysis PRD

## Description
Identify tonal characteristics


## Conceptual Info

This node analyzes audio signals to identify tonal characteristics using deep learning techniques. It takes the mel-frequency cepstral coefficients (MFCCs) and their first-order deltas as input, processes them through a deep learning model, and outputs the identified musical key along with the confidence of the detection.

## Docstring

### Summary
Analyze audio signal for tonal patterns using deep learning.

### Parameters

- **mfcc_coefficients** (float): Temporal MFCC feature representing the spectral envelope of the audio.
- **delta_mfcc** (float): First-order difference of the MFCCs, indicating the rate-of-change of the spectral envelope.

### Returns

Tuple[str, float]: A tuple containing the identified musical key (str) and the tonal detection reliability (float).

### Raises

- ValueError: If the input MFCC coefficients or their deltas are invalid or inconsistent.

### Examples

```python
>>> mfcc_coefficients = [0.1, 0.2, 0.3]
>>> delta_mfcc = [0.01, 0.02, 0.03]
>>> tonal_analysis(mfcc_coefficients, delta_mfcc)
('C Major', 0.85)
```

```python
>>> mfcc_coefficients = [0.4, 0.5, 0.6]
>>> delta_mfcc = [0.04, 0.05, 0.06]
>>> tonal_analysis(mfcc_coefficients, delta_mfcc)
('G Minor', 0.78)
```
