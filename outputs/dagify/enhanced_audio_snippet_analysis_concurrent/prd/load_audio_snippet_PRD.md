# load_audio_snippet PRD

## Description
Load audio file with metadata extraction


## Conceptual Info

The `load_audio_snippet` node reads an audio file from disk (or a remote source), decodes its waveform into raw samples, and extracts fundamental metadata—including sampling rate, format, and key signal statistics. The data is returned in a lightweight, serializable form for downstream analysis.

## Docstring

### Summary
Load an audio file and extract basic metadata for further analysis.

### Parameters

- **audio_file_path** (str): Filesystem path or URL to the audio file to be loaded.

### Returns

Dict[str, Any]: Dictionary containing `audio_data` (raw samples), `sampling_rate` (Hz), `file_format` (e.g., 'wav'), and `metadata` (list of descriptive strings).

### Raises

- FileNotFoundError: Raised if the specified file does not exist or cannot be accessed.
- ValueError: Raised if the file format is unsupported or the file is corrupted.
- RuntimeError: Raised for low‑level decoding failures (e.g., I/O errors during read).

### Examples

```python
>>> result = load_audio_snippet('samples/beat.wav')
>>> print(result['sampling_rate'])  # 44100
>>> print(result['file_format'])    # 'wav'
>>> print(len(result['metadata']))  # 4
44100
wav
4
```

```python
>>> try:
...     load_audio_snippet('missing.mp3')
>>> except FileNotFoundError as e:
...     print(str(e))
'File not found: missing.mp3'
```
