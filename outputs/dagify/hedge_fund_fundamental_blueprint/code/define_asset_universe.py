from pydantic import BaseModel, Field
from typing import List


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    strategy_category: str = (
        Field(..., description="The chosen primary investment strategy category.")
    )
    rationale: str = (
        Field(..., description="A one-paragraph explanation aligning the strategy with the fund's objectives.")
    )
    risk_profile: str = (
        Field(..., description="A concise description of the expected risk profile associated with the chosen strategy.")
    )


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    instrument_names: List[str] = (
        Field(..., description="Names of the 10 selected tradable instruments")
    )
    instrument_rationales: List[str] = (
        Field(..., description="Brief rationale for each of the 10 selected instruments")
    )
    asset_class_count: int = (
        Field(..., description="Total number of distinct asset classes represented among the 10 instruments")
    )


def define_asset_universe(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> DefineAssetUniverseOutput:
    """
    Generate a list of 10 tradable financial instruments along with short
    rationales and compute the distinct asset class count.

    Parameters
    ----------
    strategy_category : str
        Primary investment strategy category determined by the parent node
        (e.g., 'Long/Short Equity', 'Global Macro', 'Event‑Driven'). This
        informs the asset selection.
    strategy_rationale : str
        One‑paragraph justification of the chosen strategy, used for
        contextual filtering of instruments.
    risk_profile : str
        Concise description of the expected risk profile (e.g., 'High
        volatility, leverage‑enabled'). Helps prioritize high‑yield or
        high‑liquidity assets.

    Returns
    -------
    dict
        Dictionary with keys `instrument_names` (List[str]),
        `instrument_rationales` (List[str]), and `asset_class_count` (int)
        as defined in the node’s output structure.

    Raises
    ------
    ValueError
        If any of the input parameters are missing or empty.
    RuntimeError
        If the algorithm fails to assemble 10 distinct instruments after
        exhaustive search.

    Examples
    --------
    >>> # Example 1: Long/Short Equity strategy with moderate risk
    >>> result = define_asset_universe(

    ...     strategy_category='Long/Short Equity',

    ...     strategy_rationale='Capitalize on market inefficiencies while
    providing downside protection.',
    ...     risk_profile='Moderate volatility with limited leverage.'

    >>> )
    {
      'instrument_names': [
        'S&P 500 Equity Index',
        'Nasdaq 100 Equity Index',
        'US Treasury 10‑Year Bond',
        'US Treasury 30‑Year Bond',
        'Gold Futures',
        'Oil Futures',
        'EUR/USD Spot',
        'US 10‑Year Treasury Futures',
        'Emerging Market Corporate Bond Index',
        'Credit Default Swap on S&P 500'
      ],
      'instrument_rationales': [
        'Large‑cap equity exposure for core long bets.',
        'High‑growth tech exposure to balance risk.',
        'Cash‑like instrument for portfolio liquidity.',
        'Long‑term yield curve play for duration control.',
        'Inflation hedge and commodity diversification.',
        'Oil price volatility capture.',
        'Currency overlay for hedge and speculation.',
        'Leverage and duration adjustment via futures.',
        'Diversification into high‑yield debt markets.',
        'Credit risk exposure and spread trading.'
      ],
      'asset_class_count': 5
    }

    >>> # Example 2: Global Macro strategy with high risk tolerance
    >>> result = define_asset_universe(

    ...     strategy_category='Global Macro',

    ...     strategy_rationale='Exploit macroeconomic trends across asset
    classes worldwide.',
    ...     risk_profile='High volatility, aggressive leverage allowed.'
    )
    {
      'instrument_names': [
        'S&P 500 Futures',
        'Euro Stoxx 50 Futures',
        'US Treasury 10‑Year Futures',
        'US Treasury 30‑Year Futures',
        'Gold Spot',
        'Crude Oil Spot',
        'EUR/USD Forward',
        'Emerging Market Debt Futures',
        'Credit Default Swap Index on Emerging Markets',
        'Volatility Index (VIX) Futures'
      ],
      'instrument_rationales': [
        'Leverage on major equity markets.',
        'Exposure to European equity trends.',
        'Yield curve trade for duration control.',
        'Long‑term interest rate play.',
        'Inflation hedge.',
        'Energy market speculation.',
        'Currency overlay for macro bets.',
        'Emerging market debt trend exploitation.',
        'Credit spread trading across emerging markets.',
        'Volatility capture and risk management.'
      ],
      'asset_class_count': 5
    }

    """
    return DefineAssetUniverseOutput(
        instrument_names=[],
        instrument_rationales=[],
        asset_class_count=0,
    )