from pydantic import BaseModel, Field
from typing import List


class ConstructNasdaqApiRequestOutput(BaseModel):
    """Pydantic model for construct_nasdaq_api_request node outputs."""
    base_url: str = (
        Field(..., description="Base URL for the NASDAQ data service")
    )
    query_params: List[str] = (
        Field(..., description="List of query parameters for the request")
    )
    tls_settings: str = (
        Field(..., description="TLS settings for the request, including the cipher suite and HSTS enforcement")
    )
    latency_expectations: str = (
        Field(..., description="Expected latency for the request, in milliseconds")
    )
    retry_policy: str = (
        Field(..., description="Retry policy for the request, including the number of attempts and delay")
    )
    data_centers: List[str] = (
        Field(..., description="List of data centers for the request, including primary, secondary, and tertiary")
    )
    request_string: str = (
        Field(..., description="Full request string for the NASDAQ API")
    )
    full_url: str = (
        Field(..., description="Full URL for the NASDAQ API request")
    )
    expected_latency: float = (
        Field(..., description="Expected latency for the request, in milliseconds")
    )


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


def fetch_nasdaq_stock_data(construct_nasdaq_api_request_input: ConstructNasdaqApiRequestOutput, **kwargs) -> FetchNasdaqStockDataOutput:
    """
    Constructs a secure, protocol-compliant HTTP(S) request to the NASDAQ API
    and fetches the stock data over HTTPS.

    Parameters
    ----------
    api_request : str
        API request string
    timeout : int
        Timeout in seconds
    retry_policy : str
        Retry policy for handling 500-level server errors

    Returns
    -------
    dict
        Returns a dictionary containing the stock data in JSON format, API
        endpoint URI, query parameters, HTTP headers, latency, and data feed
        availability.

    Raises
    ------
    Exception
        Raises an exception if the API request fails or the timeout is
        exceeded

    Examples
    --------
    >>>
    fetch_nasdaq_stock_data(api_request='https://api.nasdaq.com/qsvc/v1/stocks',
    timeout=5, retry_policy='2')
    {"nasdaq_stock_data": ["{"symbol": "AAPL", "price": 150.0}"]}

    """
    return FetchNasdaqStockDataOutput(
        nasdaq_stock_data=[],
        nasdaq_api_endpoint="",
        nasdaq_query_params="",
        nasdaq_http_headers="",
        nasdaq_latency=0.0,
        nasdaq_data_feed_availability="",
    )