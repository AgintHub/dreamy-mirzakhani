from pydantic import BaseModel, Field


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_investment_strategy: str = (
        Field(..., description="The chosen high-level investment strategy")
    )
    justification: str = (
        Field(..., description="A one-sentence justification for the chosen investment strategy")
    )


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    annual_gross_return: float = (
        Field(..., description="Target annual gross return for the chosen strategy")
    )
    annual_volatility: float = (
        Field(..., description="Target annual volatility for the chosen strategy")
    )
    Sharpe_ratio: float = (
        Field(..., description="Target Sharpe ratio for the chosen strategy")
    )
    maximum_drawdown: float = (
        Field(..., description="Target maximum drawdown for the strategy")
    )
    performance_targets: float = (
        Field(..., description="A list of key performance metric targets for the strategy")
    )
    risk_targets: float = (
        Field(..., description="A list of risk metric targets for the strategy")
    )


def set_performance_and_risk_targets(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> SetPerformanceAndRiskTargetsOutput:
    """
    Defines numerical performance and risk targets for the hedge fund strategy,
    outputting key metrics such as expected return, volatility, Sharpe ratio,
    and max drawdown.

    Parameters
    ----------
    annual_gross_return : float
        The targeted annual gross return for the strategy, expressed as a
        percentage.
    annual_volatility : float
        The targeted annual volatility (standard deviation) of returns,
        expressed as a percentage.
    Sharpe_ratio : float
        The desired Sharpe ratio, representing risk-adjusted return.
    maximum_drawdown : float
        The maximum allowable peak-to-trough loss during the investment
        period, expressed as a percentage.

    Returns
    -------
    dict
        A dictionary containing all defined performance and risk metrics,
        including targets.

    Raises
    ------
    ValueError
        If any of the inputs are out of realistic range or improperly
        specified.

    Examples
    --------
    >>> set_performance_and_risk_targets(
    ...     annual_gross_return=15.0,
    ...     annual_volatility=10.0,
    ...     Sharpe_ratio=1.5,
    ...     maximum_drawdown=20.0
    >>> )
    {'annual_gross_return': 15.0, 'annual_volatility': 10.0, 'Sharpe_ratio':
    1.5, 'maximum_drawdown': 20.0, 'performance_targets': [15.0],
    'risk_targets': [10.0, 1.5, 20.0]}

    >>> set_performance_and_risk_targets(
    ...     annual_gross_return=8.0,
    ...     annual_volatility=12.0,
    ...     Sharpe_ratio=0.8,
    ...     maximum_drawdown=30.0
    >>> )
    {'annual_gross_return': 8.0, 'annual_volatility': 12.0, 'Sharpe_ratio': 0.8,
    'maximum_drawdown': 30.0, 'performance_targets': [8.0], 'risk_targets':
    [12.0, 0.8, 30.0]}

    """
    return SetPerformanceAndRiskTargetsOutput(
        annual_gross_return=0.0,
        annual_volatility=0.0,
        Sharpe_ratio=0.0,
        maximum_drawdown=0.0,
        performance_targets=0.0,
        risk_targets=0.0,
    )