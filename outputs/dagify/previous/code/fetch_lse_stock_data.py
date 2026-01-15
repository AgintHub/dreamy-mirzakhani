from pydantic import BaseModel, Field
from typing import List


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


def fetch_lse_stock_data(construct_lse_api_request_input: ConstructLseApiRequestOutput, **kwargs) -> FetchLseStockDataOutput:
    """
    Fetches stock data from the London Stock Exchange (LSE).

    Parameters
    ----------
    lse_api_request : str
        The LSE API request.

    Returns
    -------
    tuple[str, bool, float, str]
        A tuple containing the raw JSON data, a boolean indicating whether
        any errors occurred, the average latency, and the datacenter used to
        fetch the data.

    Raises
    ------
    Exception
        If an unexpected error occurs during the data fetch operation.

    Examples
    --------
    >>> lse_api_request = construct_lse_api_request().lse_api_url
    (raw_json_data, False, latency, datacenter)

    """
    return FetchLseStockDataOutput(
        raw_data="",
        error=False,
        latency=0.0,
        datacenter="",
    )