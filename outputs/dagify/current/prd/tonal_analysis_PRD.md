# tonal_analysis PRD

## Description
Identify tonal characteristics


## Conceptual Info

The `tonal_analysis` node takes MFCC features derived from an audio signal and uses a pre‑trained deep neural network to infer the musical key (e.g., C‑major, A‑minor) present in the clip. It also returns a confidence score indicating how reliably the key was detected.

## Docstring

### Summary
Infer the musical key from MFCC features and return a confidence score.

### Parameters

- **mfcc_coefficients** (List[float]): Temporal MFCC feature vectors extracted by the `mfcc_extraction` node.
- **delta_mfcc** (List[float]): First‑order delta MFCC values indicating the rate of change in the MFCCs.

### Returns

Tuple[str, float]: A tuple containing the detected musical key (e.g., 'C Major') and a confidence score between 0 and 1.

### Raises

- ValueError: Raised if either `mfcc_coefficients` or `delta_mfcc` is empty or not a list of floats.

### Examples

```python
>>> tone, confidence = tonal_analysis([0.12, 0.09, 0.07, 0.04], [0.01, 0.02, 0.01, 0.00])
"('C Major', 0.92)"
```

```python
>>> # Error case – empty MFCC list
>>> try:
...     tonal_analysis([], [0.01, 0.02])
>>> except ValueError as e:
...     print(e)
"Input MFCC lists must be non‑empty."
```
