# ml_feature_extraction PRD

## Description
Generates high‑level audio representations by passing the raw audio through a convolutional network for spectral pattern extraction and a recurrent network for temporal dynamics summarization.


## Conceptual Info

The node encapsulates a lightweight deep‑learning inference step that transforms raw audio into two fixed‑length embeddings—one from a convolutional pathway capturing frequency‑domain structure, and another from a recurrent pathway capturing sequence‑level dynamics.

## Docstring

### Summary
Generate deep learning features from raw audio data using CNN and RNN models.

### Parameters

- **audio_data** (str): Base64‑encoded or hex string representation of the raw audio samples.
- **sampling_rate** (int): Sampling frequency of the audio in Hz.
- **file_format** (str): Encoding format of the audio (e.g., 'WAV', 'MP3', 'FLAC').
- **metadata** (List[str]): List of signal characteristics such as duration, bit depth, channel count, and loudness level.

### Returns

Dict[str, float]: A dictionary with keys 'cnn_features' and 'rnn_features', each mapping to a float embedding summarizing spectral and temporal information respectively.

### Raises

- ValueError: Raised when `audio_data` is empty or cannot be decoded.
- TypeError: Raised if input types do not match the expected signatures.
- RuntimeError: Raised when the CNN or RNN inference fails due to model errors or corrupted inputs.

### Examples

```python
>>> audio_data = 'UklGRiQAAABXQVZFZm10IBAAAAABAAEAgLsAAAB3AAABAAgAAQ==',
>>> sampling_rate = 44100,
>>> file_format = 'WAV',
>>> metadata = ['duration:3.5s', 'bit_depth:16', 'channels:2', 'loudness:-12dB']
>>> features = ml_feature_extraction(audio_data, sampling_rate, file_format, metadata)
>>> print(features['cnn_features'])
>>> print(features['rnn_features'])
0.8735
0.4562
```

```python
>>> try:
...     ml_feature_extraction('', 44100, 'WAV', ['duration:3.5s'])
>>> except ValueError as e:
...     print(str(e))
"audio_data is empty or cannot be decoded"
```
