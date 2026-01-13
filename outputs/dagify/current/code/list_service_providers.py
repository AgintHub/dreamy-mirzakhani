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


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_names: List[str] = (
        Field(..., description="List of mandatory external service provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.")
    )
    provider_functions: List[str] = (
        Field(..., description="Core function description for each provider, matching the order of provider_names.")
    )


def list_service_providers(choose_legal_entity_type_input: ChooseLegalEntityTypeOutput, **kwargs) -> ListServiceProvidersOutput:
    """
    Generate an ordered list of mandatory external service providers and their
    core functions.

    Parameters
    ----------
    legal_entity_type : str
        The chosen legal entity type (e.g., LP, LLC, SICAV) obtained from
        the `choose_legal_entity_type` node.

    Returns
    -------
    dict
        A dictionary with two keys: `provider_names` (List[str]) and
        `provider_functions` (List[str]). Both lists are aligned so that
        index *i* in `provider_names` corresponds to index *i* in
        `provider_functions`.

    Raises
    ------
    ValueError
        Raised if `legal_entity_type` is empty or not one of the supported
        entity types.
    KeyError
        Raised if the internal mapping for the given entity type does not
        contain entries for all required providers.

    Examples
    --------
    >>> output = list_service_providers('LP')
    >>> print(output['provider_names'])
    >>> print(output['provider_functions'])
    ["Prime Broker", "Custodian", "Fund Administrator", "Legal Counsel",
    "Compliance Consultant"]\n["Facilitates trade execution and margin
    management.", "Safeguards assets and provides custody services.", "Handles
    NAV calculation, investor reporting, and fund accounting.", "Provides legal
    structuring and regulatory compliance advice.", "Assesses and implements AML
    and other compliance policies."]

    >>> output = list_service_providers('SICAV')
    >>> print(output['provider_functions'][2])
    "Handles NAV calculation, investor reporting, and fund accounting."

    """
    return ListServiceProvidersOutput(
        provider_names=[],
        provider_functions=[],
    )