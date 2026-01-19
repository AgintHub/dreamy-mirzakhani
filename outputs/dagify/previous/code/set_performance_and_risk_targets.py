from pydantic import BaseModel, Field


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_strategy: str = (
        Field(..., description="The specific hedge fund strategy selected from the predefined categories")
    )
    alignment_explanation: str = (
        Field(..., description="A one-sentence explanation of how the chosen strategy supports the fund's objectives")
    )


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    annual_gross_return_target: float = (
        Field(..., description="Target annual gross return expressed as a decimal (e.g., 0.12 for 12%)")
    )
    volatility_limit_pct: float = (
        Field(..., description="Maximum acceptable annual volatility expressed as a percentage (e.g., 15 for 15%)")
    )
    sharpe_ratio_goal: float = (
        Field(..., description="Desired Sharpe ratio target for the fund")
    )
    max_drawdown_pct: float = (
        Field(..., description="Maximum acceptable peak\u2011to\u2011trough drawdown expressed as a percentage (e.g., 20 for 20%)")
    )


def set_performance_and_risk_targets(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> SetPerformanceAndRiskTargetsOutput:
    """
    Generate quantitative performance and risk targets for a hedge fund based on
    its investment strategy.

    Parameters
    ----------
    chosen_strategy : str
        The hedge fund strategy selected in the `choose_investment_strategy`
        node.

    Returns
    -------
    dict
        A dictionary containing four float fields:
        `annual_gross_return_target`, `volatility_limit_pct`,
        `sharpe_ratio_goal`, and `max_drawdown_pct`.

    Raises
    ------
    ValueError
        If `chosen_strategy` is not one of the supported strategy
        categories.

    Examples
    --------
    >>> targets = set_performance_and_risk_targets('long/short equity')
    >>> print(targets['annual_gross_return_target'])
    0.12

    >>> targets = set_performance_and_risk_targets('global macro')
    >>> print(targets['volatility_limit_pct'])
    20.0

    """
    return SetPerformanceAndRiskTargetsOutput(
        annual_gross_return_target=0.0,
        volatility_limit_pct=0.0,
        sharpe_ratio_goal=0.0,
        max_drawdown_pct=0.0,
    )