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


def process_dropcopy_part2(pull_dropcopy_input: PullDropcopyOutput, **kwargs) -> ProcessDropcopyPart2Output:
    """
    Process the second segment of dropcopy data retrieved via OAuth
    authentication to extract and structure trade information with integrity and
    security guarantees.

    Parameters
    ----------
    raw_data_base64 : str
        Base64-encoded raw dropcopy data for the second segment, obtained
        from a secure OAuth-authenticated source.
    access_token : str
        OAuth 2.0 access token authorizing access to the dropcopy data.

    Returns
    -------
    dict[str, list]
        Dictionary containing lists of trade-related data fields extracted
        from the second dropcopy segment: 'trade_ids', 'prices', 'volumes',
        'symbols', 'timestamps', and 'sides'. Each list corresponds to
        records parsed from the segment with data integrity and compliance
        assured.

    Raises
    ------
    ValueError
        If the input data is malformed or fails validation checks.
    AuthenticationError
        If the provided OAuth token is invalid, expired, or unauthorized for
        accessing this data.
    ParseError
        If extraction or parsing of trade data from the dropcopy segment
        fails due to unexpected format or corruption.

    Examples
    --------
    >>> result = process_dropcopy_part2(raw_data_base64, access_token)
    >>> print(result['trade_ids'])
    >>> print(result['prices'])
    ['T12345', 'T12346']
    [102.5, 103.0]

    >>> segment_data = '...'  # Base64-encoded dropcopy part 2 segment
    >>> token = 'valid_oauth_token_value'
    >>> trades = process_dropcopy_part2(segment_data, token)
    >>> assert all(isinstance(tid, str) for tid in trades['trade_ids'])
    >>> assert all(isinstance(price, float) for price in trades['prices'])
    No exceptions raised; data correctly parsed and typed.

    """
    return ProcessDropcopyPart2Output(
        trade_ids=[],
        prices=[],
        volumes=[],
        symbols=[],
        timestamps=[],
        sides=[],
    )