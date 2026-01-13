from pydantic import BaseModel, Field


class ChooseLegalEntityTypeOutput(BaseModel):
    """Pydantic model for choose_legal_entity_type node outputs."""
    legal_entity_type: str = (
        Field(..., description="The chosen legal entity type (e.g., LP, LLC, SICAV)")
    )
    rationale: str = (
        Field(..., description="One-sentence explanation of why this structure suits the strategic goals")
    )


class IdentifyRegulatoryRequirementsOutput(BaseModel):
    """Pydantic model for identify_regulatory_requirements node outputs."""
    legal_entity_type: str = (
        Field(..., description="The legal entity type selected for the fund (e.g., LP, LLC, SICAV).")
    )
    regulatory_filings: str = (
        Field(..., description="A list of 6 to 8 required regulatory filings or registrations applicable to the selected entity and jurisdiction.")
    )


def identify_regulatory_requirements(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> IdentifyRegulatoryRequirementsOutput:
    """
    Generate a list of mandatory regulatory filings for the selected legal
    entity and jurisdiction.

    Parameters
    ----------
    legal_entity_type : str
        The legal entity type chosen for the hedge fund (e.g., LP, LLC,
        SICAV).

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the legal entity type and a list of required
        regulatory filings.

    Raises
    ------
    ValueError
        Raised if the input legal_entity_type is not one of the supported
        types (LP, LLC, SICAV).
    LookupError
        Raised when the jurisdiction‑specific filing data for the given
        entity type cannot be retrieved.

    Examples
    --------
    >>> output = identify_regulatory_requirements('LLC')
    >>> print(output['legal_entity_type'])
    >>> print(output['regulatory_filings'])
    "LLC\n[\n  'SEC Form 13D',\n  'SEC Form 13G',\n  'EFIS Filing',\n  'AIFM
    Registration',\n  'FCA FCA 21',\n  'HMRC Fund Registration',\n  'EU UCITS
    Directive',\n  'FINRA 24-13'\n]"

    >>> output = identify_regulatory_requirements('SICAV')
    >>> print(output['regulatory_filings'])
    "[\n  'Luxembourg AIFMD Registration',\n  'Luxembourg Fund Law Filing',\n
    'EU UCITS Directive',\n  'FCA FCA 21',\n  'SEC Form N-1A',\n  'SEC Form
    13D',\n  'EFIS Filing',\n  'HMRC Fund Registration'\n]"

    """
    return IdentifyRegulatoryRequirementsOutput(
        legal_entity_type="",
        regulatory_filings="",
    )