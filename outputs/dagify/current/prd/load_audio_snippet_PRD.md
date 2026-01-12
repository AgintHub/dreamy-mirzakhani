# load_audio_snippet PRD

## Description
Load the input audio snippet for analysis


## Conceptual Info

Loads an input audio snippet for analysis by extracting its audio features.

## Docstring

### Summary
Loads an input audio file, extracts its audio features, and returns the file path, audio features, and loading status.

### Parameters

- **audio_file** (str): Path to the input audio file

### Returns

{audio_file_path: str, audio_features: List[float], loading_status: bool}: A dictionary containing the path to the loaded audio file, its extracted audio features, and the loading status.

### Raises

- FileNotFoundError: If the input audio file does not exist.
- Exception: If there is an issue loading or processing the audio file.

### Examples

```python
>>> load_audio_snippet('path/to/audio/file.wav')
{'audio_file_path': 'path/to/audio/file.wav', 'audio_features': [1.0, 2.0, 3.0], 'loading_status': True}
```

```python
>>> load_audio_snippet('non_existent_file.wav')
Raises FileNotFoundError
```
