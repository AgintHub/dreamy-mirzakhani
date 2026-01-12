# load_audio_snippet PRD

## Description
Load an audio file from a local or remote source and provide the raw audio data in a compact string format along with key metadata such as sample rate, file format, duration, bit depth, channel count, and loudness.


## Conceptual Info

Provides the foundational audio data and its descriptive statistics for downstream audio‑analysis tasks.

## Docstring

### Summary
Loads an audio file and returns its raw samples in a compact string along with sampling rate, file format, and a list of key metadata values.

### Parameters

- **file_path** (str): Path or URL to the audio file to be loaded.

### Returns

Dict[str, Union[str, int, List[str]]]: Dictionary containing `audio_data`, `sampling_rate`, `file_format`, and `metadata`.

### Raises

- FileNotFoundError: Raised if the file does not exist or cannot be accessed.
- ValueError: Raised if the file format is unsupported or the file is corrupted.

### Examples

```python
>>> result = load_audio_snippet('/path/to/song.wav')
>>> print(result['file_format'])
>>> print(result['sampling_rate'])
>>> print(result['metadata'])
"WAV"
"44100"
"['duration: 3.12s', 'bit_depth: 16', 'channels: 2', 'loudness: -12.3 dB']"
```

```python
>>> result = load_audio_snippet('https://example.com/track.mp3')
>>> print(len(result['audio_data']))
"123456"
```
