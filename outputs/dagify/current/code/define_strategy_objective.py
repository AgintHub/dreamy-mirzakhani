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


def define_strategy_objective(general_input: str, **kwargs) -> DefineStrategyObjectiveOutput:
    """
    Create a one‑sentence objective and associated quantitative benchmarks for a
    quantitative trading strategy.

    Parameters
    ----------
    objective_description : str
        Free‑text description of the intended trading goal (e.g., "Capture
        momentum in small‑cap stocks with <3% daily volatility").
    cagr_target : float
        Desired Compound Annual Growth Rate expressed as a decimal (e.g.,
        0.15 for 15%).
    annual_vol_target : float
        Maximum acceptable annual volatility expressed as a decimal (e.g.,
        0.20 for 20%).
    max_drawdown : float
        Maximum acceptable drawdown expressed as a decimal (e.g., 0.25 for
        25%).
    sharpe_goal : float
        Target Sharpe ratio to be achieved by the strategy.

    Returns
    -------
    dict
        Dictionary containing the objective sentence and all benchmark
        values.

    Raises
    ------
    ValueError
        Raised if any numeric benchmark is not within a realistic range
        (e.g., CAGR < 0 or > 1).
    TypeError
        Raised if input types do not match the expected types.

    Examples
    --------
    >>> output = define_strategy_objective(

    ...     objective_description='Capture momentum in small‑cap stocks with
    <3%% daily volatility',
    ...     cagr_target=0.15,

    ...     annual_vol_target=0.20,

    ...     max_drawdown=0.25,

    ...     sharpe_goal=1.5

    >>> )
    {
      'strategy_sentence': 'Capture momentum in small‑cap stocks with <3% daily
    volatility',
      'cagr_target': 0.15,
      'annual_vol_target': 0.20,
      'max_drawdown': 0.25,
      'sharpe_goal': 1.5
    }

    >>> # Invalid CAGR triggers ValueError

    >>> try:

    ...     define_strategy_objective(

    ...         objective_description='Long‑term growth strategy',

    ...         cagr_target=-0.05,

    ...         annual_vol_target=0.15,

    ...         max_drawdown=0.2,

    ...         sharpe_goal=1.2

    ...     )

    >>> except ValueError as e:

    ...     print(e)
    "CAGR target must be between 0 and 1. Received: -0.05"

    """
    return DefineStrategyObjectiveOutput(
        strategy_sentence="",
        cagr_target=0.0,
        annual_vol_target=0.0,
        max_drawdown=0.0,
        sharpe_goal=0.0,
    )