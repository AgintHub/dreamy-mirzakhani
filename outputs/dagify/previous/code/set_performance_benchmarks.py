from pydantic import BaseModel, Field


class DefineStrategyObjectiveOutput(BaseModel):
    """Pydantic model for define_strategy_objective node outputs."""
    strategy_sentence: str = (
        Field(..., description="A concise one\u2011sentence statement of the strategy's objective")
    )
    cagr_target: float = (
        Field(..., description="Target Compound Annual Growth Rate (CAGR) expressed as a decimal")
    )
    annual_vol_target: float = (
        Field(..., description="Maximum acceptable annual volatility expressed as a decimal")
    )
    max_drawdown: float = (
        Field(..., description="Maximum drawdown limit expressed as a decimal")
    )
    sharpe_goal: float = (
        Field(..., description="Target Sharpe ratio to be achieved")
    )


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


def set_performance_benchmarks(define_strategy_objective_input: DefineStrategyObjectiveOutput, **kwargs) -> SetPerformanceBenchmarksOutput:
    """
    Parse performance benchmark parameters from user input and return a
    dictionary of numerical metrics.

    Parameters
    ----------
    input_text : str
        Raw prompt response containing numeric values for CAGR, volatility,
        drawdown, and Sharpe ratio. Example: "0.12, 0.18, 0.25, 1.5".

    Returns
    -------
    Dict[str, float]
        Dictionary with keys 'cagr_target', 'annual_volatility_constraint',
        'drawdown_limit', and 'sharpe_ratio_goal', each mapped to a float
        value.

    Raises
    ------
    ValueError
        If the input cannot be parsed into exactly four numeric values or if
        any value is out of a reasonable range (e.g., negative CAGR).
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> benchmarks = set_performance_benchmarks('0.15, 0.20, 0.25, 1.8')
    {'cagr_target': 0.15, 'annual_volatility_constraint': 0.20,
    'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}

    >>> benchmarks = set_performance_benchmarks('12%, 20%, 25%, 1.8')
    {'cagr_target': 0.12, 'annual_volatility_constraint': 0.20,
    'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}

    """
    return SetPerformanceBenchmarksOutput(
        cagr_target=0.0,
        annual_volatility_constraint=0.0,
        drawdown_limit=0.0,
        sharpe_ratio_goal=0.0,
    )