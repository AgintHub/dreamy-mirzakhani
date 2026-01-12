# record_audio_snippet PRD

## Description
Captures a short, high‑fidelity audio segment from the user’s device, performs real‑time pre‑processing (normalization, silence trimming, VAD), encodes the signal with Opus, and stores the result in a temporary buffer with comprehensive metadata for downstream processing.


## Conceptual Info

This node records a brief, high‑fidelity audio clip from the microphone, applies real‑time preprocessing, encodes it with Opus, and returns the binary payload together with essential metadata for downstream analysis.

## Docstring

### Summary
Records a short audio snippet from the user's microphone, normalizes and trims silence, optionally applies VAD, encodes the signal with Opus, and returns the binary payload with metadata.

### Returns

dict: Dictionary containing audio_data, metadata, duration, sample_rate, codec, and vad_confidence.

### Raises

- AudioCaptureError: Raised when the audio capture hardware fails or the recording is interrupted.
- PermissionError: Raised when the application does not have permission to access the microphone.

### Examples

```python
>>> result = record_audio_snippet()
{
  "audio_data": "<binary base64>",
  "metadata": ["5.0", "48000", "Opus", "0.95"],
  "duration": 5.0,
  "sample_rate": 48000,
  "codec": "Opus",
  "vad_confidence": 0.95
}
```

```python
>>> try:
  record_audio_snippet()
except PermissionError as e:
  print(e)
PermissionError: Microphone access denied.
```
