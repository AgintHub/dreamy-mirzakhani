# identify_sampled_songs PRD

## Description
Detects and identifies the original songs sampled within a recorded audio snippet by combining traditional audio fingerprinting techniques (Chromaprint, pHash) with deep‑learning embeddings (VGGish/PANNs) and efficient approximate nearest‑neighbor similarity search (FAISS/Annoy). The node outputs a ranked list of candidate tracks, confidence scores, and relevant metadata, enabling downstream verification and attribution.


## Conceptual Info

This node identifies sampled songs in an audio snippet using a combination of audio fingerprinting, deep learning embeddings, and similarity search.

## Docstring

### Summary
Identifies sampled songs by extracting features, generating fingerprints, and performing similarity search.

### Parameters

- **processed_audio_data** (dict): Preprocessed audio data containing base64 encoded audio, duration, sample rate, and feature vectors.

### Returns

List[dict]: A list of dictionaries containing track_id, confidence, start_time, end_time, and metadata for each identified candidate track.

### Raises

- ValueError: If the input audio data is invalid or corrupted.
- RuntimeError: If the similarity search or fingerprint generation fails.

### Examples

```python
>>> processed_audio_data = {'processed_audio_base64': '...', 'duration_seconds': 10.0, 'sample_rate_hz': 44100, 'feature_vectors': [...]
>>> identified_tracks = identify_sampled_songs(processed_audio_data)
[{'track_id': 'TRK123', 'confidence': 0.9, 'start_time': 2.5, 'end_time': 5.0, 'artist_name': 'Artist1', 'track_title': 'Track1', 'release_date': '2020-01-01'}]
```
