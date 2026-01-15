from pydantic import BaseModel, Field


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


def identify_lse_stocks(general_input: str, **kwargs) -> IdentifyLseStocksOutput:
    """
    Return a structured catalogue of LSE equities with per-symbol data feed
    protocol, latency, and datacenter requirements.

    Returns
    -------
    List[Dict[str, Union[str, int]]]
        A list of records, each describing an LSE symbol with fields:
        symbol, market, protocol, latency_ms, datacenter, and tier.

    Raises
    ------
    ValueError
        Raised if the catalogue cannot be retrieved or a symbol entry is
        malformed.
    RuntimeError
        Raised if downstream data feeds or data centers are unavailable.

    Examples
    --------
    >>> identify_lse_stocks()
    [{"symbol": "LON-AAL", "market": 1, "protocol": "REST", "latency_ms": 120,
    "datacenter": "London-West", "tier": 1}]

    >>> identify_lse_stocks()
    [{"symbol": "LON-LLOY", "market": 1, "protocol": "FIX", "latency_ms": 65,
    "datacenter": "London-East", "tier": 2}]

    """
    return IdentifyLseStocksOutput(
        symbol="",
        market=0,
        protocol="",
        latency_ms=0,
        datacenter="",
        tier=0,
    )