# pull_dropcopy PRD

## Description
Securely retrieve the identified dropcopy data from the specified source within the pico datacenter using OAuth authentication to ensure authorized access.


## Conceptual Info

This node performs a secure retrieval of raw dropcopy data from a specific source within the pico datacenter. Leveraging OAuth authentication, it ensures authorized access, compliance with security protocols, and data integrity through cryptographic verification. The node transforms the validated source identification into a base64-encoded data payload along with metadata about retrieval time, data size, and success status.

## Docstring

### Summary
Retrieve raw dropcopy data securely from the identified pico datacenter source using OAuth authentication, returning the base64-encoded data along with provenance and integrity metadata.

### Parameters

- **identified_source** (dict): Output from 'identify_dropcopy_source' node containing the unique source_id, source URI, and accessibility verification used to locate and authenticate access to the dropcopy source.
- **oauth_credentials** (dict): Validated OAuth credentials (e.g., access tokens) required to authenticate the retrieval request securely within the pico datacenter environment.

### Returns

dict: A dictionary containing: 'raw_data_base64' (base64-encoded dropcopy content), 'source_id' (source identifier), 'retrieved_at' (ISO 8601 timestamp), 'size_bytes' (integer size of data), 'sha256_hash' (SHA-256 integrity hash), and 'retrieval_success' (boolean success indicator).

### Raises

- AuthenticationError: If OAuth credentials are invalid, expired, or insufficient for authorized data access.
- SourceAccessError: If the identified dropcopy source is inaccessible, not found, or access is denied.
- DataRetrievalError: If any error occurs during data transfer, corruption is detected, or data fails integrity checks.

### Examples

```python
>>> identified_source = {
...   'source_id': 'dc-12345',
...   'source_uri': '/datacenter/dropcopy/dc-12345',
...   'is_accessible': True
>>> }
>>> oauth_credentials = {'access_token': 'abc123token', 'token_type': 'Bearer'}
>>> pull_dropcopy(identified_source, oauth_credentials)
{
```
