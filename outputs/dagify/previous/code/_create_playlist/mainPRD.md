# _create_playlist - Complete PRD Documentation

## Overview
PRDs for nodes in the '_create_playlist' module.

## Table of Contents

- [validate_musician_inputs](#validate_musician_inputs)

- [expand_musician_aliases](#expand_musician_aliases)

- [fetch_sampled_songs_metadata](#fetch_sampled_songs_metadata)

- [extract_nlp_features](#extract_nlp_features)

- [apply_collaborative_filtering](#apply_collaborative_filtering)

- [build_graph_based_model](#build_graph_based_model)

- [rank_tracks_with_graph_algorithm](#rank_tracks_with_graph_algorithm)

- [select_final_tracks](#select_final_tracks)

- [generate_playlist_metadata](#generate_playlist_metadata)

- [calculate_artist_diversity_score](#calculate_artist_diversity_score)

- [extract_genre_representation](#extract_genre_representation)

- [generate_playlist_id](#generate_playlist_id)



---

## validate_musician_inputs

### Description
Validates that the provided musician IDs, names, and alias lists are consistent, correctly typed, and non‑empty, returning a status message.

### Conceptual Info

This shim ensures that the musician data supplied to downstream playlist creation processes is well‑formed and error‑free, preventing downstream failures.

### Docstring

**Summary:** Validate consistency and integrity of musician input data.

**Parameters:**

- musician_ids (str): JSON‑encoded list of unique musician identifiers.
- musician_names (str): JSON‑encoded list of musician names.
- musician_aliases (str): JSON‑encoded list of lists containing aliases for each musician.
**Returns:** str - A message indicating success or the specific validation error.

**Raises:**

- ValueError: Raised when list lengths differ or required fields are missing.
- TypeError: Raised when inputs cannot be parsed as JSON arrays of strings.
**Examples:**

```python
>>> validate_musician_inputs(
...     musician_ids='["id1", "id2"]',
...     musician_names='["Alice", "Bob"]',
...     musician_aliases='[["A"], ["B"]]')
'Validation successful'
```

```python
>>> validate_musician_inputs(
...     musician_ids='["id1"]',
...     musician_names='["Alice", "Bob"]',
...     musician_aliases='[["A"], ["B"]]')
ValueError: Length mismatch between musician_ids, musician_names, and musician_aliases.
```



---

## expand_musician_aliases

### Description
Expands musician data by combining IDs, names, and alias lists into a dictionary mapping each musician ID to its name and aliases.

### Conceptual Info

This shim serves as a data normalization step, aligning raw musician identifiers, names, and alias metadata into a unified structure required by downstream playlist generation and recommendation modules.

### Docstring

**Summary:** Combines lists of musician IDs, names, and aliases into a single dictionary mapping each ID to its name and list of aliases.

**Parameters:**

- musician_ids (str): JSON-encoded list of unique musician identifiers.
- musician_names (str): JSON-encoded list of musician names corresponding to the IDs.
- aliases (str): JSON-encoded list where each element is a list of aliases for the corresponding musician.
**Returns:** str - A JSON string representing a dictionary where each key is a musician ID and the value is a dictionary with keys 'name' (str) and 'aliases' (list of str).

**Raises:**

- ValueError: If the three input lists are not of the same length.
- TypeError: If any input string cannot be parsed as a JSON list.
**Examples:**

```python
>>> musician_ids = '["m1", "m2"]'
>>> musician_names = '["Artist One", "Artist Two"]'
>>> aliases = '["[A", "A1"]", ["B", "B1", "B2"]]'
>>> output = expand_musician_aliases(musician_ids, musician_names, aliases)
{"m1": {"name": "Artist One", "aliases": ["A", "A1"]}, "m2": {"name": "Artist Two", "aliases": ["B", "B1", "B2"]}}
```

```python
>>> expand_musician_aliases('[]', '[]', '[]')
{}
```



---

## fetch_sampled_songs_metadata

### Description
Retrieves metadata for a sampled set of songs based on expanded musician data, returning a list of song metadata dictionaries.

### Conceptual Info

This shim serves as the bridge between musician data expansion and the downstream playlist creation pipeline by providing a curated set of song metadata that can be used for feature extraction and recommendation scoring.

### Docstring

**Summary:** Fetch sampled songs metadata from an external service or database based on the provided expanded musician data.

**Parameters:**

- musician_data (str): JSON string representing a dictionary with keys 'musician_ids', 'musician_names', and 'aliases', used to sample songs.
**Returns:** str - A JSON string that can be parsed into a List[dict] where each dictionary contains metadata fields such as 'song_id', 'title', 'artist_id', 'genre', and 'duration'.

**Raises:**

- ValueError: If the input JSON does not contain required keys or has malformed structure.
- TypeError: If the input parameter is not a string.
- RuntimeError: If the external service fails to return data or returns an unexpected format.
**Examples:**

```python
>>> musician_data = '{"musician_ids":["id1"],"musician_names":["Artist"],"aliases":[["Alias1"]]}'
>>> result = fetch_sampled_songs_metadata(musician_data=musician_data)
>>> print(result)
[{"song_id": "s1", "title": "Song One", "artist_id": "id1", "genre": "Pop", "duration": 210}, {"song_id": "s2", "title": "Song Two", "artist_id": "id1", "genre": "Pop", "duration": 195}]
```

```python
>>> musician_data = '{"musician_ids":["id2"],"musician_names":["Band"],"aliases":[["BandAlias"]]}'
>>> result = fetch_sampled_songs_metadata(musician_data=musician_data)
>>> print(result)
[{"song_id": "s3", "title": "Track Three", "artist_id": "id2", "genre": "Rock", "duration": 240}]
```



---

## extract_nlp_features

### Description
Extracts NLP features from the given songs metadata.

### Conceptual Info

This shim node is responsible for extracting NLP features from the provided songs metadata, which is crucial for further processing in the playlist generation pipeline.

### Docstring

**Summary:** Extracts NLP features from the given songs metadata and returns them as a string representation of a dictionary.

**Parameters:**

- songs_metadata (str): A string representation of a list of dictionaries containing songs metadata.
**Returns:** str - A string representation of a dictionary containing the extracted NLP features.

**Raises:**

- ValueError: If the input songs metadata is not in the expected format or is empty.
- TypeError: If the input type is not a string or if the input string cannot be parsed into a list of dictionaries.
**Examples:**

```python
>>> songs_metadata = '[{"title": "Song 1", "lyrics": "Lyrics 1"}, {"title": "Song 2", "lyrics": "Lyrics 2"}]'
>>> extract_nlp_features(songs_metadata=songs_metadata)
'{"song1": {"feature1": 0.5, "feature2": 0.3}, "song2": {"feature1": 0.2, "feature2": 0.7}}'
```

```python
>>> songs_metadata = '[{"title": "Invalid Song", "lyrics": null}]'
>>> extract_nlp_features(songs_metadata=songs_metadata)
ValueError: Input songs metadata contains invalid or missing data.
```



---

## apply_collaborative_filtering

### Description
Applies collaborative filtering to compute similarity scores between musicians and songs based on provided metadata.

### Conceptual Info

This shim computes collaborative filtering scores that capture the affinity between musicians and songs, enabling downstream graph-based recommendation models.

### Docstring

**Summary:** Computes collaborative filtering scores from musician data and song metadata.

**Parameters:**

- musician_data (str): JSON string containing expanded musician information (ids, names, aliases).
- songs_metadata (str): JSON string containing metadata for each song (e.g., title, artist, genre, features).
**Returns:** str - JSON string that maps musician IDs to song IDs with associated similarity scores.

**Raises:**

- ValueError: Raised when the input JSON does not contain required fields or is malformed.
- TypeError: Raised when either musician_data or songs_metadata is not a string.
**Examples:**

```python
>>> musician_data = '{"musician_ids": ["m1"], "musician_names": ["Artist A"], "musician_aliases": [[]]}'
>>> songs_metadata = '{"songs": [{"song_id": "s1", "title": "Song X"}]}'
>>> apply_collaborative_filtering(musician_data, songs_metadata)
{"m1": {"s1": 0.85}}
```

```python
>>> apply_collaborative_filtering('invalid json', '{}')
ValueError: Invalid JSON format for musician_data.
```



---

## build_graph_based_model

### Description
Builds a graph model from NLP features, collaborative filtering scores, and songs metadata, returning a serialized graph representation as a JSON string.

### Conceptual Info

This shim encapsulates the logic for merging linguistic features, collaborative filtering scores, and song metadata into a unified graph model, which is later used for track ranking and playlist generation.

### Docstring

**Summary:** Creates a graph model from NLP features, collaborative filtering scores, and song metadata, returning the graph as a JSON string.

**Parameters:**

- nlp_features (str): JSON string containing extracted NLP features for songs.
- cf_scores (str): JSON string containing collaborative filtering scores for songs.
- songs_metadata (str): JSON string containing metadata for songs.
**Returns:** str - JSON string representing the constructed graph model.

**Raises:**

- ValueError: Raised when any of the input JSON strings are missing required fields.
- TypeError: Raised when input types are not strings.
**Examples:**

```python
>>> result = build_graph_based_model(
...     nlp_features='{"features": [0.1, 0.2, 0.3]}',
...     cf_scores='{"scores": [0.9, 0.8]}',
...     songs_metadata='{"songs": [{"id": "s1", "title": "Song A"}]}')
{"graph": {"nodes": 3, "edges": 2}}
```

```python
>>> result = build_graph_based_model(
...     nlp_features='{"features": []}',
...     cf_scores='{"scores": []}',
...     songs_metadata='{"songs": []}')
{"graph": {"nodes": 0, "edges": 0}}
```



---

## rank_tracks_with_graph_algorithm

### Description
Ranks tracks using a graph-based algorithm based on the provided graph model.

### Conceptual Info

This shim node is responsible for ranking tracks based on a graph model. It takes a graph model as input and returns a list of ranked track identifiers.

### Docstring

**Summary:** Ranks tracks using a graph-based algorithm.

**Parameters:**

- graph_model (str): A string representation of the graph model used for ranking tracks.
**Returns:** List[str] - A list of track identifiers ranked by the graph algorithm.

**Raises:**

- ValueError: If the graph model is invalid or cannot be processed.
- TypeError: If the input graph model is not a string.
**Examples:**

```python
>>> rank_tracks_with_graph_algorithm(graph_model='{"nodes": ["track1", "track2"], "edges": [{"source": "track1", "target": "track2"}]}')
['track2', 'track1']
```

```python
>>> rank_tracks_with_graph_algorithm(graph_model='{"nodes": ["track3", "track4"], "edges": [{"source": "track3", "target": "track4"}]}')
['track4', 'track3']
```



---

## select_final_tracks

### Description
Selects final tracks based on ranked tracks and diversity threshold.

### Conceptual Info

This shim function is responsible for selecting the final tracks from a list of ranked tracks based on a specified diversity threshold. It plays a crucial role in generating a playlist by ensuring that the selected tracks meet certain diversity criteria.

### Docstring

**Summary:** Selects final tracks from ranked tracks based on a diversity threshold.

**Parameters:**

- ranked_tracks (str): A string representation of a list of track IDs ranked according to their relevance or score.
- diversity_threshold (str): A string representation of a float value between 0 and 1 that determines the minimum diversity required among the selected tracks.
**Returns:** List[str] - A list of track IDs that have been selected based on the ranked tracks and the diversity threshold.

**Raises:**

- ValueError: If the diversity threshold is not within the range 0 to 1.
- TypeError: If the input types are incorrect.
**Examples:**

```python
>>> ranked_tracks = '["track1", "track2", "track3"]'
>>> diversity_threshold = '0.7'
>>> select_final_tracks(ranked_tracks=ranked_tracks, diversity_threshold=diversity_threshold)
['track1', 'track3']
```

```python
>>> ranked_tracks = '["track4", "track5", "track6"]'
>>> diversity_threshold = '0.5'
>>> select_final_tracks(ranked_tracks=ranked_tracks, diversity_threshold=diversity_threshold)
['track4', 'track6']
```



---

## generate_playlist_metadata

### Description
Generates metadata for a playlist based on selected tracks and musician names.

### Conceptual Info

This shim node is responsible for generating playlist metadata, including name and description, based on the selected track IDs and musician names provided as input.

### Docstring

**Summary:** Generates playlist metadata based on selected track IDs and musician names.

**Parameters:**

- selected_tracks (str): A JSON string representing a list of track identifiers selected for the playlist.
- musician_names (str): A JSON string representing a list of musician names associated with the selected tracks.
**Returns:** str - A JSON string representing a dictionary containing playlist metadata, including 'name' and 'description'.

**Raises:**

- ValueError: If the input strings are not valid JSON representations of lists.
- TypeError: If the input types are not strings.
**Examples:**

```python
>>> import json
>>> selected_tracks = json.dumps(['track1', 'track2'])
>>> musician_names = json.dumps(['musician1', 'musician2'])
>>> generate_playlist_metadata(selected_tracks, musician_names)
{"name": "Playlist Name", "description": "Playlist Description"}
```

```python
>>> import json
>>> selected_tracks = json.dumps(['track3', 'track4'])
>>> musician_names = json.dumps(['musician3', 'musician4'])
>>> generate_playlist_metadata(selected_tracks, musician_names)
{"name": "Another Playlist", "description": "Another Description"}
```



---

## calculate_artist_diversity_score

### Description
Calculates a score representing the diversity of artists in a given list of track IDs.

### Conceptual Info

This shim calculates the artist diversity score for a playlist based on the track IDs provided. It plays a crucial role in evaluating the variety of artists represented in the playlist.

### Docstring

**Summary:** Calculates the artist diversity score for a given list of track IDs.

**Parameters:**

- track_ids (str): A string containing the list of track IDs separated by commas or another delimiter.
**Returns:** float - A float value between 0 and 1 representing the diversity score of artists in the given track IDs.

**Raises:**

- ValueError: If the input track_ids string is empty or not properly formatted.
- TypeError: If the input track_ids is not a string.
**Examples:**

```python
>>> calculate_artist_diversity_score(track_ids='track1,track2,track3')
0.85
```

```python
>>> calculate_artist_diversity_score(track_ids='track4,track5')
0.7
```



---

## extract_genre_representation

### Description
Extracts a list of genres represented in a playlist based on the provided track identifiers.

### Conceptual Info

This shim function plays a crucial role in the playlist generation pipeline by determining the genre representation of the created playlist based on the selected track IDs.

### Docstring

**Summary:** Extracts a list of genres represented in a playlist based on the track identifiers provided as input.

**Parameters:**

- track_ids (str): A string containing the track identifiers, expected to be a list or comma-separated values.
**Returns:** List[str] - A list of unique genre names represented in the playlist.

**Raises:**

- ValueError: If the input track_ids is not a valid string or cannot be processed.
- TypeError: If the input type is not a string.
**Examples:**

```python
>>> extract_genre_representation(track_ids='track1,track2,track3')
['pop', 'rock', 'electronic']
```

```python
>>> extract_genre_representation(track_ids='track4')
['hip-hop']
```



---

## generate_playlist_id

### Description
Generates a unique identifier for a playlist.

### Conceptual Info

This shim generates a unique identifier for a playlist, playing a crucial role in playlist management within the larger system.

### Docstring

**Summary:** Generates a unique identifier for a playlist without taking any input parameters.

**Returns:** str - A unique string identifier for the playlist.

**Raises:**

- RuntimeError: If the identifier generation fails.
**Examples:**

```python
>>> generate_playlist_id()
'playlist_12345'
```

```python
>>> generate_playlist_id()
'unique_playlist_id_67890'
```

