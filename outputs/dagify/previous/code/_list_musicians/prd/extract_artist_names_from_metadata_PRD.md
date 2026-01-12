# extract_artist_names_from_metadata PRD

## Description
Extracts a list of artist names from the provided metadata string.


## Conceptual Info

This shim node is responsible for extracting artist names from a given metadata string, playing a crucial role in processing song metadata.

## Docstring

### Summary
Extracts artist names from the provided metadata string and returns them as a list.

### Parameters

- **metadata** (str): The input metadata string containing artist information.

### Returns

List[str]: A list of artist names extracted from the metadata string.

### Raises

- ValueError: If the input metadata is not a valid string or is empty.
- TypeError: If the input metadata is not of type string.

### Examples

```python
>>> metadata = 'Song by Artist1, Artist2, and Artist3'
>>> artist_names = extract_artist_names_from_metadata(metadata=metadata)
['Artist1', 'Artist2', 'Artist3']
```

```python
>>> metadata = 'Artists: ArtistX, ArtistY'
>>> artist_names = extract_artist_names_from_metadata(metadata=metadata)
['ArtistX', 'ArtistY']
```
