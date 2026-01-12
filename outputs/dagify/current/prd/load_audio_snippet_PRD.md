# load_audio_snippet PRD

## Description
Load an audio file from a local or remote source and provide the raw audio data in a compact string format along with key metadata such as sample rate, file format, duration, bit depth, channel count, and loudness.


## Conceptual Info

The node encapsulates audio ingestion, decoding, and metadata extraction to provide a lightweight, transportable representation of an audio snippet.

## Docstring

### Summary
Load an audio file from a local path or URL, decode it, and return raw data plus essential metadata.

### Parameters

- **audio_uri** (str): A filesystem path or HTTP(S) URL pointing to the audio file to be loaded.

### Returns

Dict[str, Any]: A dictionary with four keys:
- audio_data (str): Base64‑encoded raw samples.
- sampling_rate (int): Sample rate in Hz.
- file_format (str): Audio file format.
- metadata (List[str]): List of formatted strings describing duration, bit depth, channels, and loudness.

### Raises

- FileNotFoundError: Raised when the local file does not exist or cannot be accessed.
- ConnectionError: Raised when the remote URL cannot be reached or the download fails.
- ValueError: Raised when the file format is unsupported or the file is corrupted.

### Examples

```python
>>> result = load_audio_snippet('samples/track.wav')
>>> print(result['sampling_rate'])
44100
```

```python
>>> result = load_audio_snippet('https://example.com/music.mp3')
>>> print(result['file_format'])
MP3
```
