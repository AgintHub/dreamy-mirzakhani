# validate_metadata_structure PRD

## Description
Validates the structure of the input metadata to ensure it conforms to the expected format.


## Conceptual Info

This shim node is responsible for validating the structure of the input metadata. It ensures that the metadata conforms to the expected format, which is crucial for downstream processing and analysis.

## Docstring

### Summary
Validates the input metadata structure to ensure conformity to the expected format.

### Parameters

- **metadata** (str): The input metadata to be validated. It should be a string representation of a dictionary containing song metadata.

### Returns

str: A string representation of the validated metadata in the expected format.

### Raises

- ValueError: If the input metadata is not a valid string representation of a dictionary or if it lacks required fields.
- TypeError: If the input metadata is not a string.

### Examples

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
