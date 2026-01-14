from ._identify_regulatory_requirements.extract_jurisdiction_from_kwargs import extract_jurisdiction_from_kwargs
from ._identify_regulatory_requirements.validate_legal_entity_and_jurisdiction import validate_legal_entity_and_jurisdiction
from ._identify_regulatory_requirements.fetch_regulatory_requirements import fetch_regulatory_requirements
from ._identify_regulatory_requirements.select_primary_requirement import select_primary_requirement
from ._identify_regulatory_requirements.format_implementation_notes import format_implementation_notes

from pydantic import BaseModel, Field
from typing import List


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


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    requirement: str = (
        Field(..., description = (
            "The specific regulatory filing or registration required.")
        )
    )
    agency_citation: str = (
        Field(..., description = (
            "The regulatory agency and citation or form number associated with the requirement.")
        )
    )
    implementation_notes: List[str] = (
        Field(..., description = (
            "One or two brief notes describing how to implement or comply with the requirement.")
        )
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
    legal_entity_type: str = choose_legal_entity_type_input.legal_entity_type
    jurisdiction: str = extract_jurisdiction_from_kwargs(**kwargs)
    
    validated_entity_info: dict = validate_legal_entity_and_jurisdiction(
        entity_type=legal_entity_type, 
        jurisdiction=jurisdiction
    )
    
    regulatory_requirements_list: List[dict] = fetch_regulatory_requirements(
        entity_type=validated_entity_info["legal_entity_type"],
        jurisdiction=validated_entity_info["jurisdiction"]
    )
    
    primary_requirement: dict = select_primary_requirement(
        requirements_list=regulatory_requirements_list
    )
    
    formatted_notes: List[str] = format_implementation_notes(
        raw_notes=primary_requirement.get("implementation_notes", [])
    )
    
    return IdentifyRegulatoryRequirementsOutput(
        requirement=primary_requirement["requirement"],
        agency_citation=primary_requirement["agency_citation"],
        implementation_notes=formatted_notes
    )