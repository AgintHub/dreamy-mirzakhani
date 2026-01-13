from pydantic import BaseModel, Field
from typing import List


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    legal_entity_type: str = (
        Field(..., description="The chosen legal entity type (e.g., LP, LLC, SICAV)")
    )
    operational_advantages: List[str] = (
        Field(..., description="List of three operational advantages of the chosen legal entity type")
    )
    compliance_consideration: str = (
        Field(..., description="One compliance consideration specific to the chosen legal entity type")
    )


class OutlinerGovernanceStructureOutput(BaseModel):
    """Pydantic model for outliner_governance_structure node outputs."""
    role_names: List[str] = Field(..., description="Names of the roles")
    role_responsibility_1: List[str] = (
        Field(..., description="First responsibility for each role")
    )
    role_responsibility_2: List[str] = (
        Field(..., description="Second responsibility for each role")
    )
    role_responsibility_3: List[str] = (
        Field(..., description="Third responsibility for each role")
    )
    role_authority_scope: List[str] = (
        Field(..., description="Authority scope for each role")
    )


def outliner_governance_structure(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> OutlinerGovernanceStructureOutput:
    """
    Creates a governance framework for a hedge fund based on the selected legal
    entity type.

    Parameters
    ----------
    legal_entity_type : str
        The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).

    Returns
    -------
    dict
        Dictionary containing five lists: role_names, role_responsibility_1,
        role_responsibility_2, role_responsibility_3, and
        role_authority_scope.

    Raises
    ------
    ValueError
        If `legal_entity_type` is an empty string or not among the supported
        entity types.

    Examples
    --------
    >>> outliner_governance_structure('LP')
    {
      'role_names': ['GP', 'Investment Manager', 'Compliance Officer', 'Chief
    Operating Officer', 'Investor Relations Officer'],
      'role_responsibility_1': ['Oversee overall fund strategy', 'Develop trade
    ideas', 'Ensure regulatory compliance', 'Manage day‑to‑day operations',
    'Maintain investor communications'],
      'role_responsibility_2': ['Allocate capital', 'Approve trade execution',
    'Monitor AML/KYC', 'Coordinate vendor relationships', 'Distribute
    performance reports'],
      'role_responsibility_3': ['Set performance targets', 'Conduct risk
    reviews', 'Draft compliance policies', 'Report to board', 'Handle investor
    inquiries'],
      'role_authority_scope': ['Strategic decisions', 'Trade approval up to
    $10M', 'Compliance approvals', 'Operational budgets', 'Investor
    disclosures']
    }

    >>> outliner_governance_structure('LLC')
    {
      'role_names': ['GP', 'Investment Manager', 'Compliance Officer', 'Chief
    Financial Officer', 'Investor Relations Officer'],
      'role_responsibility_1': ['Set investment mandate', 'Identify market
    opportunities', 'Maintain regulatory filings', 'Oversee financial
    reporting', 'Engage investors'],
      'role_responsibility_2': ['Allocate capital within limits', 'Approve
    execution plans', 'Implement AML controls', 'Manage budgets', 'Provide
    performance updates'],
      'role_responsibility_3': ['Define risk appetite', 'Conduct compliance
    audits', 'Prepare annual reports', 'Ensure tax compliance', 'Coordinate
    investor meetings'],
      'role_authority_scope': ['Strategic direction', 'Trade approvals up to
    $8M', 'Compliance approvals', 'Financial oversight', 'Investor disclosure']
    }

    """
    return OutlinerGovernanceStructureOutput(
        role_names=[],
        role_responsibility_1=[],
        role_responsibility_2=[],
        role_responsibility_3=[],
        role_authority_scope=[],
    )