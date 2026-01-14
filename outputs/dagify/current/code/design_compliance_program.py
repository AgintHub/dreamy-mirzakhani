from pydantic import BaseModel, Field
from typing import List


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    legal_entity_type: str = (
        Field(..., description="The legal entity type selected for the fund (e.g., LP, LLC, SICAV).")
    )
    regulatory_filings: str = (
        Field(..., description="A list of 6 to 8 required regulatory filings or registrations applicable to the selected entity and jurisdiction.")
    )


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    control_name: List[str] = (
        Field(..., description="Names of the quantitative risk controls implemented")
    )
    control_limit: List[float] = (
        Field(..., description="Numerical limit or threshold associated with each control (e.g., VaR in % of AUM, position size cap in % of portfolio)")
    )


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
    regulations: List[str] = (
        Field(..., description="List of regulatory requirements identified for the fund")
    )
    policies_controls: List[str] = (
        Field(..., description="List of corresponding internal policies or controls mapped to each regulatory requirement")
    )
    entry_count: int = (
        Field(..., description="Total number of regulatory-policy/control entries created (should be between 7 and 10)")
    )


def design_compliance_program(identify_regulatory_requirements_input: IdentifyRegulatoryRequirementsOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, **kwargs) -> DesignComplianceProgramOutput:
    """
    Designs a compliance program by mapping regulatory requirements to internal
    policies and controls.

    Parameters
    ----------
    regulatory_requirements : List[str]
        List of regulatory requirements identified for the fund (output from
        identify_regulatory_requirements node)
    risk_controls : List[str]
        List of quantitative risk controls implemented (output from
        design_risk_management_framework node)

    Returns
    -------
    dict
        {regulations: List of regulatory requirements, policies_controls:
        List of corresponding internal policies or controls, entry_count:
        Total number of regulatory-policy/control entries}

    Raises
    ------
    ValueError
        If the number of regulatory-policy/control entries is not between 7
        and 10

    Examples
    --------
    >>> regulatory_requirements = ['SEC Form CFA', 'EFIS', 'AIFM']
    >>> risk_controls = ['VaR limits', 'position size caps']
    >>> design_compliance_program(regulatory_requirements, risk_controls)
    {'regulations': ['SEC Form CFA', 'EFIS', 'AIFM'], 'policies_controls':
    ['Internal Policy 1', 'Internal Policy 2'], 'entry_count': 7}

    """
    return DesignComplianceProgramOutput(
        regulations=[],
        policies_controls=[],
        entry_count=0,
    )