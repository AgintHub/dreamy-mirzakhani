from pydantic import BaseModel, Field
from typing import List


class StoreDropcopyPart1Output(BaseModel):
    """Pydantic model for store_dropcopy_part1 node outputs."""
    file_path: str = (
        Field(..., description="The file system or repository path where the processed dropcopy segment was stored.")
    )
    is_successful: bool = (
        Field(..., description="Indicates whether the storage operation succeeded.")
    )
    records_stored: int = (
        Field(..., description="The number of records or entries stored from the processed dropcopy segment.")
    )
    storage_timestamp: str = (
        Field(..., description="Timestamp (ISO 8601 format) indicating when the storage operation was completed.")
    )
    error_message: str = (
        Field(..., description="Error message if the storage operation failed; empty string if successful.")
    )


class StoreDropcopyPart2Output(BaseModel):
    """Pydantic model for store_dropcopy_part2 node outputs."""
    stored_file_path: str = (
        Field(..., description="Repository path or URL where the processed second segment was stored.")
    )
    record_count: int = (
        Field(..., description="Number of trade records stored.")
    )
    storage_hash: str = (
        Field(..., description="SHA-256 hash of the stored file for integrity verification.")
    )
    storage_success: bool = (
        Field(..., description="True if storage succeeded, False otherwise.")
    )
    stored_timestamp: str = (
        Field(..., description="ISO 8601 timestamp of when the file was stored.")
    )
    trade_ids: List[str] = (
        Field(..., description="List of trade IDs included in the stored segment.")
    )


class StoreDropcopyPart3Output(BaseModel):
    """Pydantic model for store_dropcopy_part3 node outputs."""
    stored_file_path: str = (
        Field(..., description="The repository path where the processed dropcopy part 3 was stored.")
    )
    record_count: int = (
        Field(..., description="The number of records stored from the processed dropcopy part 3.")
    )
    checksum: str = (
        Field(..., description="The SHA-256 checksum of the stored file to verify data integrity.")
    )
    stored_at: str = (
        Field(..., description="The ISO 8601 timestamp when the file was stored.")
    )
    is_success: bool = (
        Field(..., description="Whether the storage operation succeeded without errors.")
    )


class MergeStoredDropcopyOutput(BaseModel):
    """Pydantic model for merge_stored_dropcopy node outputs."""
    merged_dataset_id: str = (
        Field(..., description="Unique identifier or repository path of the merged dropcopy dataset.")
    )
    record_count: int = (
        Field(..., description="Total number of records aggregated into the merged dataset.")
    )
    total_size_bytes: int = (
        Field(..., description="Total size of the merged dataset in bytes.")
    )
    merge_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when the merge operation was completed.")
    )
    merge_success: bool = (
        Field(..., description="Indicates whether the merge operation completed successfully.")
    )
    part1_id: str = (
        Field(..., description="Identifier of the stored first segment of the dropcopy.")
    )
    part2_id: str = (
        Field(..., description="Identifier of the stored second segment of the dropcopy.")
    )
    part3_id: str = (
        Field(..., description="Identifier of the stored third segment of the dropcopy.")
    )
    checksum: str = (
        Field(..., description="Cryptographic hash (e.g., SHA-256) of the merged dataset for integrity verification.")
    )


def merge_stored_dropcopy(store_dropcopy_part1_input: StoreDropcopyPart1Output, store_dropcopy_part2_input: StoreDropcopyPart2Output, store_dropcopy_part3_input: StoreDropcopyPart3Output, **kwargs) -> MergeStoredDropcopyOutput:
    """
    Merge three stored segments of a dropcopy into a consolidated dataset within
    the repository ensuring data consistency, integrity, and traceability.

    Parameters
    ----------
    part1_info : dict
        Metadata and storage details of the first dropcopy segment,
        including its unique identifier and record count.
    part2_info : dict
        Metadata and storage details of the second dropcopy segment,
        including its unique identifier and record count.
    part3_info : dict
        Metadata and storage details of the third dropcopy segment,
        including its unique identifier and record count.
    oauth_token : str
        OAuth access token used to securely authenticate merging operations
        in the repository.

    Returns
    -------
    dict
        A dictionary containing merged dataset identifier, total record
        count, size in bytes, timestamp of merge completion, success flag,
        identifiers of each original segment, and a cryptographic checksum
        of the merged dataset.

    Raises
    ------
    ValueError
        Raised if any of the dropcopy segments' metadata is missing or
        malformed.
    AuthenticationError
        Raised if OAuth authentication fails or token is invalid/expired.
    MergeOperationError
        Raised if the merge process encounters data consistency errors or
        fails to complete.

    Examples
    --------
    >>> part1 = {'file_path': 'repo/path/segment1', 'is_successful': True,
    'records_stored': 1000, 'storage_timestamp': '2024-06-01T10:00:00Z',
    'error_message': ''}
    >>> part2 = {'stored_file_path': 'repo/path/segment2', 'record_count': 1500,
    'storage_hash': 'abc123', 'storage_success': True, 'stored_timestamp':
    '2024-06-01T10:05:00Z', 'trade_ids': ['t1', 't2']}
    >>> part3 = {'stored_file_path': 'repo/path/segment3', 'record_count': 1200,
    'checksum': 'def456', 'stored_at': '2024-06-01T10:10:00Z', 'is_success':
    True}
    >>> result = merge_stored_dropcopy(part1, part2, part3,
    oauth_token='token123')
    >>> print(result['merge_success'], result['record_count'])
    True 3700

    >>> part1 = {'file_path': 'repo/path/segment1', 'is_successful': True,
    'records_stored': 100, 'storage_timestamp': '2024-06-02T08:00:00Z',
    'error_message': ''}
    >>> part2 = {'stored_file_path': 'repo/path/segment2', 'record_count': 200,
    'storage_hash': 'xyz789', 'storage_success': True, 'stored_timestamp':
    '2024-06-02T08:05:00Z', 'trade_ids': ['t10', 't11']}
    >>> part3 = {'stored_file_path': 'repo/path/segment3', 'record_count': 150,
    'checksum': 'uvw123', 'stored_at': '2024-06-02T08:10:00Z', 'is_success':
    True}
    >>> result = merge_stored_dropcopy(part1, part2, part3,
    oauth_token='tokenXYZ')
    >>> print(result['merged_dataset_id'])
    'repo/merged/dropcopy_20240602T081000Z'

    """
    return MergeStoredDropcopyOutput(
        merged_dataset_id="",
        record_count=0,
        total_size_bytes=0,
        merge_timestamp="",
        merge_success=False,
        part1_id="",
        part2_id="",
        part3_id="",
        checksum="",
    )