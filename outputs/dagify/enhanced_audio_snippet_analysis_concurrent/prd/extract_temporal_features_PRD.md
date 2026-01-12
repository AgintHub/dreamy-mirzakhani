# extract_temporal_features PRD

## Description
Calculate temporal domain features from raw audio data, returning the zero‑crossing rate, signal energy, entropy, and a list of raw temporal metrics.


## Conceptual Info

This node transforms raw audio samples into a compact set of time‑domain descriptors that capture the signal’s dynamic behaviour.

## Docstring

### Summary
Extract zero‑crossing rate, energy, and entropy from raw audio data.

### Parameters

- **audio_data** (str): Raw audio samples, typically a string of comma‑separated numeric values.
- **sampling_rate** (int): Sampling frequency of the audio signal in Hz.
- **file_format** (str): Encoding format of the input audio (e.g., 'wav', 'mp3').
- **metadata** (list[str]): Additional signal descriptors extracted by load_audio_snippet.

### Returns

dict: Dictionary with keys 'zero_crossing_rate', 'energy', 'entropy', and 'temporal_features', each mapped to a float or list of floats.

### Raises

- ValueError: If audio_data is empty, contains non‑numeric tokens, or if sampling_rate <= 0.

### Examples

```python
>>> audio_data = '1,-1,1,-1,0,0,1,-1'
>>> sampling_rate = 44100
>>> file_format = 'wav'
>>> metadata = []
>>> result = extract_temporal_features(audio_data, sampling_rate, file_format, metadata)
>>> print(result)
{'zero_crossing_rate': 4.0, 'energy': 8.0, 'entropy': 1.0, 'temporal_features': [4.0, 8.0, 1.0]}
```

```python
>>> audio_data = '0.5,-0.5,0.5,-0.5'
>>> sampling_rate = 22050
>>> file_format = 'mp3'
>>> metadata = []
>>> print(extract_temporal_features(audio_data, sampling_rate, file_format, metadata))
{'zero_crossing_rate': 2.0, 'energy': 1.0, 'entropy': 0.0, 'temporal_features': [2.0, 1.0, 0.0]}
```
