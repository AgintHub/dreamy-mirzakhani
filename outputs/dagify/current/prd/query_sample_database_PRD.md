# query_sample_database PRD

## Description
Query the sample database to find matching samples


## Conceptual Info

Query the sample database using extracted audio features to find matching song samples.

## Docstring

### Summary
Query the sample database to find matching song samples based on extracted audio features.

### Parameters

- **audio_features** (dict): Dictionary containing spectrogram, mfccs, and chroma features of the audio snippet.
- **database_id** (str): Unique identifier for the sample database.

### Returns

dict: Dictionary containing a list of potential matching song samples, their confidence scores, and query status.

### Raises

- ValueError: If audio features or database ID are missing or invalid.

### Examples

```python
>>> audio_features = {'spectrogram': [1, 2, 3], 'mfccs': [4, 5, 6], 'chroma_features': [7, 8, 9]}
>>> database_id = 'sample_db_1'
>>> result = query_sample_database(audio_features, database_id)
{'matching_samples': ['song1', 'song2'], 'sample_confidence_scores': [0.8, 0.9], 'query_status': True}
```
