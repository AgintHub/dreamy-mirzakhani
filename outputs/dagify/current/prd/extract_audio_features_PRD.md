# extract_audio_features PRD

## Description
Extract relevant audio features from the loaded snippet


## Conceptual Info

This node takes an audio snippet loaded by the 'load_audio_snippet' node and extracts relevant audio features.

## Docstring

### Summary
Extracts spectrogram, MFCCs, and chroma features from an audio snippet.

### Parameters

- **audio_snippet** (dict): Loaded audio snippet with its path and features.

### Returns

dict: A dictionary containing spectrogram, MFCCs, chroma features, and feature extraction status.

### Raises

- Exception: If there's an error in feature extraction.

### Examples

```python
>>> audio_snippet = {'audio_file_path': '/path/to/audio.wav', 'audio_features': [...] }
>>> features = extract_audio_features(audio_snippet)
{'spectrogram': [...], 'mfccs': [...], 'chroma_features': [...], 'feature_extraction_status': True}
```
