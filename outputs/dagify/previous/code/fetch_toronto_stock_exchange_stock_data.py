from pydantic import BaseModel, Field


class ConstructTorontoStockExchangeApiRequestOutput(BaseModel):
    """Pydantic model for construct_toronto_stock_exchange_api_request node outputs."""
    api_request_string: str = (
        Field(..., description="The constructed API request string")
    )
    api_endpoint: str = (
        Field(..., description="The API endpoint URL for the Toronto Stock Exchange")
    )
    user_agent_header: str = (
        Field(..., description="The User-Agent header value for the API request")
    )
    api_key_authentication: str = (
        Field(..., description="The API key authentication token for the Toronto Stock Exchange API")
    )
    tls_settings: str = (
        Field(..., description="The TLS settings, including the protocol version and cipher suite, for the API request")
    )
    latency_expectation: int = (
        Field(..., description="The expected latency for the API request, in milliseconds")
    )
    data_centers: str = (
        Field(..., description="The list of available data centers for the Toronto Stock Exchange API, including Toronto, New York, and London")
    )


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


def fetch_toronto_stock_exchange_stock_data(construct_toronto_stock_exchange_api_request_input: ConstructTorontoStockExchangeApiRequestOutput, **kwargs) -> FetchTorontoStockExchangeStockDataOutput:
    """
    Perform HTTPS GET request to the Toronto Stock Exchange data service with
    specified query parameters and authentication headers.

    Parameters
    ----------
    api_request : str
        Fully constructed API request

    Returns
    -------
    dict[str, any]
        Parsed JSON response from the TSE API

    Raises
    ------
    requests.RequestException
        If there is a problem with the HTTPS request
    json.JSONDecodeError
        If the response is not valid JSON

    Examples
    --------
    >>> response = fetch_toronto_stock_exchange_stock_data('api_request')
    {'timestamp': '2023-03-01 10:00:00', 'exchange': 'NYSE', 'symbol': 'AAPL',
    'price': 100.0, 'volume': 1000, 'metadata': {'latency_ms': 80, 'datacenter':
    'Toronoto', 'source_url': 'https://api.tse.ca/v1/quotes'}

    """
    return FetchTorontoStockExchangeStockDataOutput(
        timestamp="",
        exchange="",
        symbol="",
        price=0.0,
        volume=0,
        metadata="",
    )