# verify_dropcopy_integrity PRD

## Description
Perform a comprehensive integrity verification of the consolidated dropcopy dataset by cryptographically validating its authenticity and ensuring it remains untampered since merging. This process confirms data consistency and trustworthiness following the aggregation of all processed dropcopy parts into a single repository entry.


## Conceptual Info

This node performs a secure, OAuth-authenticated cryptographic integrity check on the unified dropcopy dataset. By validating the authenticity and confirming that the data has not been altered since merging, it ensures the dataset's consistency, trustworthiness, and compliance with data integrity requirements before downstream processing or stakeholder notification.

## Docstring

### Summary
Verify the cryptographic integrity and authenticity of the consolidated dropcopy dataset using OAuth-secured access tokens. Confirm that the merged dataset remains untampered and consistent since its aggregation.

### Parameters

- **merged_dataset_id** (str): Unique identifier or repository path of the consolidated dropcopy dataset to be verified.
- **oauth_access_token** (str): OAuth-secured access token permitting authorized access to the dataset repository.
- **expected_checksum** (str): Cryptographic hash (e.g., SHA-256) of the merged dataset used as the benchmark for integrity verification.

### Returns

dict: Dictionary with the verification results including is_integrity_valid (bool), validation_timestamp (str, ISO 8601), validation_method (str), and details_message (str) providing context or errors.

### Raises

- AuthenticationError: Raised when OAuth authentication fails or access token is invalid/expired.
- DatasetNotFoundError: Raised when the merged dropcopy dataset cannot be located using the provided identifier.
- IntegrityVerificationError: Raised when the checksum verification fails or cannot be performed due to corrupted or inaccessible data.

### Examples

```python
>>> verify_dropcopy_integrity(
...     merged_dataset_id='repo/dropcopy/merged_20240101',
...     oauth_access_token='eyJhbGciOiJIUzI1...',
...     expected_checksum='3a7bd3e2360a8f8e1725b7c65d5e8e8b2c66f8bdf36e1f79a4d30233f4b37a7d'
>>> )
{
```
