from pydantic import BaseModel, Field


class IdentifyTorontoStockExchangeStocksOutput(BaseModel):
    """Pydantic model for identify_toronto_stock_exchange_stocks node outputs."""
    ticker: str = Field(..., description="4-letter ticker symbol")
    company_name: str = Field(..., description="Full legal name of the company")
    sector_industry: str = (
        Field(..., description="Sector and industry classification (SGI/Global Industry Classification standard)")
    )
    market_cap_tier: str = (
        Field(..., description="Market capitalization tier: Large, Mid, or Small")
    )
    preferred_data_feed_protocol: str = (
        Field(..., description="Preferred data feed protocol: WebSocket, REST, or FIX")
    )
    expected_latency_ms: int = (
        Field(..., description="Expected latency in milliseconds for real-time data feed")
    )
    datacenter: str = (
        Field(..., description="Primary data center location (e.g., Toronto ON-1)")
    )


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


def construct_toronto_stock_exchange_api_request(identify_toronto_stock_exchange_stocks_input: IdentifyTorontoStockExchangeStocksOutput, **kwargs) -> ConstructTorontoStockExchangeApiRequestOutput:
    """
    Constructs a technically sophisticated API request for retrieving data from
    the Toronto Stock Exchange.

    Returns
    -------
    dict
        A dictionary containing the API request string, API endpoint, user
        agent header, API key authentication, TLS settings, latency
        expectation, and data centers

    Examples
    --------
    >>> toronto_stock_exchange_api_request =
    construct_toronto_stock_exchange_api_request('TSE')
    >>> print(toronto_stock_exchange_api_request['api_request_string'])
    >>> print(toronto_stock_exchange_api_request['api_endpoint'])
    >>> print(toronto_stock_exchange_api_request['user_agent_header'])
    >>> print(toronto_stock_exchange_api_request['api_key_authentication'])
    >>> print(toronto_stock_exchange_api_request['tls_settings'])
    >>> print(toronto_stock_exchange_api_request['latency_expectation'])
    >>> print(toronto_stock_exchange_api_request['data_centers'])
    {'api_request_string': ..., 'api_endpoint': ..., 'user_agent_header': ...,
    'api_key_authentication': ..., 'tls_settings': ..., 'latency_expectation':
    ..., 'data_centers': ...}

    """
    return ConstructTorontoStockExchangeApiRequestOutput(
        api_request_string="",
        api_endpoint="",
        user_agent_header="",
        api_key_authentication="",
        tls_settings="",
        latency_expectation=0,
        data_centers="",
    )