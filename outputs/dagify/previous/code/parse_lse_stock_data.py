from pydantic import BaseModel, Field
from typing import List


class FetchLseStockDataOutput(BaseModel):
    """Pydantic model for fetch_lse_stock_data node outputs."""
    raw_data: str = (
        Field(..., description="The raw JSON data received from the LSE API.")
    )
    error: bool = (
        Field(..., description="Whether any errors occurred during the data fetch operation.")
    )
    latency: float = (
        Field(..., description="The average latency experienced during the data fetch operation.")
    )
    datacenter: str = (
        Field(..., description="The datacenter used to fetch the data (one of London, New York, or Singapore).")
    )


class ParseLseStockDataOutput(BaseModel):
    """Pydantic model for parse_lse_stock_data node outputs."""
    lse_api_response: str = (
        Field(..., description="The raw API response from the LSE")
    )
    dataframe_rows: List[str] = (
        Field(..., description="The rows of the parsed Pandas DataFrame as a list of strings")
    )
    protocol_used: str = (
        Field(..., description="The protocol used for fetching the LSE stock data")
    )
    fetch_latency_ms: float = (
        Field(..., description="The latency in milliseconds for fetching the LSE stock data")
    )
    datacenter_origin: str = (
        Field(..., description="The datacenter origin of the LSE stock data")
    )


def parse_lse_stock_data(fetch_lse_stock_data_input: FetchLseStockDataOutput, **kwargs) -> ParseLseStockDataOutput:
    """Transforms raw LSE stock data fetched via HTTPS into a sanitized, schema-validated Pandas DataFrame, enriching the output with protocol, latency, and datacenter provenance for downstream analytics and SLA monitoring.

    Args:
        fetch_lse_stock_data_input: Input from the 'fetch_lse_stock_data' node.
        **kwargs: Additional keyword arguments.

    Returns:
        ParseLseStockDataOutput: Object containing outputs for this node.
    """
    # TODO: Implement this function

    # Return stub output with placeholder values
    return ParseLseStockDataOutput(
        lse_api_response="",
        dataframe_rows=[],
        protocol_used="",
        fetch_latency_ms=0.0,
        datacenter_origin="",
    )