# create_playlist PRD

## Description
Curates a playlist featuring a diverse selection of songs from the identified musicians, leveraging their sampled songs' metadata to inform the playlist's thematic and sonic coherence.


## Conceptual Info

This node generates a playlist based on the musicians identified in the sampled songs, ensuring diversity and coherence through advanced algorithms.

## Docstring

### Summary
Creates a playlist by analyzing sampled songs' metadata, applying NLP and collaborative filtering, and ranking tracks based on a graph-based model.

### Parameters

- **musician_ids** (List[str]): List of unique identifiers for the musicians, derived from the `list_musicians` node.
- **musician_names** (List[str]): List of names of the musicians, used to inform the playlist's thematic coherence.
- **musician_aliases** (List[List[str]]): List of lists containing aliases for each musician, aiding in disambiguation and comprehensive coverage.

### Returns

Dict[str, Union[str, List[str], float]]: A dictionary containing the generated playlist's details, including its ID, track IDs, name, description, artist diversity score, and genre representation.

### Raises

- ValueError: If the input lists (`musician_ids`, `musician_names`, `musician_aliases`) are inconsistent or empty.
- RuntimeError: If the graph-based ranking algorithm fails to converge or if there's an issue with the MIR framework.

### Examples

```python
>>> create_playlist(musician_ids=['M1', 'M2'], musician_names=['Artist1', 'Artist2'], musician_aliases=[['A1'], ['A2']])
{'playlist_id': 'P1', 'track_ids': ['T1', 'T2'], 'playlist_name': 'Diverse Playlist', 'playlist_description': 'A mix of genres', 'artist_diversity_score': 0.8, 'genre_representation': ['Rock', 'Pop']}
```
