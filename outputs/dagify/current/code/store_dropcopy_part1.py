from pydantic import BaseModel, Field
from typing import List


class ProcessDropcopyPart1Output(BaseModel):
    """Pydantic model for process_dropcopy_part1 node outputs."""
    part_number: int = (
        Field(..., description="Identifier for the part of the dropcopy being processed.")
    )
    record_count: int = (
        Field(..., description="Number of trade records extracted from this part.")
    )
    transaction_ids: List[str] = (
        Field(..., description="List of transaction identifiers extracted from this part.")
    )
    instrument_ids: List[str] = (
        Field(..., description="List of instrument identifiers corresponding to each trade.")
    )
    sides: List[str] = (
        Field(..., description="List indicating the trade side ('buy' or 'sell') for each record.")
    )
    trade_volumes: List[int] = (
        Field(..., description="List of trade volumes (number of units) for each record.")
    )
    trade_prices: List[float] = (
        Field(..., description="List of trade prices per unit for each record.")
    )
    trade_timestamps: List[str] = (
        Field(..., description="ISO 8601 timestamps for each trade record.")
    )
    is_valid: bool = (
        Field(..., description="Flag indicating whether the extraction and parsing were successful.")
    )
    total_volume: int = (
        Field(..., description="Total volume of all trades in this part.")
    )
    average_price: float = (
        Field(..., description="Average trade price for this part.")
    )


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


def store_dropcopy_part1(process_dropcopy_part1_input: ProcessDropcopyPart1Output, **kwargs) -> StoreDropcopyPart1Output:
    """
    Stores the first processed segment of dropcopy data securely in a repository
    using OAuth authentication, ensuring access control and data integrity.

    Parameters
    ----------
    processed_segment : dict
        A dictionary containing the processed first segment of the dropcopy
        data including structured trade records, volumes, prices, and
        timestamps, as produced by the `process_dropcopy_part1` node.
    oauth_credentials : dict
        OAuth credentials (e.g., access tokens) required to authenticate and
        authorize access to the secure storage repository.

    Returns
    -------
    dict
        A dictionary with keys: `file_path` (str) where data is stored,
        `is_successful` (bool) indicating storage success, `records_stored`
        (int) number of records stored, `storage_timestamp` (str) ISO 8601
        timestamp of storage completion, and `error_message` (str) detailing
        any failure cause or empty if successful.

    Raises
    ------
    AuthenticationError
        Raised if OAuth authentication fails or credentials are invalid.
    StorageError
        Raised if storage fails due to network issues, permission errors, or
        data integrity problems.
    ValueError
        Raised if the processed segment data is empty, malformed, or missing
        required fields.

    Examples
    --------
    >>> processed_segment = {
    ...     'part_number': 1,
    ...     'record_count': 100,
    ...     'transaction_ids': ['tx123', 'tx124', 'tx125'],
    ...     'instrument_ids': ['instA', 'instB', 'instC'],
    ...     'sides': ['buy', 'sell', 'buy'],
    ...     'trade_volumes': [1000, 500, 750],
    ...     'trade_prices': [10.5, 10.7, 10.6],
    ...     'trade_timestamps': ['2024-06-01T12:00:00Z', '2024-06-01T12:01:00Z',
    '2024-06-01T12:02:00Z'],
    ...     'is_valid': True,
    ...     'total_volume': 2250,
    ...     'average_price': 10.6
    >>> }
    >>> oauth_credentials = {'access_token': 'abc123', 'token_type': 'Bearer'}
    >>> result = store_dropcopy_part1(processed_segment, oauth_credentials)
    {'file_path': '/repo/dropcopy/part1_20240601.json', 'is_successful': True,
    'records_stored': 100, 'storage_timestamp': '2024-06-01T12:05:00Z',
    'error_message': ''}

    >>> invalid_segment = {}
    >>> oauth_credentials = {'access_token': 'abc123', 'token_type': 'Bearer'}
    >>> result = store_dropcopy_part1(invalid_segment, oauth_credentials)
    Traceback (most recent call last):
      ...
    ValueError: Processed segment data is empty or malformed.

    """
    return StoreDropcopyPart1Output(
        file_path="",
        is_successful=False,
        records_stored=0,
        storage_timestamp="",
        error_message="",
    )