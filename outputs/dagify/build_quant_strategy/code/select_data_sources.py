from pydantic import BaseModel, Field
from typing import List


class SelectDataSourcesOutput(BaseModel):
    """Pydantic model for select_data_sources node outputs."""
    source_names: List[str] = (
        Field(..., description="Names of the selected market data sources")
    )
    time_ranges: List[str] = (
        Field(..., description="Time ranges for each source in ISO format (e.g., \"2020-01-01 to 2023-12-31\")")
    )
    frequencies: List[str] = (
        Field(..., description="Data frequencies for each source (e.g., \"tick\", \"1d\", \"1h\")")
    )
    source_types: List[str] = (
        Field(..., description="Classification of each source (e.g., \"tick\", \"OHLCV\", \"fundamental\")")
    )


def select_data_sources(general_input: str, **kwargs) -> SelectDataSourcesOutput:
    """
    Selects and validates high‑quality market data sources for a quantitative
    strategy.

    Parameters
    ----------
    strategy_objective : str
        A concise one‑sentence description of the strategy’s goal (e.g.,
        "Capture momentum in small‑cap stocks with <3% daily volatility").
    performance_benchmarks : dict
        Benchmark metrics dict with keys 'cagr_target', 'annual_vol_target',
        'max_drawdown', 'sharpe_goal' produced by
        set_performance_benchmarks.
    risk_limits : dict
        Risk limits dict with keys 'portfolio_volatility_limit',
        'sector_concentration_limit', 'drawdown_trigger_limit',
        'position_correlation_limit' produced by build_risk_rules.
    entry_exit_requirements : dict
        Entry/exit rule descriptors (e.g., required features such as SMA,
        ATR, volatility) produced by develop_entry_rules and
        develop_exit_rules.

    Returns
    -------
    tuple
        Four lists: source_names (List[str]), time_ranges (List[str]),
        frequencies (List[str]), source_types (List[str])

    Raises
    ------
    ValueError
        Raised if the strategy objective is empty or missing required
        fields.
    LookupError
        Raised if a requested data source is unavailable or does not satisfy
        the required frequency/time‑range constraints.

    Examples
    --------
    >>> source_names, time_ranges, frequencies, source_types =
    select_data_sources(
    ...     strategy_objective='Capture momentum in small‑cap stocks with <3%
    daily volatility',
    ...     performance_benchmarks={
    ...         'cagr_target': 0.15,
    ...         'annual_vol_target': 0.20,
    ...         'max_drawdown': 0.25,
    ...         'sharpe_goal': 1.2
    ...     },
    ...     risk_limits={
    ...         'portfolio_volatility_limit': 0.15,
    ...         'sector_concentration_limit': 0.30,
    ...         'drawdown_trigger_limit': 0.20,
    ...         'position_correlation_limit': 0.70
    ...     },
    ...     entry_exit_requirements={
    ...         'required_features': ['SMA_50', 'ATR_14', 'volatility'],
    ...         'data_type': 'OHLCV'
    ...     }
    >>> )
    [
      ['Bloomberg', 'YahooFinance', 'AlphaVantage'],
      ['2018-01-01 to 2023-12-31', '2018-01-01 to 2023-12-31', '2018-01-01 to
    2023-12-31'],
      ['tick', '1d', '1d'],
      ['tick', 'OHLCV', 'fundamental']
    ]

    >>> source_names, time_ranges, frequencies, source_types =
    select_data_sources(
    ...     strategy_objective='Mean‑reversion on FX pairs',
    ...     performance_benchmarks={},
    ...     risk_limits={},
    ...     entry_exit_requirements={}
    >>> )
    [
      ['Reuters', 'Oanda'],
      ['2015-01-01 to 2023-12-31', '2015-01-01 to 2023-12-31'],
      ['1h', 'tick'],
      ['OHLCV', 'tick']
    ]

    """
    return SelectDataSourcesOutput(
        source_names=[],
        time_ranges=[],
        frequencies=[],
        source_types=[],
    )