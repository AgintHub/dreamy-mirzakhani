# load_audio_snippet PRD

## Description
Load audio file with metadata extraction


## Conceptual Info

The `load_audio_snippet` node reads an audio file from disk, extracts the raw sample data, the sample rate, the file format, and generates a short textual summary of key signal characteristics (duration, channel count, bit depth, etc.). This node serves as the foundational data source for all downstream audio‑feature extraction and analysis nodes.

## Docstring

### Summary
Read an audio file and return raw data and metadata.

### Parameters

- **audio_file_path** (str): File system path to the audio file to be loaded.

### Returns

Dict[str, Any]: Dictionary containing four keys:
- `audio_data` (str): Raw audio samples as bytes or base64 string.
- `sampling_rate` (int): Sample rate in Hz.
- `file_format` (str): Audio file format (e.g., 'wav', 'mp3').
- `metadata` (List[str]): Human‑readable list of signal characteristics such as duration, channels, and bit depth.

### Raises

- FileNotFoundError: Raised when the specified file does not exist.
- ValueError: Raised when the file format is unsupported or the file is corrupted.
- IOError: Raised on low‑level I/O errors during file read.

### Examples

```python
>>> audio_info = load_audio_snippet('samples/example.wav')
>>> print(audio_info['sampling_rate'])
>>> print(audio_info['metadata'])
44100
['duration: 3.58s', 'channels: 2', 'bit depth: 16']
```

```python
>>> try:
...     load_audio_snippet('nonexistent.mp3')
>>> except FileNotFoundError as e:
...     print('Error:', e)
Error: [Errno 2] No such file or directory: 'nonexistent.mp3'
```
