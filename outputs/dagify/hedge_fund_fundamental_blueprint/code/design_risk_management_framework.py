from pydantic import BaseModel, Field
from typing import List


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    metric_names: List[str] = (
        Field(..., description="Names of the performance and risk metrics (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).")
    )
    target_values: List[float] = (
        Field(..., description="Numerical target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).")
    )
    rationale_texts: List[str] = (
        Field(..., description="Brief rationale for each target, explaining how it aligns with strategy and risk appetite.")
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


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    num_quant_controls: int = (
        Field(..., description="Number of quantifiable risk controls specified")
    )
    quant_controls_desc: List[str] = (
        Field(..., description="Descriptions of each quantifiable risk control")
    )
    num_qual_practices: int = (
        Field(..., description="Number of qualitative risk practices specified")
    )
    qual_practices_desc: List[str] = (
        Field(..., description="Descriptions of each qualitative risk practice")
    )


def design_risk_management_framework(set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, define_asset_universe_input: DefineAssetUniverseOutput, **kwargs) -> DesignRiskManagementFrameworkOutput:
    """
    Generate a risk mitigation framework that aligns with performance targets
    and the chosen asset universe.

    Parameters
    ----------
    metric_names : List[str]
        Names of performance and risk metrics from
        set_performance_and_risk_targets.
    target_values : List[float]
        Numeric target values corresponding to each metric.
    rationale_texts : List[str]
        Brief rationale for each target.
    instrument_names : List[str]
        List of the 10 selected tradable instruments from
        define_asset_universe.
    instrument_rationales : List[str]
        Rationales for each instrument.
    asset_class_count : int
        Number of distinct asset classes represented among the 10
        instruments.

    Returns
    -------
    dict
        Dictionary matching the node's output structure:
        {num_quant_controls, quant_controls_desc, num_qual_practices,
        qual_practices_desc}.

    Raises
    ------
    ValueError
        If any required input list is empty or misaligned in length.
    TypeError
        If input types do not match the expected PrimitiveTypes.

    Examples
    --------
    >>> design_risk_management_framework(

    ...     metric_names=['Gross Return', 'Volatility', 'Sharpe Ratio', 'Max
    Drawdown'],
    ...     target_values=[0.15, 0.10, 2.0, 0.20],

    ...     rationale_texts=['Targeting 15% return', 'Control volatility to
    10%', 'Sharpe > 2', 'Drawdown < 20%'],
    ...     instrument_names=['SPX Futures', 'Emerging Debt', 'Gold Futures',
    'USD Bonds', 'EU Equity ETF', 'Oil Futures', 'US Treasury', 'China Shares',
    'Eurodollar Futures', 'US Equity ETF'],
    ...     instrument_rationales=['Liquidity', 'Diversification', 'Inflation
    hedge', 'Safe haven', 'European exposure', 'Energy cycle', 'Credit quality',
    'Growth potential', 'Interest rate sensitivity', 'Broad market exposure'],
    ...     asset_class_count=4

    >>> )
    {
      "num_quant_controls": 5,
      "quant_controls_desc": [
        "Position limit: max 10% of portfolio per instrument",
        "Daily VaR: 2% of NAV at 99% confidence",
        "Liquidity threshold: min 20% of position must be marketable within 2
    hours",
        "Concentration limit: no single asset class > 25% of total NAV",
        "Leverage cap: maximum 3x equity exposure"
      ],
      "num_qual_practices": 3,
      "qual_practices_desc": [
        "Daily risk dashboard emailed to Portfolio Manager and Head of Risk",
        "Weekly risk review meeting with investment team and compliance",
        "Monthly audit of risk controls against performance targets"
      ]
    }

    >>> design_risk_management_framework(

    ...     metric_names=['Gross Return', 'Volatility'],

    ...     target_values=[0.12, 0.08],

    ...     rationale_texts=['12% return', '8% vol'],

    ...     instrument_names=['AAPL', 'SPX Futures', 'US Treasury', 'Gold'],

    ...     instrument_rationales=['Growth', 'Index', 'Safe haven', 'Inflation
    hedge'],
    ...     asset_class_count=3

    >>> )
    {
      "num_quant_controls": 4,
      "quant_controls_desc": [
        "Max position per security: 5% of NAV",
        "Daily VaR: 1.5% of NAV",
        "Liquidity: 15% of position must be liquid within 1 hour",
        "Leverage: capped at 2x equity"
      ],
      "num_qual_practices": 3,
      "qual_practices_desc": [
        "Daily risk metric report",
        "Bi‑weekly risk review",
        "Quarterly independent risk audit"
      ]
    }

    """
    return DesignRiskManagementFrameworkOutput(
        num_quant_controls=0,
        quant_controls_desc=[],
        num_qual_practices=0,
        qual_practices_desc=[],
    )