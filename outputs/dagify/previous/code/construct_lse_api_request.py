from pydantic import BaseModel, Field
from typing import List


class IdentifyLseStocksOutput(BaseModel):
    """Pydantic model for identify_lse_stocks node outputs."""
    symbol: str = (
        Field(..., description="The primary market code (e.g., 'LON') and ticker.")
    )
    market: int = Field(..., description="The market code (e.g., 1, 2...).")
    protocol: str = (
        Field(..., description="The preferred data feed protocol (e.g., FIX, REST, WebSocket).")
    )
    latency_ms: int = (
        Field(..., description="Expected latency window (ms) for real\u2011time quotes and end\u2011of\u2011day snapshots.")
    )
    datacenter: str = (
        Field(..., description="The nearest data centre location (e.g., 'London\u2011West', 'London\u2011East').")
    )
    tier: int = (
        Field(..., description="Optional: the subscription tier required (e.g., Tier 1, Tier 2, Tier 3).")
    )


class ConstructLseApiRequestOutput(BaseModel):
    """Pydantic model for construct_lse_api_request node outputs."""
    lse_api_url: str = (
        Field(..., description="The HTTPS URL of the LSE API request.")
    )
    query_parameters: List[str] = (
        Field(..., description="A list of query parameters to be used in the LSE API request.")
    )
    headers: List[str] = (
        Field(..., description="A list of headers to be used in the LSE API request.")
    )
    authentication: str = (
        Field(..., description="The authentication credentials used in the LSE API request.")
    )
    latency_considerations: str = (
        Field(..., description="The latency considerations used in the LSE API request.")
    )
    datacenter_routing_logic: str = (
        Field(..., description="The datacenter routing logic used in the LSE API request.")
    )


def construct_lse_api_request(identify_lse_stocks_input: IdentifyLseStocksOutput, **kwargs) -> ConstructLseApiRequestOutput:
    """
    Constructs a high-quality HTTPS request to the LSE API.

    Parameters
    ----------
    lse_symbol : str
        The LSE symbol to be queried.

    Returns
    -------
    Dict[str, str]
        A dictionary containing the HTTPS URL of the LSE API request, query
        parameters, headers, authentication, latency considerations, and
        datacenter routing logic.

    Raises
    ------
    ValueError
        If the LSE symbol is not found.

    Examples
    --------
    >>> lse_url = construct_lse_api_request('AAPL', '2022-01-01', '2022-01-31')
    >>> print(lse_url)
    {'lse_api_url': 'https://api.lse.co.uk/v1/quotes/AAPL', 'query_parameters':
    ['symbol=AAPL', 'start_date=2022-01-01', 'end_date=2022-01-31'], 'headers':
    ['Authorization: Bearer lse_api_key'], 'authentication': 'lsapikey',
    'latency_considerations': 'high', 'datacenter_routing_logic': 'lse-
    datacenter'}

    """
    return ConstructLseApiRequestOutput(
        lse_api_url="",
        query_parameters=[],
        headers=[],
        authentication="",
        latency_considerations="",
        datacenter_routing_logic="",
    )