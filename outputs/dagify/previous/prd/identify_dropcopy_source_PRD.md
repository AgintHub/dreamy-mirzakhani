# identify_dropcopy_source PRD

## Description
Precisely determine the authoritative dropcopy source within the pico datacenter environment, leveraging validated OAuth authentication to ensure secure and compliant access.


## Conceptual Info

This node securely identifies and validates the authoritative dropcopy data source within the pico datacenter environment by utilizing OAuth-authenticated credentials to ensure access permissions, accuracy, and readiness for data extraction.

## Docstring

### Summary
Identifies the authoritative dropcopy source within the pico datacenter leveraging validated OAuth authentication to ensure secure, authorized, and compliant access.

### Parameters

- **oauth_access_token** (str): OAuth 2.0 access token obtained from the authenticate_pico_credentials node used to authorize access to pico datacenter resources.

### Returns

dict: A dictionary containing the dropcopy source's unique identifier (source_id), its human-readable name (source_name), the URI or path to the source (source_uri), and a boolean flag (is_accessible) indicating whether the source was verified as accessible and ready for extraction.

### Raises

- AuthenticationError: If the provided OAuth access token is invalid or lacks necessary scopes to identify the dropcopy source.
- SourceNotFoundError: If no authoritative dropcopy source can be located within the pico datacenter environment.
- AccessDeniedError: If access to the identified source is denied or the source is found to be inaccessible.
- ConnectionError: If network or service issues prevent validation of source accessibility.

### Examples

```python
>>> result = identify_dropcopy_source(oauth_access_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...')
>>> print(result['source_id'], result['source_name'], result['source_uri'], result['is_accessible'])
'dc-12345' 'Primary Dropcopy' '/datacenter/dropcopy/primary' True
```

```python
>>> result = identify_dropcopy_source(oauth_access_token='valid_token_string')
>>> if result['is_accessible']:
...     # Proceed to pull dropcopy data
...     pass
# No output, just procedural flow based on accessibility.
```
