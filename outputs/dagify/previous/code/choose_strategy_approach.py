from pydantic import BaseModel, Field
from typing import List


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


class ChooseStrategyApproachOutput(BaseModel):
    """Pydantic model for choose_strategy_approach node outputs."""
    methodology: str = (
        Field(..., description="Chosen methodology type: 'rule-based', 'machine-learning', or 'hybrid'")
    )
    justifications: List[str] = (
        Field(..., description="Short bullet points explaining why the chosen methodology is suitable for the strategy objective")
    )
    technical_reasons: List[str] = (
        Field(..., description="Specific technical reasons (e.g., data availability, model interpretability, computational cost) supporting the methodology choice")
    )


def choose_strategy_approach(define_strategy_objective_input: DefineStrategyObjectiveOutput, **kwargs) -> ChooseStrategyApproachOutput:
    """
    Selects the trading methodology (rule‑based, machine‑learning, or hybrid)
    that best fits the strategy objective.

    Parameters
    ----------
    strategy_sentence : str
        One‑sentence statement of the strategy’s objective, e.g., 'Capture
        momentum in small‑cap stocks with <3% daily volatility'.
    cagr_target : float
        Target Compound Annual Growth Rate expressed as a decimal (e.g.,
        0.15).
    annual_vol_target : float
        Maximum acceptable annual volatility expressed as a decimal (e.g.,
        0.20).
    max_drawdown : float
        Maximum drawdown limit expressed as a decimal (e.g., 0.25).
    sharpe_goal : float
        Target Sharpe ratio to be achieved.

    Returns
    -------
    dict
        Dictionary containing `methodology`, `justifications`, and
        `technical_reasons` as described in the output structure.

    Raises
    ------
    ValueError
        Raised if any required input is missing or of incorrect type.

    Examples
    --------
    >>> result = choose_strategy_approach(
    ...     strategy_sentence='Capture momentum in small-cap stocks with <3%
    daily volatility',
    ...     cagr_target=0.15,
    ...     annual_vol_target=0.20,
    ...     max_drawdown=0.25,
    ...     sharpe_goal=1.5)
    >>> print(result['methodology'])
    >>> print(result['justifications'])
    >>> print(result['technical_reasons'])
    ```
    methodology: 'rule-based'
    justifications: ['Momentum signals are well captured by trend-following
    rules.', 'Requires minimal computational overhead for high-frequency
    execution.']
    technical_reasons: ['Historical data is abundant and clean.', 'Model
    interpretability is critical for regulatory compliance.', 'Low latency
    execution is achievable with rule-based logic.']
    ```

    >>> result = choose_strategy_approach(
    ...     strategy_sentence='Generate alpha from mean-reversion patterns in
    high-volatility futures',
    ...     cagr_target=0.20,
    ...     annual_vol_target=0.35,
    ...     max_drawdown=0.30,
    ...     sharpe_goal=2.0)
    >>> print(result['methodology'])
    ```
    methodology: 'machine-learning'
    ```

    """
    return ChooseStrategyApproachOutput(
        methodology="",
        justifications=[],
        technical_reasons=[],
    )