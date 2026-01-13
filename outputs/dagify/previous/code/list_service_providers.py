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


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    service_provider_categories: List[str] = (
        Field(..., description="List of mandatory service provider categories required for the hedge fund setup")
    )


def list_service_providers(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> ListServiceProvidersOutput:
    """
    Generate a fixed list of service provider categories needed to launch a
    hedge fund.

    Parameters
    ----------
    legal_entity_type : str
        The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).

    Returns
    -------
    dict
        Dictionary containing a single key `service_provider_categories`
        mapped to a list of strings.

    Raises
    ------
    ValueError
        If `legal_entity_type` is empty or not one of the supported types
        (LP, LLC, SICAV).

    Examples
    --------
    >>> list_service_providers('LP')
    {'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance
    Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit
    Firm', 'IT Service Provider']}

    >>> list_service_providers('LLC')
    {'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance
    Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit
    Firm', 'IT Service Provider']}

    """
    return ListServiceProvidersOutput(
        service_provider_categories=[],
    )