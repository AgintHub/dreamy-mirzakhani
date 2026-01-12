# _list_musicians - Complete PRD Documentation

## Overview
PRDs for nodes in the '_list_musicians' module.

## Table of Contents

- [validate_metadata_structure](#validate_metadata_structure)

- [extract_artist_names_from_metadata](#extract_artist_names_from_metadata)

- [normalize_artist_names](#normalize_artist_names)

- [deduplicate_artist_list](#deduplicate_artist_list)

- [generate_musician_ids](#generate_musician_ids)

- [fetch_musician_aliases](#fetch_musician_aliases)

- [check_deduplication_occurred](#check_deduplication_occurred)



---

## validate_metadata_structure

### Description
Validates the structure of the input metadata to ensure it conforms to the expected format.

### Conceptual Info

This shim node is responsible for validating the structure of the input metadata. It ensures that the metadata conforms to the expected format, which is crucial for downstream processing and analysis.

### Docstring

**Summary:** Validates the input metadata structure to ensure conformity to the expected format.

**Parameters:**

- metadata (str): The input metadata to be validated. It should be a string representation of a dictionary containing song metadata.
**Returns:** str - A string representation of the validated metadata in the expected format.

**Raises:**

- ValueError: If the input metadata is not a valid string representation of a dictionary or if it lacks required fields.
- TypeError: If the input metadata is not a string.
**Examples:**

```python
>>> metadata = '{\"song_title\": \"Example Song\", \"artist_names\": \"Example Artist\"}'
>>> validated_metadata = validate_metadata_structure(metadata=metadata)
'{"song_title": "Example Song", "artist_names": "Example Artist"}'
```

```python
>>> metadata = '{\"invalid_key\": \"Invalid Value\"}'
>>> try:
...     validated_metadata = validate_metadata_structure(metadata=metadata)
>>> except ValueError as e:
...     print(e)
'Missing required fields in metadata'
```



---

## extract_artist_names_from_metadata

### Description
Extracts a list of artist names from the provided metadata string.

### Conceptual Info

This shim node is responsible for extracting artist names from a given metadata string, playing a crucial role in processing song metadata.

### Docstring

**Summary:** Extracts artist names from the provided metadata string and returns them as a list.

**Parameters:**

- metadata (str): The input metadata string containing artist information.
**Returns:** List[str] - A list of artist names extracted from the metadata string.

**Raises:**

- ValueError: If the input metadata is not a valid string or is empty.
- TypeError: If the input metadata is not of type string.
**Examples:**

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



---

## normalize_artist_names

### Description
Normalizes a list of artist names by standardizing their format and correcting minor variations in spelling or punctuation.

### Conceptual Info

This node takes a list of artist names, potentially containing variations in spelling, punctuation, or format, and normalizes them to a standard format.

### Docstring

**Summary:** Normalizes a list of artist names to a standard format.

**Parameters:**

- names (LIST_STR): A list of artist names that may contain variations in spelling, punctuation, or format.
**Returns:** LIST_STR - A list of artist names normalized to a standard format.

**Raises:**

- TypeError: If the input 'names' is not a list of strings.
- ValueError: If the input list is empty or contains non-string values.
**Examples:**

```python
>>> normalize_artist_names(names=['John Doe', 'Jane Smith'])
['John Doe', 'Jane Smith']
```

```python
>>> normalize_artist_names(names=['J Doe', 'Jane S.'])
['John Doe', 'Jane Smith']
```



---

## deduplicate_artist_list

### Description
Removes duplicate artist names from a given list while preserving the original order.

### Conceptual Info

This shim function is designed to remove duplicate artist names from a list, ensuring that the original order of artists is maintained. It plays a crucial role in data preprocessing for music metadata analysis.

### Docstring

**Summary:** Deduplicates a list of artist names while preserving their original order.

**Parameters:**

- names (LIST_STR): A list of artist names that may contain duplicates.
**Returns:** LIST_STR - A list of artist names with duplicates removed, maintaining the original order.

**Raises:**

- TypeError: If the input 'names' is not a list or if the list contains non-string elements.
- ValueError: If the input list is empty or contains only whitespace strings.
**Examples:**

```python
>>> deduplicate_artist_list(names=['John Doe', 'Jane Doe', 'John Doe'])
['John Doe', 'Jane Doe']
```

```python
>>> deduplicate_artist_list(names=['Artist1', 'Artist2', 'Artist1', 'Artist3'])
['Artist1', 'Artist2', 'Artist3']
```



---

## generate_musician_ids

### Description
Generates unique identifiers for musicians based on their names.

### Conceptual Info

This shim generates unique identifiers for musicians based on their names, serving as a crucial step in organizing and referencing musician data within the larger system.

### Docstring

**Summary:** Generates unique identifiers for musicians based on the provided names.

**Parameters:**

- names (str): A string containing musician names, likely comma-separated or in a specific format.
**Returns:** List[str] - A list of unique identifiers corresponding to the input musician names.

**Raises:**

- ValueError: If the input string is empty or contains invalid characters.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> generate_musician_ids(names='John Lennon,Paul McCartney')
['id1', 'id2']
```

```python
>>> generate_musician_ids(names='Michael Jackson')
['id3']
```



---

## fetch_musician_aliases

### Description
Fetches aliases for a list of musician names, returning a list of aliases corresponding to each musician.

### Conceptual Info

This shim node is responsible for retrieving aliases for musicians based on their names. It plays a crucial role in expanding the information available for each musician, potentially aiding in deduplication and comprehensive data collection.

### Docstring

**Summary:** Fetches aliases for a given list of musician names.

**Parameters:**

- names (List[str]): A list of musician names for which aliases are to be fetched.
**Returns:** List[str] - A list of aliases corresponding to the input musician names. Each element in the list represents aliases for a musician, potentially as a comma-separated string or a list of strings.

**Raises:**

- ValueError: If the input list of names is empty or contains invalid names.
- TypeError: If the input is not a list of strings.
**Examples:**

```python
>>> musicians = ['John Lennon', 'Paul McCartney']
>>> aliases = fetch_musician_aliases(names=musicians)
['Lennon, John Winston Lennon', 'McCartney, James Paul McCartney']
```

```python
>>> musicians = ['Michael Jackson']
>>> aliases = fetch_musician_aliases(names=musicians)
['The King of Pop, MJ']
```



---

## check_deduplication_occurred

### Description
Checks if deduplication occurred between the original and deduplicated lists of artist names.

### Conceptual Info

This shim function compares the original list of artist names with the deduplicated list to determine if any deduplication occurred.

### Docstring

**Summary:** Compares original and deduplicated lists of artist names to check if deduplication occurred.

**Parameters:**

- original (str): The original list of artist names before deduplication.
- deduplicated (str): The list of artist names after deduplication.
**Returns:** bool - True if deduplication occurred, False otherwise.

**Raises:**

- TypeError: If either 'original' or 'deduplicated' is not of type str.
- ValueError: If the input strings are not valid representations of lists.
**Examples:**

```python
>>> check_deduplication_occurred(original='["Artist1", "Artist2", "Artist1"]', deduplicated='["Artist1", "Artist2"]')
>>> # Expected output: True
True
```

```python
>>> check_deduplication_occurred(original='["Artist1", "Artist2"]', deduplicated='["Artist1", "Artist2"]')
>>> # Expected output: False
False
```

