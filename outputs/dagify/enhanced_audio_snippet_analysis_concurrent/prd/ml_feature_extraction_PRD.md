# ml_feature_extraction PRD

## Description
Generate deep learning features using CNN and RNN architectures


## Conceptual Info

Extracts high‑level deep‑learning embeddings from raw audio by feeding the waveform through a CNN backbone followed by an RNN, producing compact scalar summaries of learned spectral and temporal characteristics.

## Docstring

### Summary
Generate deep learning features from raw audio using a convolutional‑plus‑recurrent architecture.

### Parameters

- **audio_data** (str): Raw audio bytes (e.g., WAV or MP3 payload) obtained from `load_audio_snippet`.
- **sampling_rate** (int): Sampling rate of the audio signal in Hz.
- **file_format** (str): Encoding format of the audio file (e.g., "wav", "mp3").
- **metadata** (List[str]): Optional list of pre‑computed signal characteristics (e.g., spectral centroid, zero‑crossing rate).

### Returns

Dict[str, float]: A dictionary containing two scalar features:
- `cnn_features`: A single float summarizing the convolutional network’s output.
- `rnn_features`: A single float summarizing the recurrent network’s output.

### Raises

- ValueError: Raised when `audio_data` is empty or None.
- RuntimeError: Raised if the underlying deep‑learning inference fails (e.g., GPU out‑of‑memory, model file missing).

### Examples

```python
>>> result = ml_feature_extraction('\x00\x01\x02', 44100, 'wav', ['centroid: 2000', 'rolloff: 3000'])
{'cnn_features': 0.123, 'rnn_features': 0.456}
```

```python
>>> try:
...     ml_feature_extraction('', 44100, 'wav', [])
>>> except ValueError as e:
...     print(e)
"audio_data must not be empty"
```
