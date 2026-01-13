from pydantic import BaseModel, Field
from typing import List


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    jurisdiction_name: str = (
        Field(..., description="The chosen fund domicile name")
    )
    rationale: str = (
        Field(..., description="One sentence explanation for selecting this jurisdiction")
    )
    pros: List[str] = (
        Field(..., description="Two key advantages of the chosen jurisdiction")
    )
    cons: List[str] = (
        Field(..., description="Two key disadvantages or challenges of the chosen jurisdiction")
    )


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    legal_entity_type: str = (
        Field(..., description="The chosen legal entity type (e.g., LP, LLC, SICAV)")
    )
    rationale: str = (
        Field(..., description="One-sentence explanation of why this structure suits the strategic goals")
    )


def choose_legal_entity_type(select_jurisdiction_input: SelectJurisdictionOutput, **kwargs) -> ChooseLegalEntityTypeOutput:
    """
    Executes the selection of a legal entity type based on the chosen
    jurisdiction and provides a rationale for the choice.

    Parameters
    ----------
    jurisdiction_name : str
        The name of the jurisdiction selected in the previous node.
    rationale_for_jurisdiction : str
        The rationale provided for choosing the jurisdiction.

    Returns
    -------
    dict
        A dictionary containing the chosen legal entity type and the
        rationale for the selection.

    Raises
    ------
    ValueError
        If the jurisdiction name or rationale is empty.

    Examples
    --------
    >>> choose_legal_entity_type(jurisdiction_name='Cayman Islands',
    rationale_for_jurisdiction='Tax efficiency and minimal regulatory
    oversight.')
    {'legal_entity_type': 'LP', 'rationale': 'LP structure is suitable for the
    Cayman Islands due to its flexibility and tax benefits.'}

    """
    return ChooseLegalEntityTypeOutput(
        legal_entity_type="",
        rationale="",
    )