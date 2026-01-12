# ml_feature_extraction PRD

## Description
Generates high‑level audio representations by passing the raw audio through a convolutional network for spectral pattern extraction and a recurrent network for temporal dynamics summarization.


## Conceptual Info

This node generates high-level audio representations using deep learning architectures.

## Docstring

### Summary
Extracts deep learning features from raw audio data using CNN and RNN models.

### Parameters

- **audio_data** (str): Base64-encoded representation of the raw audio samples from load_audio_snippet.
- **sampling_rate** (int): Sampling frequency of the audio in Hertz from load_audio_snippet.

### Returns

tuple[float, float]: A tuple containing cnn_features and rnn_features, summarizing spectral and temporal patterns respectively.

### Raises

- ValueError: If audio_data is empty or sampling_rate is invalid.

### Examples

```python
>>> audio_data = 'base64_encoded_audio_data'
>>> sampling_rate = 44100
>>> cnn_features, rnn_features = ml_feature_extraction(audio_data, sampling_rate)
(array([0.1, 0.2, ...]), array([0.3, 0.4, ...]))
```
