from pydantic import BaseModel, Field
from typing import List


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    chosen_jurisdiction: str = (
        Field(..., description="The name of the selected fund domicile")
    )
    advantages: List[str] = (
        Field(..., description = (
            "A list of two key advantages of the chosen jurisdiction")
        )
    )
    disadvantages: List[str] = (
        Field(..., description = (
            "A list of two key disadvantages of the chosen jurisdiction")
        )
    )
    justification: str = (
        Field(..., description = (
            "Brief explanation linking the jurisdiction to the fund\u2019s objectives and strategy")
        )
    )


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    legal_entity_type: str = (
        Field(..., description = (
            "The chosen legal entity type (e.g., LP, LLC, SICAV)")
        )
    )
    operational_advantages: List[str] = (
        Field(..., description = (
            "List of three operational advantages of the chosen legal entity type")
        )
    )
    compliance_consideration: str = (
        Field(..., description = (
            "One compliance consideration specific to the chosen legal entity type")
        )
    )


def choose_legal_entity_type(select_jurisdiction_input: SelectJurisdictionOutput, **kwargs) -> ChooseLegalEntityTypeOutput:
    """
    Choose a legal entity type based on the selected jurisdiction and provide
    operational advantages and compliance considerations.

    Parameters
    ----------
    jurisdiction : str
        The selected jurisdiction (e.g., Cayman Islands, Delaware,
        Luxembourg)

    Returns
    -------
    dict
        A dictionary containing the chosen legal entity type, operational
        advantages, and compliance consideration.

    Raises
    ------
    ValueError
        If the selected jurisdiction is not supported.

    Examples
    --------
    >>> choose_legal_entity_type('Cayman Islands')
    >>> # Output: {'legal_entity_type': 'LP', 'operational_advantages': ['Tax
    efficiency', 'Flexibility in ownership structure', 'Limited liability
    protection'], 'compliance_consideration': 'Registration with the Cayman
    Islands Monetary Authority'}
    {'legal_entity_type': 'LP', 'operational_advantages': ['Tax efficiency',
    'Flexibility in ownership structure', 'Limited liability protection'],
    'compliance_consideration': 'Registration with the Cayman Islands Monetary
    Authority'}

    """
    return ChooseLegalEntityTypeOutput(
        legal_entity_type="",
        operational_advantages=[],
        compliance_consideration="",
    )