from pydantic import BaseModel, Field
from typing import List


class FetchNasdaqStockDataOutput(BaseModel):
    """Pydantic model for fetch_nasdaq_stock_data node outputs."""
    nasdaq_stock_data: List[str] = (
        Field(..., description="List of stock data in JSON format fetched from the NASDAQ API")
    )
    nasdaq_api_endpoint: str = (
        Field(..., description="API endpoint URI of the NASDAQ API")
    )
    nasdaq_query_params: str = (
        Field(..., description="Query parameters used to specify stock symbols and date ranges")
    )
    nasdaq_http_headers: str = (
        Field(..., description="HTTP headers used for authentication and rate limiting")
    )
    nasdaq_latency: float = (
        Field(..., description="Latency of the data feed in milliseconds")
    )
    nasdaq_data_feed_availability: str = (
        Field(..., description="Metadata on data feed availability, including server response times and error messages")
    )


class ParseNasdaqStockDataOutput(BaseModel):
    """Pydantic model for parse_nasdaq_stock_data node outputs."""
    symbol: str = Field(..., description="Stock symbol.")
    date: str = Field(..., description="ISO-8601 UTC date.")
    open: float = Field(..., description="Opening price.")
    high: float = Field(..., description="Highest price during the interval.")
    low: float = Field(..., description="Lowest price during the interval.")
    close: float = Field(..., description="Closing price.")
    volume: int = Field(..., description="Traded volume.")
    adjusted_close: float = (
        Field(..., description="Adjusted close for splits/dividends.")
    )
    market_cap: float = Field(..., description="Market capitalization.")
    source_datacenter: str = Field(..., description="Datacenter origin.")
    fetch_latency_ms: int = (
        Field(..., description="Fetch latency in milliseconds.")
    )
    parse_duration_ms: int = (
        Field(..., description="Parse duration in milliseconds.")
    )


def parse_nasdaq_stock_data(fetch_nasdaq_stock_data_input: FetchNasdaqStockDataOutput, **kwargs) -> ParseNasdaqStockDataOutput:
    """Converts raw NASDAQ API responses into a clean, structured dataset. Handles protocol-level details such as datacenter origin, fetch latency, and parse timing, while ensuring data integrity and compliance with the feed’s latency SLAs.

    Args:
        fetch_nasdaq_stock_data_input: Input from the 'fetch_nasdaq_stock_data' node.
        **kwargs: Additional keyword arguments.

    Returns:
        ParseNasdaqStockDataOutput: Object containing outputs for this node.
    """
    # TODO: Implement this function

    # Return stub output with placeholder values
    return ParseNasdaqStockDataOutput(
        symbol="",
        date="",
        open=0.0,
        high=0.0,
        low=0.0,
        close=0.0,
        volume=0,
        adjusted_close=0.0,
        market_cap=0.0,
        source_datacenter="",
        fetch_latency_ms=0,
        parse_duration_ms=0,
    )