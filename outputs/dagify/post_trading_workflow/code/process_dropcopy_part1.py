from pydantic import BaseModel, Field
from typing import List


class PullDropcopyOutput(BaseModel):
    """Pydantic model for pull_dropcopy node outputs."""
    raw_data_base64: str = (
        Field(..., description="Base64-encoded raw dropcopy data retrieved from the source.")
    )
    source_id: str = (
        Field(..., description="Identifier of the dropcopy source, as determined by identify_dropcopy_source node.")
    )
    retrieved_at: str = (
        Field(..., description="ISO 8601 timestamp of when the dropcopy was retrieved.")
    )
    size_bytes: int = (
        Field(..., description="Total size in bytes of the retrieved dropcopy data.")
    )
    sha256_hash: str = (
        Field(..., description="SHA-256 hash of the retrieved dropcopy data for integrity verification.")
    )
    retrieval_success: bool = (
        Field(..., description="Indicates whether the dropcopy retrieval succeeded without errors.")
    )


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


def process_dropcopy_part1(pull_dropcopy_input: PullDropcopyOutput, **kwargs) -> ProcessDropcopyPart1Output:
    """
    Processes the initial segment of dropcopy data securely using OAuth
    authentication to extract structured trade and market details, validating
    and aggregating the information for downstream use.

    Parameters
    ----------
    raw_data_base64 : str
        Base64-encoded raw dropcopy data for the first segment retrieved
        securely from the pico datacenter.
    access_token : str
        OAuth 2.0 access token used to authenticate the data access and
        processing requests.

    Returns
    -------
    dict
        A dictionary containing parsed and validated trade data fields
        including part number, record count, lists of transaction IDs,
        instrument IDs, sides, volumes, prices, timestamps, a validity flag
        for extraction success, total volume, and average trade price for
        the processed segment.

    Raises
    ------
    ValueError
        If the input raw_data_base64 is empty or improperly encoded.
    AuthenticationError
        If OAuth access_token is invalid or expired, denying secure access.
    ParsingError
        If extracted data cannot be parsed or validated correctly.

    Examples
    --------
    >>> result =
    process_dropcopy_part1(raw_data_base64='QmFzZTY0RW5jb2RlZERhdGE=',
    access_token='valid_oauth_token')
    >>> print(result['part_number'], result['record_count'],
    result['total_volume'], result['average_price'])
    1 10 1500 25.75

    >>> result = process_dropcopy_part1(raw_data_base64='VGhpcyBpcyBhIHRlc3Q=',
    access_token='valid_oauth_token')
    >>> assert result['is_valid'] is True
    >>> assert len(result['transaction_ids']) == result['record_count']
    True

    """
    return ProcessDropcopyPart1Output(
        part_number=0,
        record_count=0,
        transaction_ids=[],
        instrument_ids=[],
        sides=[],
        trade_volumes=[],
        trade_prices=[],
        trade_timestamps=[],
        is_valid=False,
        total_volume=0,
        average_price=0.0,
    )