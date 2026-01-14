from pydantic import BaseModel, Field
from typing import List


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    legal_entity_type: str = (
        Field(..., description="The chosen legal entity type (e.g., LP, LLC, SICAV)")
    )
    rationale: str = (
        Field(..., description="One-sentence explanation of why this structure suits the strategic goals")
    )


class OutlineGovernanceStructureOutput(BaseModel):
    """Pydantic model for outline_governance_structure node outputs."""
    roles: List[str] = (
        Field(..., description="List of the five leadership roles defined for the fund")
    )
    duties: List[str] = (
        Field(..., description="One-sentence duty description corresponding to each role in the same order as the roles list")
    )


def outline_governance_structure(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> OutlineGovernanceStructureOutput:
    """
    Generate a list of five leadership roles and a one‑sentence description of
    each duty for a hedge fund, based on the chosen legal entity type.

    Parameters
    ----------
    legal_entity_type : str
        The legal entity type selected in the choose_legal_entity_type node
        (e.g., LP, LLC, SICAV).

    Returns
    -------
    Dict[str, List[str]]
        A dictionary with two keys: 'roles', a list of role names, and
        'duties', a list of one‑sentence duty statements in the same order.

    Raises
    ------
    ValueError
        Raised if legal_entity_type is not one of the supported types (LP,
        LLC, SICAV).
    KeyError
        Raised if the internal role mapping for the provided entity type is
        missing.

    Examples
    --------
    >>> output = outline_governance_structure('LP')
    {
      "roles": ["General Partner (GP)", "Chief Investment Officer (CIO)", "Chief
    Financial Officer (CFO)", "Chief Operating Officer (COO)", "Chief Compliance
    Officer (CCO)"],
      "duties": ["Oversee overall fund strategy and execution.", "Set investment
    mandates and monitor performance.", "Manage capital structure, budgeting,
    and reporting.", "Coordinate day‑to‑day operations and technology.", "Ensure
    regulatory compliance and risk oversight."]
    }

    >>> output = outline_governance_structure('SICAV')
    {
      "roles": ["President", "Chief Investment Officer (CIO)", "Chief Financial
    Officer (CFO)", "Chief Operating Officer (COO)", "Chief Risk Officer
    (CRO)"],
      "duties": ["Represent the SICAV to regulators and investors.", "Define and
    monitor investment strategies.", "Oversee financial reporting and capital
    management.", "Lead operational efficiency and IT governance.", "Develop and
    enforce risk policies across the fund."]
    }

    """
    return OutlineGovernanceStructureOutput(
        roles=[],
        duties=[],
    )