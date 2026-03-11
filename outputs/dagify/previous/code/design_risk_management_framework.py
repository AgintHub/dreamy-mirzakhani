from pydantic import BaseModel, Field


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


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    risk_control_1: str = (
        Field(..., description="First risk control (e.g., position limits)")
    )
    risk_control_2: str = (
        Field(..., description="Second risk control (e.g., VaR caps)")
    )
    risk_control_3: str = (
        Field(..., description="Third risk control (e.g., stop-loss levels)")
    )
    risk_control_4: str = (
        Field(..., description="Fourth risk control (e.g., liquidity thresholds)")
    )
    risk_control_5: str = (
        Field(..., description="Fifth risk control (optional)")
    )
    risk_control_6: str = (
        Field(..., description="Sixth risk control (optional)")
    )


def design_risk_management_framework(set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, **kwargs) -> DesignRiskManagementFrameworkOutput:
    """
    Designs a risk control architecture based on the performance and risk
    targets.

    Examples
    --------
    >>> risk_control_architecture =
    design_risk_management_framework(set_performance_and_risk_targets())
    >>> print(risk_control_architecture['risk_control_1'])
    position limits

    """
    return DesignRiskManagementFrameworkOutput(
        risk_control_1="",
        risk_control_2="",
        risk_control_3="",
        risk_control_4="",
        risk_control_5="",
        risk_control_6="",
    )