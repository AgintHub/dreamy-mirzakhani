from pydantic import BaseModel, Field
from typing import List


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    regulatory_requirements: List[str] = (
        Field(..., description="List of principal regulatory filings or registrations required for the selected entity and jurisdiction.")
    )
    regulatory_authorities: List[str] = (
        Field(..., description="List of governing authorities overseeing the filings and registrations.")
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


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
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


def design_compliance_program(identify_regulatory_requirements_input: IdentifyRegulatoryRequirementsOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, **kwargs) -> DesignComplianceProgramOutput:
    """
    Creates the risk control architecture by implementing core risk controls and
    systems.

    Returns
    -------
    {risk_control_1: str, risk_control_2: str, risk_control_3: str, risk_control_4: str, risk_control_5: str, risk_control_6: str}
        The implemented risk control architecture as a dictionary with keys:
        risk_control_1, risk_control_2, risk_control_3, risk_control_4,
        risk_control_5, risk_control_6, corresponding to the implemented
        risk controls.

    Raises
    ------
    RuntimeError
        If any required risk control or system is not implemented.

    Examples
    --------
    >>> risk_controls =
    design_risk_management_framework(set_performance_and_risk_targets()).values
    >>> print(risk_controls)
    {'risk_control_1': 'position limits', 'risk_control_2': 'VaR caps',
    'risk_control_3': 'stop-loss levels', 'risk_control_4': 'liquidity
    thresholds'}

    """
    return DesignComplianceProgramOutput(
        risk_control_1="",
        risk_control_2="",
        risk_control_3="",
        risk_control_4="",
        risk_control_5="",
        risk_control_6="",
    )