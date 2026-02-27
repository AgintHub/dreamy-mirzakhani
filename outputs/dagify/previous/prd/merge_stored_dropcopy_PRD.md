# merge_stored_dropcopy PRD

## Description
Integrate and consolidate the three individually stored, processed segments of the dropcopy into a unified, comprehensive repository entry. This merged dataset serves as a definitive source for subsequent verification and analysis, ensuring data integrity and coherence across the combined parts.


## Conceptual Info

This node securely consolidates the three individually stored and processed segments of the dropcopy dataset into a single, comprehensive merged dataset within a repository. Leveraging OAuth authentication for secure access, it verifies the integrity and consistency of the combined data segments, aggregating records, calculating total size, and generating a cryptographic checksum. The output merged dataset acts as a canonical source for subsequent verification and analysis pipelines.

## Docstring

### Summary
Merge three stored segments of a dropcopy into a consolidated dataset within the repository ensuring data consistency, integrity, and traceability.

### Parameters

- **part1_info** (dict): Metadata and storage details of the first dropcopy segment, including its unique identifier and record count.
- **part2_info** (dict): Metadata and storage details of the second dropcopy segment, including its unique identifier and record count.
- **part3_info** (dict): Metadata and storage details of the third dropcopy segment, including its unique identifier and record count.
- **oauth_token** (str): OAuth access token used to securely authenticate merging operations in the repository.

### Returns

dict: A dictionary containing merged dataset identifier, total record count, size in bytes, timestamp of merge completion, success flag, identifiers of each original segment, and a cryptographic checksum of the merged dataset.

### Raises

- ValueError: Raised if any of the dropcopy segments' metadata is missing or malformed.
- AuthenticationError: Raised if OAuth authentication fails or token is invalid/expired.
- MergeOperationError: Raised if the merge process encounters data consistency errors or fails to complete.

### Examples

```python
>>> part1 = {'file_path': 'repo/path/segment1', 'is_successful': True, 'records_stored': 1000, 'storage_timestamp': '2024-06-01T10:00:00Z', 'error_message': ''}
>>> part2 = {'stored_file_path': 'repo/path/segment2', 'record_count': 1500, 'storage_hash': 'abc123', 'storage_success': True, 'stored_timestamp': '2024-06-01T10:05:00Z', 'trade_ids': ['t1', 't2']}
>>> part3 = {'stored_file_path': 'repo/path/segment3', 'record_count': 1200, 'checksum': 'def456', 'stored_at': '2024-06-01T10:10:00Z', 'is_success': True}
>>> result = merge_stored_dropcopy(part1, part2, part3, oauth_token='token123')
>>> print(result['merge_success'], result['record_count'])
True 3700
```

```python
>>> part1 = {'file_path': 'repo/path/segment1', 'is_successful': True, 'records_stored': 100, 'storage_timestamp': '2024-06-02T08:00:00Z', 'error_message': ''}
>>> part2 = {'stored_file_path': 'repo/path/segment2', 'record_count': 200, 'storage_hash': 'xyz789', 'storage_success': True, 'stored_timestamp': '2024-06-02T08:05:00Z', 'trade_ids': ['t10', 't11']}
>>> part3 = {'stored_file_path': 'repo/path/segment3', 'record_count': 150, 'checksum': 'uvw123', 'stored_at': '2024-06-02T08:10:00Z', 'is_success': True}
>>> result = merge_stored_dropcopy(part1, part2, part3, oauth_token='tokenXYZ')
>>> print(result['merged_dataset_id'])
'repo/merged/dropcopy_20240602T081000Z'
```
