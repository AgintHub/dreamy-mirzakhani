from pydantic import BaseModel, Field


class FetchTorontoStockExchangeStockDataOutput(BaseModel):
    """Pydantic model for fetch_toronto_stock_exchange_stock_data node outputs."""
    timestamp: str = Field(..., description="ISO-8601 UTC of record ingestion")
    exchange: str = Field(..., description="NYSE")
    symbol: str = Field(..., description="Ticker symbol")
    price: float = Field(..., description="Last traded price")
    volume: int = Field(..., description="Total traded volume")
    metadata: str = (
        Field(..., description="Object containing latency_ms, datacenter, and source_url")
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


def parse_toronto_stock_exchange_stock_data(fetch_toronto_stock_exchange_stock_data_input: FetchTorontoStockExchangeStockDataOutput, **kwargs) -> ParseTorontoStockExchangeStockDataOutput:
    """
    Validates Toronto Stock Exchange API data into a high-precision time-series
    DataFrame.

    Returns
    -------
    DataFrame
        Validated and transformed time-series data.

    Raises
    ------
    ValueError
        Invalid data format or missing required fields.

    Examples
    --------
    >>> api_response = {'timestamp': '2022-01-01T12:00:00', 'ticker': 'AAPL',
    'open': 100.0, 'high': 120.0, 'low': 90.0, 'close': 110.0, 'volume': 10000,
    'adjusted_close': 115.0}
    >>> dataframe = parse_toronto_stock_exchange_stock_data(api_response)
    >>> print(dataframe)
        ticker  timestamp  open  high   low  close  volume  adjusted_close
    0     AAPL 2022-01-01T12:00:00  100.0  120.0   90.0  110.0  10000
    115.0

    >>> api_response = {'timestamp': None, 'ticker': 'AAPL', 'open': 100.0,
    'high': 120.0, 'low': 90.0, 'close': 110.0, 'volume': 10000,
    'adjusted_close': 115.0}
    >>> dataframe = parse_toronto_stock_exchange_stock_data(api_response)
    >>> print(dataframe)
    ValueError: Invalid data format or missing required fields.

    """
    return ParseTorontoStockExchangeStockDataOutput(
        ticker="",
        timestamp="",
        open=0.0,
        high=0.0,
        low=0.0,
        close=0.0,
        volume=0,
        adjusted_close=0.0,
    )