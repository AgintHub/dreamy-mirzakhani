from pydantic import BaseModel, Field


class SetPerformanceBenchmarksOutput(BaseModel):
    """Pydantic model for set_performance_benchmarks node outputs."""
    cagr_target: float = (
        Field(..., description="Target compound annual growth rate in decimal form (e.g., 0.15 for 15%)")
    )
    annual_volatility_constraint: float = (
        Field(..., description="Maximum acceptable annual volatility in decimal form (e.g., 0.20 for 20%)")
    )
    drawdown_limit: float = (
        Field(..., description="Maximum allowable drawdown expressed as a decimal (e.g., 0.25 for 25%)")
    )
    sharpe_ratio_goal: float = (
        Field(..., description="Target Sharpe ratio to be achieved by the strategy")
    )


class BuildRiskRulesOutput(BaseModel):
    """Pydantic model for build_risk_rules node outputs."""
    portfolio_volatility_limit: float = (
        Field(..., description="The maximum allowed portfolio volatility")
    )
    sector_concentration_limit: float = (
        Field(..., description="The maximum allowed sector concentration")
    )
    drawdown_trigger_limit: float = (
        Field(..., description="The maximum allowed drawdown trigger")
    )
    position_correlation_limit: float = (
        Field(..., description="The maximum allowed position correlation")
    )
    risk_limit_rules: str = (
        Field(..., description="List of risk limit rules with their thresholds")
    )


def build_risk_rules(set_performance_benchmarks_input: SetPerformanceBenchmarksOutput, **kwargs) -> BuildRiskRulesOutput:
    """
    Builds portfolio-level risk controls based on given risk limit rules and
    thresholds.

    Parameters
    ----------
    performance_benchmarks : dict
        Performance benchmarks output from 'set_performance_benchmarks' node
    risk_limit_rules_input : dict
        Input dictionary containing risk limit rules and their thresholds

    Returns
    -------
    dict
        A dictionary containing the portfolio volatility limit, sector
        concentration limit, drawdown trigger limit, position correlation
        limit, and a list of risk limit rules with their thresholds

    Raises
    ------
    ValueError
        If the input dictionary is empty or missing required keys
    TypeError
        If the input dictionary values are not of the correct type

    Examples
    --------
    >>> performance_benchmarks = {'cagr_target': 0.15,
    'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25,
    'sharpe_ratio_goal': 1.5}
    >>> risk_limit_rules_input = {'portfolio_volatility': 0.10,
    'sector_concentration': 0.30, 'drawdown_trigger': 0.20,
    'position_correlation': 0.50}
    >>> risk_limits = build_risk_rules(performance_benchmarks,
    risk_limit_rules_input)
    {'portfolio_volatility_limit': 0.10, 'sector_concentration_limit': 0.30,
    'drawdown_trigger_limit': 0.20, 'position_correlation_limit': 0.50,
    'risk_limit_rules': ['portfolio_volatility: 0.10', 'sector_concentration:
    0.30', 'drawdown_trigger: 0.20', 'position_correlation: 0.50']}

    """
    return BuildRiskRulesOutput(
        portfolio_volatility_limit=0.0,
        sector_concentration_limit=0.0,
        drawdown_trigger_limit=0.0,
        position_correlation_limit=0.0,
        risk_limit_rules="",
    )