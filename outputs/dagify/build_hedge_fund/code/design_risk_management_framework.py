from pydantic import BaseModel, Field
from typing import List


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


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    control_name: List[str] = (
        Field(..., description="Names of the quantitative risk controls implemented")
    )
    control_limit: List[float] = (
        Field(..., description="Numerical limit or threshold associated with each control (e.g., VaR in % of AUM, position size cap in % of portfolio)")
    )


def design_risk_management_framework(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, **kwargs) -> DesignRiskManagementFrameworkOutput:
    """
    Generate a list of quantitative risk controls and their numeric limits based
    on the chosen investment strategy and performance targets.

    Parameters
    ----------
    chosen_strategy : str
        The hedge fund strategy selected in the `choose_investment_strategy`
        node (e.g., "long/short equity", "market neutral", etc.).
    annual_gross_return_target : float
        Target annual gross return expressed as a decimal (e.g., 0.12 for
        12%).
    volatility_limit_pct : float
        Maximum acceptable annual volatility expressed as a percentage
        (e.g., 15 for 15%).
    sharpe_ratio_goal : float
        Desired Sharpe ratio target for the fund.
    max_drawdown_pct : float
        Maximum acceptable peak‑to‑trough drawdown expressed as a percentage
        (e.g., 20 for 20%).

    Returns
    -------
    Tuple[List[str], List[float]]
        Two lists: control_name and control_limit, each element
        corresponding by index.

    Raises
    ------
    ValueError
        If any numeric target is negative or out of a realistic range (e.g.,
        VaR > 100%).
    KeyError
        If a required input key is missing from the arguments.

    Examples
    --------
    >>> control_name, control_limit = design_risk_management_framework(
    ...     chosen_strategy="long/short equity",
    ...     annual_gross_return_target=0.15,
    ...     volatility_limit_pct=12.0,
    ...     sharpe_ratio_goal=1.5,
    ...     max_drawdown_pct=18.0)
    >>> ]
    "control_name": ["VaR limit", "Position size cap", "Liquidity threshold",
    "Stop‑loss level"],\n"control_limit": [2.5, 10.0, 5.0, 3.0]

    >>> control_name, control_limit = design_risk_management_framework(
    ...     chosen_strategy="market neutral",
    ...     annual_gross_return_target=0.10,
    ...     volatility_limit_pct=8.0,
    ...     sharpe_ratio_goal=1.2,
    ...     max_drawdown_pct=12.0)
    >>> ]
    "control_name": ["VaR limit", "Position size cap", "Liquidity
    threshold"],\n"control_limit": [1.8, 8.0, 4.0]

    """
    return DesignRiskManagementFrameworkOutput(
        control_name=[],
        control_limit=[],
    )