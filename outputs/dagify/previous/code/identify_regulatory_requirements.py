from ._identify_regulatory_requirements.validate_legal_entity_type import validate_legal_entity_type
from ._identify_regulatory_requirements.extract_jurisdiction_from_kwargs import extract_jurisdiction_from_kwargs
from ._identify_regulatory_requirements.validate_jurisdiction import validate_jurisdiction
from ._identify_regulatory_requirements.get_regulatory_requirements_mapping import get_regulatory_requirements_mapping
from ._identify_regulatory_requirements.extract_primary_requirement import extract_primary_requirement
from ._identify_regulatory_requirements.extract_agency_citation import extract_agency_citation
from ._identify_regulatory_requirements.generate_implementation_notes import generate_implementation_notes

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
    validated_entity_type: str = validate_legal_entity_type(entity_type=choose_legal_entity_type_input.legal_entity_type)
    jurisdiction: str = extract_jurisdiction_from_kwargs(**kwargs)
    validated_jurisdiction: str = validate_jurisdiction(jurisdiction=jurisdiction)
    regulatory_mapping: dict = get_regulatory_requirements_mapping(entity_type=validated_entity_type, jurisdiction=validated_jurisdiction)
    primary_requirement: str = extract_primary_requirement(mapping=regulatory_mapping)
    agency_citation: str = extract_agency_citation(mapping=regulatory_mapping)
    implementation_notes: List[str] = generate_implementation_notes(entity_type=validated_entity_type, jurisdiction=validated_jurisdiction, requirement=primary_requirement)
    return IdentifyRegulatoryRequirementsOutput(
        requirement=primary_requirement,
        agency_citation=agency_citation,
        implementation_notes=implementation_notes,
    )