from pydantic import BaseModel, Field
from typing import List


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    requirement: str = (
        Field(..., description="The specific regulatory filing or registration required.")
    )
    agency_citation: str = (
        Field(..., description="The regulatory agency and citation or form number associated with the requirement.")
    )
    implementation_notes: List[str] = (
        Field(..., description="One or two brief notes describing how to implement or comply with the requirement.")
    )


class DefineInvestorProfileOutput(BaseModel):
    """Pydantic model for define_investor_profile node outputs."""
    typical_investor_types: List[str] = (
        Field(..., description="List of typical investor types (e.g., family offices, pensions)")
    )
    required_minimum_investment: int = (
        Field(..., description="Required minimum investment in USD")
    )
    liquidity_expectations: str = (
        Field(..., description="Description of liquidity expectations")
    )
    risk_tolerance_levels: List[str] = (
        Field(..., description="List of risk tolerance levels (e.g., aggressive, conservative)")
    )
    geographic_focus: str = (
        Field(..., description="Description of geographic focus")
    )


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
    accreditation_items: List[str] = (
        Field(..., description="List of investor accreditation standard items required for compliance")
    )
    accreditation_dates: List[str] = (
        Field(..., description="Implementation dates for each accreditation item (YYYY-MM-DD format)")
    )
    subscription_items: List[str] = (
        Field(..., description="List of subscription verification procedures to be followed")
    )
    subscription_dates: List[str] = (
        Field(..., description="Implementation dates for each subscription procedure (YYYY-MM-DD format)")
    )
    aml_items: List[str] = (
        Field(..., description="List of anti-money laundering policy items to implement")
    )
    aml_dates: List[str] = (
        Field(..., description="Implementation dates for each AML policy item (YYYY-MM-DD format)")
    )


def design_compliance_program(identify_regulatory_requirements_input: IdentifyRegulatoryRequirementsOutput, define_investor_profile_input: DefineInvestorProfileOutput, **kwargs) -> DesignComplianceProgramOutput:
    """
    Generate compliance checklists for investor accreditation, subscription
    verification, and AML policies, each paired with an implementation date.

    Parameters
    ----------
    regulatory_requirements : List[Dict[str, Any]]
        Output from identify_regulatory_requirements. Each dict contains
        keys 'requirement', 'agency_citation', and 'implementation_notes'.
        These provide the regulatory basis for accreditation, subscription,
        and AML items.
    investor_profile : Dict[str, Any]
        Output from define_investor_profile. Contains fields such as
        'typical_investor_types', 'required_minimum_investment',
        'liquidity_expectations', 'risk_tolerance_levels', and
        'geographic_focus'. These inform the specificity of accreditation
        and subscription items.

    Returns
    -------
    Dict[str, List[str]]
        A dictionary with six keys—accreditation_items, accreditation_dates,
        subscription_items, subscription_dates, aml_items, aml_dates—each
        mapping to a list of strings.

    Raises
    ------
    ValueError
        If either input list is empty or missing required keys.
    TypeError
        If inputs are not of the expected types.

    Examples
    --------
    >>> # Example 1: Basic compliance program generation
    >>> reg_req = [
    ...   {'requirement': 'SEC Form ADV', 'agency_citation': 'SEC',
    'implementation_notes': ['File annually', 'Update bi‑annually']},
    ...   {'requirement': 'FINRA Membership', 'agency_citation': 'FINRA',
    'implementation_notes': ['Apply within 30 days']}
    >>> ]
    >>> inv_prof = {
    ...   'typical_investor_types': ['Family Office', 'Pension Fund'],
    ...   'required_minimum_investment': 5000000,
    ...   'liquidity_expectations': 'Monthly',
    ...   'risk_tolerance_levels': ['Aggressive'],
    ...   'geographic_focus': 'US'"
                "}
    >>> result = design_compliance_program(reg_req, inv_prof)
    >>> print(result['accreditation_items'])
    ['SEC Form ADV', 'FINRA Membership']

    >>> # Example 2: Validation error when inputs missing
    >>> try:
    ...   design_compliance_program([], inv_prof)
    >>> except ValueError as e:
    ...   print(str(e))
    Input regulatory_requirements list is empty.

    """
    return DesignComplianceProgramOutput(
        accreditation_items=[],
        accreditation_dates=[],
        subscription_items=[],
        subscription_dates=[],
        aml_items=[],
        aml_dates=[],
    )