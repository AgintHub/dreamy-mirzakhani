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


class CalculatePositionSizingOutput(BaseModel):
    """Pydantic model for calculate_position_sizing node outputs."""
    risk_per_trade: float = Field(..., description="Risk percentage per trade")
    volatility_scaling_multiple: float = (
        Field(..., description="Volatility scaling multiple")
    )
    maximum_position_size: float = (
        Field(..., description="Maximum position size")
    )
    account_equity_reference: float = (
        Field(..., description="Account equity reference value")
    )
    position_sizing_algorithm: str = (
        Field(..., description="Position sizing algorithm description")
    )


def calculate_position_sizing(set_performance_benchmarks_input: SetPerformanceBenchmarksOutput, **kwargs) -> CalculatePositionSizingOutput:
    """
    This function calculates the position sizing parameters based on the
    provided risk per trade, volatility scaling multiple, and maximum position
    size, while considering the account equity.

    Parameters
    ----------
    cagr_target : float
        Target compound annual growth rate
    annual_volatility_constraint : float
        Maximum acceptable annual volatility
    drawdown_limit : float
        Maximum allowable drawdown
    sharpe_ratio_goal : float
        Target Sharpe ratio

    Returns
    -------
    dict
        A dictionary containing the calculated position sizing parameters:
        risk per trade, volatility scaling multiple, maximum position size,
        account equity reference, and position sizing algorithm description.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid or inconsistent.

    Examples
    --------
    >>> calculate_position_sizing(cagr_target=0.15,
    annual_volatility_constraint=0.20, drawdown_limit=0.25,
    sharpe_ratio_goal=1.5)
    {'risk_per_trade': 0.02, 'volatility_scaling_multiple': 1.5,
    'maximum_position_size': 10000.0, 'account_equity_reference': 100000.0,
    'position_sizing_algorithm': 'Risk-based position sizing'}

    """
    return CalculatePositionSizingOutput(
        risk_per_trade=0.0,
        volatility_scaling_multiple=0.0,
        maximum_position_size=0.0,
        account_equity_reference=0.0,
        position_sizing_algorithm="",
    )