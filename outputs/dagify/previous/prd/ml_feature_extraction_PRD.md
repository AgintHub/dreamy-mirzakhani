# ml_feature_extraction PRD

## Description
Generate deep learning features using CNN and RNN architectures


## Conceptual Info

Extract high‑level audio embeddings from a raw waveform using pretrained convolutional and recurrent neural networks. These embeddings capture both spectral textures and temporal dynamics, enabling downstream tasks such as classification, similarity search, or augmentation.

## Docstring

### Summary
Generate deep learning features using CNN and RNN architectures.

### Parameters

- **audio_data** (str): Raw audio sample data as a byte string or base64‑encoded string.
- **sampling_rate** (int): Sample rate of the audio in Hz.
- **file_format** (str): Encoding format of the input audio (e.g., 'wav', 'mp3').
- **metadata** (List[str]): Additional signal characteristics extracted by the loader.

### Returns

Tuple[List[float], List[float]]: A tuple containing (cnn_features, rnn_features). Each list holds floating‑point embeddings of the same dimensionality.

### Raises

- ValueError: Raised if audio_data is empty or cannot be decoded.
- TypeError: Raised when input types do not match expected signatures.
- RuntimeError: Raised if the deep‑learning model inference fails.

### Examples

```python
>>> cnn, rnn = ml_feature_extraction(
...     audio_data='\x00\x01\x02',
...     sampling_rate=44100,
...     file_format='wav',
...     metadata=['mono', 'stereo']
>>> )
([0.12, 0.45, 0.78, 0.33], [0.56, 0.89, 0.11, 0.22])
```

```python
>>> cnn, rnn = ml_feature_extraction(
...     audio_data='\x00\x01',
...     sampling_rate=48000,
...     file_format='mp3',
...     metadata=[]
>>> )
([0.10, 0.34, 0.67, 0.29], [0.51, 0.83, 0.09, 0.18])
```
