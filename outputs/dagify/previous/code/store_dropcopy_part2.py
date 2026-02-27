from pydantic import BaseModel, Field
from typing import List


class ProcessDropcopyPart2Output(BaseModel):
    """Pydantic model for process_dropcopy_part2 node outputs."""
    trade_ids: List[str] = (
        Field(..., description="List of unique trade identifiers extracted from the dropcopy segment.")
    )
    prices: List[float] = Field(..., description="Corresponding trade prices.")
    volumes: List[int] = Field(..., description="Corresponding trade volumes.")
    symbols: List[str] = (
        Field(..., description="Stock or asset symbols associated with each trade.")
    )
    timestamps: List[str] = (
        Field(..., description="ISO 8601 timestamps of each trade.")
    )
    sides: List[str] = (
        Field(..., description="Trade side ('buy' or 'sell') for each trade.")
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


def store_dropcopy_part2(process_dropcopy_part2_input: ProcessDropcopyPart2Output, **kwargs) -> StoreDropcopyPart2Output:
    """
    Stores the processed second segment of dropcopy trade data in a secure,
    OAuth-authenticated repository, preserving data integrity and accessibility
    for downstream processes.

    Parameters
    ----------
    processed_segment : dict
        A dictionary containing the fully processed second segment of
        dropcopy data including trade IDs, prices, volumes, symbols,
        timestamps, and sides, prepared by the preceding processing node.
    oauth_credentials : dict
        Credentials and tokens necessary for OAuth authentication to
        authorize secure storage operations within the repository.
    repository_config : dict
        Configuration details including repository endpoint, access
        policies, and storage paths specifying where and how to store the
        processed data.

    Returns
    -------
    dict
        A dictionary containing storage details: 'stored_file_path' (storage
        location), 'record_count' (number of trades stored), 'storage_hash'
        (SHA-256 hash for integrity), 'storage_success' (boolean success
        flag), 'stored_timestamp' (ISO timestamp of storage event), and
        'trade_ids' (list of stored trade identifiers).

    Raises
    ------
    AuthenticationError
        Raised when OAuth authentication fails, preventing authorized access
        to the storage repository.
    StorageError
        Raised if the storage operation encounters failures such as network
        errors, permission denials, or write errors.
    ValueError
        Raised if the processed_segment is missing required trade
        information or is malformed.

    Examples
    --------
    >>> processed_segment = {
    ...     'trade_ids': ['T123', 'T124'],
    ...     'prices': [101.5, 102.0],
    ...     'volumes': [200, 150],
    ...     'symbols': ['AAPL', 'MSFT'],
    ...     'timestamps': ['2024-04-11T15:23:45Z', '2024-04-11T15:24:01Z'],
    ...     'sides': ['buy', 'sell']
    >>> }
    >>> oauth_credentials = {...}
    >>> repository_config = {'endpoint':
    'https://repo.example.com/dropcopy/part2'}
    >>> result = store_dropcopy_part2(processed_segment, oauth_credentials,
    repository_config)
    >>> print(result['storage_success'], result['record_count'],
    result['stored_file_path'])
    True 2
    'https://repo.example.com/dropcopy/part2/segment2_20240411T152345Z.json'

    """
    return StoreDropcopyPart2Output(
        stored_file_path="",
        record_count=0,
        storage_hash="",
        storage_success=False,
        stored_timestamp="",
        trade_ids=[],
    )