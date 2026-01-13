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


def identify_regulatory_requirements(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> IdentifyRegulatoryRequirementsOutput:
    """
    Generate a list of all regulatory filings, registrations, and associated
    implementation notes required for the hedge fund’s chosen legal entity and
    jurisdiction.

    Parameters
    ----------
    legal_entity_info : dict
        Dictionary containing the legal entity type and jurisdiction as
        returned by the parent node `choose_legal_entity_type`.

    Returns
    -------
    List[dict]
        A list of dictionaries, each containing a `requirement`,
        `agency_citation`, and `implementation_notes` field.

    Raises
    ------
    KeyError
        If `legal_entity_info` does not contain expected keys such as
        `legal_entity_type` or `jurisdiction`.
    ValueError
        If the legal entity type or jurisdiction is unsupported or unknown.

    Examples
    --------
    >>> legal_entity_info = {
    ...     'legal_entity_type': 'LLC',
    ...     'jurisdiction': 'Delaware'
    >>> }
    [
      {
        "requirement": "Register with SEC as an investment adviser",
        "agency_citation": "SEC, Form ADV",
        "implementation_notes": [
          "File Form ADV Part 2A and 2B with the SEC",
          "Maintain annual updates and filing deadlines"

    """
    return IdentifyRegulatoryRequirementsOutput(
        requirement="",
        agency_citation="",
        implementation_notes=[],
    )