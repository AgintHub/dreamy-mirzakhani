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


def identify_toronto_stock_exchange_stocks(general_input: str, **kwargs) -> IdentifyTorontoStockExchangeStocksOutput:
    """
    Return a curated list of Toronto Stock Exchange equities with ticker,
    company_name, sector_industry, market_cap_tier,
    preferred_data_feed_protocol, expected_latency_ms, and datacenter.

    Returns
    -------
    List[Dict[str, Any]]
        A list where each element is a dict with keys: ticker, company_name,
        sector_industry, market_cap_tier, preferred_data_feed_protocol,
        expected_latency_ms, datacenter.

    Raises
    ------
    ValueError
        If the resolved catalog contains missing mandatory fields or invalid
        value ranges.
    TypeError
        If the resolved catalog elements are not dictionaries with the
        expected schema.

    Examples
    --------
    >>> identify_toronto_stock_exchange_stocks()
    [{'ticker': 'BCE', 'company_name': 'BCE Inc.', 'sector_industry':
    'Communication Services - Telecom', 'market_cap_tier': 'Large',
    'preferred_data_feed_protocol': 'WebSocket', 'expected_latency_ms': 20,
    'datacenter': 'Toronto (ON-1)'}, {'ticker': 'SHOP', 'company_name': 'Shopify
    Inc.', 'sector_industry': 'Technology - Internet Retail', 'market_cap_tier':
    'Large', 'preferred_data_feed_protocol': 'REST', 'expected_latency_ms': 45,
    'datacenter': 'Toronto (ON-1)'}]

    """
    return IdentifyTorontoStockExchangeStocksOutput(
        ticker="",
        company_name="",
        sector_industry="",
        market_cap_tier="",
        preferred_data_feed_protocol="",
        expected_latency_ms=0,
        datacenter="",
    )