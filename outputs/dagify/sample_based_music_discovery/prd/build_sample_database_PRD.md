# build_sample_database PRD

## Description
Create a database of known song samples


## Conceptual Info

Builds a comprehensive database of song samples with their audio features for efficient querying.

## Docstring

### Summary
Creates a database of known song samples with their corresponding audio features.

### Returns

{database_id: str, sample_count: int, audio_features: List[str], sample_ids: List[str]}: A dictionary containing the database_id, sample_count, audio_features, and sample_ids.

### Raises

- Exception: If there is an issue gathering the dataset or storing it in the database.

### Examples

```python
>>> build_sample_database()
{'database_id': 'db123', 'sample_count': 1000, 'audio_features': ['spectrogram', 'mfcc', 'chroma'], 'sample_ids': ['sample1', 'sample2', ...]}
```
