# ml_feature_extraction PRD

## Description
Generates high‑level audio representations by passing the raw audio through a convolutional network for spectral pattern extraction and a recurrent network for temporal dynamics summarization.


## Conceptual Info

This node transforms raw audio data into compact, learnable embeddings by applying a CNN to capture local spectral structures and an RNN to model sequential temporal dynamics. The resulting vectors can be used for downstream tasks such as similarity search, classification, or metadata enrichment.

## Docstring

### Summary
Extract deep learning‑based audio features using a CNN for spectral analysis and an RNN for temporal summarization.

### Parameters

- **audio_data** (str): Base64‑encoded raw audio samples returned by `load_audio_snippet`.
- **sampling_rate** (int): Sampling frequency of the audio in Hertz.

### Returns

Dict[str, float]: Dictionary containing `cnn_features` and `rnn_features` – each a scalar summarizing the high‑level representation extracted by the respective network.

### Raises

- ValueError: If `audio_data` is empty, not valid Base64, or decoding fails.
- RuntimeError: If the CNN or RNN inference pipeline raises an exception (e.g., GPU out‑of‑memory, model file missing).

### Examples

```python
>>> cnn, rnn = ml_feature_extraction('UklGRi4AAABXRUJQVlA4TBEAAAAvAAAAAA', 44100)
>>> print(cnn, rnn)
0.123 0.456
```

```python
>>> result = ml_feature_extraction('invalid_base64_string', 44100)
>>> print(result)
ValueError: Invalid Base64 audio data.
```
