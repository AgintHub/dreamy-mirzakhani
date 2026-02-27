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


class ProcessDropcopyPart3Output(BaseModel):
    """Pydantic model for process_dropcopy_part3 node outputs."""
    metadata_keys: List[str] = (
        Field(..., description="List of metadata field names extracted from the dropcopy segment")
    )
    metadata_values: List[str] = (
        Field(..., description="Corresponding list of metadata field values as strings")
    )
    user_ids: List[str] = (
        Field(..., description="List of user identifiers extracted from the data segment")
    )
    timestamps: List[str] = (
        Field(..., description="List of timestamps in ISO 8601 string format associated with extracted events")
    )
    payload_contents: List[str] = (
        Field(..., description="Serialized JSON strings representing sanitized and normalized payload data items")
    )
    auth_states: List[str] = (
        Field(..., description="Chronological log entries of authentication states and token refresh events")
    )
    parse_metrics: List[str] = (
        Field(..., description="Logs and metrics related to parsing performance and encountered errors or warnings")
    )
    success: bool = (
        Field(..., description="Indicates whether the processing and extraction were successful without critical errors")
    )


def process_dropcopy_part3(pull_dropcopy_input: PullDropcopyOutput, **kwargs) -> ProcessDropcopyPart3Output:
    """
    Authenticate using OAuth 2.0 and securely process the third segment of
    dropcopy data from the pico datacenter. Validate and refresh tokens as
    needed, parse the data to extract metadata fields, user IDs, timestamps, and
    payloads; log authentication and parsing events; and output structured,
    sanitized results.

    Parameters
    ----------
    access_token : str
        OAuth 2.0 access token to authenticate and authorize access to the
        dropcopy segment.
    dropcopy_data_segment : str
        Raw data segment (typically base64-encoded or structured) of the
        third part of the dropcopy obtained from the pico datacenter.

    Returns
    -------
    dict
        Dictionary containing extracted fields: metadata_keys,
        metadata_values, user_ids, timestamps, payload_contents,
        auth_states, parse_metrics, and success flag indicating operation
        status.

    Raises
    ------
    AuthenticationError
        Raised if the access token is invalid and cannot be refreshed.
    DataParsingError
        Raised if the data segment cannot be parsed correctly or required
        fields are missing.
    TokenRefreshError
        Raised if an error occurs during token refresh.

    Examples
    --------
    >>> output = process_dropcopy_part3(
    ...     access_token='valid_oauth_token',
    ...     dropcopy_data_segment='base64_encoded_data_segment_here')
    >>> print(output['success'])
    True

    >>> result = process_dropcopy_part3(
    ...     access_token='expired_token',
    ...     dropcopy_data_segment='malformed_data_segment')
    >>> print(result['success'])
    False

    """
    return ProcessDropcopyPart3Output(
        metadata_keys=[],
        metadata_values=[],
        user_ids=[],
        timestamps=[],
        payload_contents=[],
        auth_states=[],
        parse_metrics=[],
        success=False,
    )