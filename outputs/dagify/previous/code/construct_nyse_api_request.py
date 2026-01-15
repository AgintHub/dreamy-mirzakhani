from pydantic import BaseModel, Field
from typing import List


class IdentifyNyseStocksOutput(BaseModel):
    """Pydantic model for identify_nyse_stocks node outputs."""
    NYSE_equities: List[str] = Field(..., description="List of NYSE equities")
    equity_count: int = Field(..., description="Total number of NYSE equities")
    fetch_success: bool = (
        Field(..., description="Whether the data fetch operation was successful")
    )


class ConstructNyseApiRequestOutput(BaseModel):
    """Pydantic model for construct_nyse_api_request node outputs."""
    nyse_api_request_string: str = (
        Field(..., description="The constructed NYSE API request string.")
    )
    api_endpoint: str = (
        Field(..., description="The API endpoint URL for the NYSE stock data.")
    )
    user_agent_header: str = (
        Field(..., description="The User-Agent header value for the API request.")
    )
    api_key_authentication: str = (
        Field(..., description="The API key authentication token for the NYSE API.")
    )
    tls_settings: str = (
        Field(..., description="The TLS settings, including the protocol version and cipher suite, for the API request.")
    )
    data_centers: List[str] = (
        Field(..., description="The list of available data centers for the NYSE API, including New York (NY4), Chicago (CH1), and London (LD4).")
    )
    latency_expectation: int = (
        Field(..., description="The expected latency for the NYSE API request, in milliseconds.")
    )
    retry_policy: str = (
        Field(..., description="The retry policy for the NYSE API request, including the number of retries and the backoff strategy.")
    )
    error_handling_mechanisms: str = (
        Field(..., description="The comprehensive set of error handling mechanisms, including failure analysis and mitigation strategies.")
    )


def construct_nyse_api_request(identify_nyse_stocks_input: IdentifyNyseStocksOutput, **kwargs) -> ConstructNyseApiRequestOutput:
    """
    Constructs the NYSE API request string.

    Parameters
    ----------
    api_endpoint : str
        The base URL of the NYSE API.
    stock_symbols : List[str]
        The list of stock symbols to query.
    date_range : str
        The date range for the data query.
    data_frequency : str
        The data frequency, such as 1-minute or daily bars.
    api_key_authentication : str
        The API key authentication token for the NYSE API.
    user_agent_header : str
        The User-Agent header value for the API request.
    tls_settings : str
        The TLS settings, including the protocol version and cipher suite,
        for the API request.
    retry_policy : str
        The retry policy for the NYSE API request, including the number of
        retries and the backoff strategy.

    Returns
    -------
    nyse_api_request_string
        The constructed NYSE API request string.

    Raises
    ------
    ValueError
        If any of the required inputs are missing or invalid.
    ConnectionError
        If there is a connection issue with the NYSE API.

    Examples
    --------
    >>> stock_symbols = ['AAPL', 'GOOG', 'MSFT']
    >>> date_range = '2020-01-01:2020-01-31'
    >>> data_frequency = '1min'
    >>> api_key_authentication = 'your_api_key'
    >>> user_agent_header = 'Your-User-Agent'
    >>> tls_settings = 'TLS 1.2, SHA-256'
    >>> retry_policy = '3 retries with exponential backoff'
    >>> construct_nyse_api_request(api_endpoint, stock_symbols, date_range,
    data_frequency, api_key_authentication, user_agent_header, tls_settings,
    retry_policy)
    The constructed NYSE API request string.

    >>> stock_symbols = ['AAPL', 'GOOG', 'MSFT']
    >>> date_range = '2020-01-01:2020-01-31'
    >>> data_frequency = '1min'
    >>> api_key_authentication = 'your_api_key'
    >>> user_agent_header = 'Your-User-Agent'
    >>> tls_settings = 'TLS 1.2, SHA-256'
    >>> retry_policy = '3 retries with exponential backoff'
    >>> construct_nyse_api_request(api_endpoint, stock_symbols, date_range,
    data_frequency, api_key_authentication, user_agent_header, tls_settings,
    retry_policy)
    The constructed NYSE API request string.

    """
    return ConstructNyseApiRequestOutput(
        nyse_api_request_string="",
        api_endpoint="",
        user_agent_header="",
        api_key_authentication="",
        tls_settings="",
        data_centers=[],
        latency_expectation=0,
        retry_policy="",
        error_handling_mechanisms="",
    )