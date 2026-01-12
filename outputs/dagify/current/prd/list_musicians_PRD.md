# list_musicians PRD

## Description
Aggregates and deduplicates a comprehensive list of musicians involved in the sampled songs, leveraging metadata extracted from the identified samples.


## Conceptual Info

This node aggregates and deduplicates a list of musicians from the metadata of sampled songs, ensuring a canonicalized and structured output for downstream consumption.

## Docstring

### Summary
Aggregates and deduplicates musicians from sampled song metadata.

### Parameters

- **song_metadata** (List[Dict]): Metadata of the sampled songs, including artist names and other relevant details extracted by the `extract_song_metadata` node.

### Returns

Tuple[List[str], List[str], List[List[str]], bool]: A tuple containing lists of musician IDs, names, aliases, and a boolean indicating whether the list has been deduplicated.

### Raises

- ValueError: If the input metadata is malformed or missing critical information.

### Examples

```python
>>> song_metadata = [{'artist_names': ['Artist1', 'Artist2']}, {'artist_names': ['Artist2', 'Artist3']}]
>>> list_musicians(song_metadata)
(['id1', 'id2', 'id3'], ['Artist1', 'Artist2', 'Artist3'], [['Alias1'], ['Alias2'], ['Alias3']], True)
```
