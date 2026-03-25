from pydantic import BaseModel, Field
from typing import List


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    selected_entity_type: str = (
        Field(..., description="The selected legal vehicle structure for the fund's chosen jurisdiction.")
    )
    entity_type_rationale: str = (
        Field(..., description="A brief one-sentence explanation for the selected legal vehicle structure.")
    )


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    regulatory_requirements: List[str] = (
        Field(..., description="List of principal regulatory filings or registrations required for the selected entity and jurisdiction.")
    )
    regulatory_authorities: List[str] = (
        Field(..., description="List of governing authorities overseeing the filings and registrations.")
    )


def identify_regulatory_requirements(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> IdentifyRegulatoryRequirementsOutput:
    """
    Returns the regulatory filings and authorities required for the specified
    legal entity type and jurisdiction.

    Parameters
    ----------
    entity_type : str
        The selected legal entity type for the fund, such as LP, LLC, SICAV.
    jurisdiction : str
        The jurisdiction where the fund is established, e.g., Delaware,
        Cayman, Luxembourg.

    Returns
    -------
    Dict[str, List[str]]
        A dictionary containing two lists: regulatory requirements and
        overseeing authorities.

    Raises
    ------
    ValueError
        Raised if the entity type or jurisdiction is invalid or unsupported.

    Examples
    --------
    >>> identify_regulatory_requirements('LP', 'Delaware')
    {regulatory_requirements: [Form D Filing, State Business License],
    regulatory_authorities: [SEC, Delaware Division of Corporations]}

    >>> identify_regulatory_requirements('SICAV', 'Luxembourg')
    {regulatory_requirements: [LuxSE Authorization, COMEX Registration],
    regulatory_authorities: [Luxembourg Financial Supervisory Authority,
    Luxembourg Stock Exchange]}

    """
    return IdentifyRegulatoryRequirementsOutput(
        regulatory_requirements=[],
        regulatory_authorities=[],
    )