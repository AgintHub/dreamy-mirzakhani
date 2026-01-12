# verify_official_url PRD

## Description
Verifies the official URL from a list of candidate URLs based on musician metadata.


## Conceptual Info

This shim node is responsible for verifying the official URL of a musician from a list of candidate URLs by utilizing the provided musician metadata.

## Docstring

### Summary
Verifies the official URL from a list of candidate URLs based on musician metadata.

### Parameters

- **candidate_urls** (list[str]): A list of URLs to be verified as the official URL of the musician.
- **musician_metadata** (str): Metadata associated with the musician, which can include information like name, aliases, and other relevant data.

### Returns

str: The verified official URL of the musician.

### Raises

- ValueError: If the input candidate_urls is empty or if musician_metadata is invalid.
- TypeError: If the type of candidate_urls is not list[str] or if musician_metadata is not str.

### Examples

```python
>>> candidate_urls = ['https://example.com/musician1', 'https://example.com/musician1-alias']
>>> musician_metadata = '{"name": "Musician1", "aliases": ["Musician1-alias"]}'
>>> verified_url = verify_official_url(candidate_urls=candidate_urls, musician_metadata=musician_metadata)
'https://example.com/musician1'
```

```python
>>> candidate_urls = ['https://example.com/musician2-official', 'https://example.com/musician2']
>>> musician_metadata = '{"name": "Musician2", "aliases": ["Musician2-alias"]}'
>>> verified_url = verify_official_url(candidate_urls=candidate_urls, musician_metadata=musician_metadata)
'https://example.com/musician2-official'
```
