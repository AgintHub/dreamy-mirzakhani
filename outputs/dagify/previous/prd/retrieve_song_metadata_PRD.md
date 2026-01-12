# retrieve_song_metadata PRD

## Description
Retrieve metadata for the matching songs


## Conceptual Info

This node retrieves metadata such as song titles, artist names, and album information for the matching songs.

## Docstring

### Summary
Retrieve song metadata based on the provided sample IDs and similarity scores.

### Parameters

- **sample_ids** (List[str]): List of IDs of the matching samples
- **similarity_scores** (List[float]): List of similarity scores corresponding to the matching samples
- **is_valid** (bool): Whether the output is valid

### Returns

dict: A dictionary containing the retrieved song metadata

### Raises

- ValueError: If the input sample IDs or similarity scores are empty

### Examples

```python
>>> sample_ids = ['song1', 'song2']
>>> similarity_scores = [0.8, 0.9]
>>> is_valid = True
>>> metadata = retrieve_song_metadata(sample_ids, similarity_scores, is_valid)
{'song_titles': ['Song 1', 'Song 2'], 'artist_names': ['Artist 1', 'Artist 2'], 'album_info': ['Album 1', 'Album 2'], 'metadata_retrieval_status': True}
```
