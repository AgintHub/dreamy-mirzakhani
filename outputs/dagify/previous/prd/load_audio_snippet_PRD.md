# load_audio_snippet PRD

## Description
Load an audio file from a local or remote source and provide the raw audio data in a compact string format along with key metadata such as sample rate, file format, duration, bit depth, channel count, and loudness.


## Conceptual Info

Loads audio data and extracts relevant metadata.

## Docstring

### Summary
Loads an audio file and extracts its raw data and metadata.

### Parameters

- **file_path** (str): Path to the audio file (local or remote).

### Returns

Tuple[str, int, str, List[str]]: A tuple containing the Base64-encoded audio data, sampling rate, file format, and a list of metadata.

### Raises

- FileNotFoundError: If the audio file is not found.
- ValueError: If the audio file is corrupted or unsupported.

### Examples

```python
>>> load_audio_snippet('path/to/audio.wav')
('base64_encoded_data', 44100, 'WAV', ['Duration: 10s', 'Bit Depth: 16', 'Channels: 2', 'Loudness: -20dB'])
```

```python
>>> load_audio_snippet('https://example.com/audio.mp3')
('base64_encoded_data', 48000, 'MP3', ['Duration: 5s', 'Bit Depth: 24', 'Channels: 1', 'Loudness: -15dB'])
```
