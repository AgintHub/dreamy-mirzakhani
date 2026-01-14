from pydantic import BaseModel, Field
from typing import List


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


class ParseNyseStockDataOutput(BaseModel):
    """Pydantic model for parse_nyse_stock_data node outputs."""
    timestamp: str = (
        Field(..., description="ISO\u20118601 UTC of record ingestion")
    )
    exchange: str = Field(..., description="NYSE")
    symbol: str = Field(..., description="ticker symbol")
    price: float = Field(..., description="last traded price (float)")
    volume: int = Field(..., description="total traded volume (integer)")
    metadata: str = (
        Field(..., description="object containing `latency_ms`, `datacenter`, and `source_url`")
    )


class ParseTorontoStockExchangeStockDataOutput(BaseModel):
    """Pydantic model for parse_toronto_stock_exchange_stock_data node outputs."""
    ticker: str = Field(..., description="Ticker symbol.")
    timestamp: str = (
        Field(..., description="Exact trade timestamp (ISO 8601 UTC)")
    )
    open: float = Field(..., description="Opening price.")
    high: float = Field(..., description="Highest price during the interval.")
    low: float = Field(..., description="Lowest price during the interval.")
    close: float = Field(..., description="Closing price.")
    volume: int = Field(..., description="Traded volume.")
    adjusted_close: float = (
        Field(..., description="Adjusted close for splits/dividends.")
    )


class StoreCombinedStockDataOutput(BaseModel):
    """Pydantic model for store_combined_stock_data node outputs."""
    schema_validated: bool = (
        Field(..., description="Whether the data is schema-validated")
    )
    versioning_status: str = (
        Field(..., description="Current versioning status of the data lake")
    )
    ingestion_latency_ms: int = (
        Field(..., description="Latency of data ingestion in milliseconds")
    )
    data_lake_region: str = (
        Field(..., description="Region where the data lake is located")
    )
    data_lake_size_gb: float = (
        Field(..., description="Current size of the data lake in GB")
    )


def store_combined_stock_data(parse_lse_stock_data_input: ParseLseStockDataOutput, parse_nasdaq_stock_data_input: ParseNasdaqStockDataOutput, parse_nyse_stock_data_input: ParseNyseStockDataOutput, parse_toronto_stock_exchange_stock_data_input: ParseTorontoStockExchangeStockDataOutput, **kwargs) -> StoreCombinedStockDataOutput:
    """
    Store the combined stock data in a geo-distributed data lake with strict
    schema validation, versioning, and low-latency ingestion.

    Parameters
    ----------
    lse_data : List[str]
        LSE stock data from `parse_lse_stock_data` node.
    nasdaq_data : List[str]
        NASDAQ stock data from `parse_nasdaq_stock_data` node.
    nyse_data : List[str]
        NYSE stock data from `parse_nyse_stock_data` node.
    tsx_data : List[str]
        TSX stock data from `parse_toronto_stock_exchange_stock_data` node.

    Returns
    -------
    Dict[str, str]
        Dictionary containing boolean indicating schema validation, current
        versioning status, ingestion latency, data lake region, and current
        data lake size.

    Raises
    ------
    ValueError
        If input data is not in the correct format.

    Examples
    --------
    >>> lse_data = parse_lse_stock_data(fetch_lse_stock_data())
    >>> nasdaq_data = parse_nasdaq_stock_data(fetch_nasdaq_stock_data())
    >>> nyse_data = parse_nyse_stock_data(fetch_nyse_stock_data())
    >>> tsx_data = parse_toronto_stock_exchange_stock_data(fetch_toronto_stock_e
    xchange_stock_data())
    >>> store_combined_stock_data(lse_data, nasdaq_data, nyse_data, tsx_data)
    {schema_validated: True, versioning_status: Version 1.0,
    ingestion_latency_ms: 100, data_lake_region: US East, data_lake_size_gb:
    100.0}

    """
    return StoreCombinedStockDataOutput(
        schema_validated=False,
        versioning_status="",
        ingestion_latency_ms=0,
        data_lake_region="",
        data_lake_size_gb=0.0,
    )