from ._draft_operations_workflow.validate_input_requirements import validate_input_requirements
from ._draft_operations_workflow.define_operational_stages import define_operational_stages
from ._draft_operations_workflow.assign_stage_responsibilities import assign_stage_responsibilities
from ._draft_operations_workflow.determine_vendor_involvement import determine_vendor_involvement
from ._draft_operations_workflow.generate_stage_descriptions import generate_stage_descriptions

from pydantic import BaseModel, Field
from typing import List


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    instrument_names: List[str] = (
        Field(..., description="Names of the 10 selected tradable instruments")
    )
    instrument_rationales: List[str] = (
        Field(..., description = (
            "Brief rationale for each of the 10 selected instruments")
        )
    )
    asset_class_count: int = (
        Field(..., description = (
            "Total number of distinct asset classes represented among the 10 instruments")
        )
    )


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_names: List[str] = (
        Field(..., description = (
            "List of mandatory external service provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.")
        )
    )
    provider_functions: List[str] = (
        Field(..., description = (
            "Core function description for each provider, matching the order of provider_names.")
        )
    )


class DraftOperationsWorkflowOutput(BaseModel):
    """Pydantic model for draft_operations_workflow node outputs."""
    stages: List[str] = (
        Field(..., description = (
            "Ordered list of operational stages from idea generation to settlement")
        )
    )
    responsible_parties: List[str] = (
        Field(..., description = (
            "Corresponding responsible party for each stage (e.g., "In-house", "Prime Broker")")
        )
    )
    vendor_involved: List[bool] = (
        Field(..., description = (
            "Boolean flag per stage indicating whether a vendor is involved (true = vendor, false = in-house)")
        )
    )
    stage_descriptions: List[str] = (
        Field(..., description = (
            "Brief description of activities performed in each stage")
        )
    )


def draft_operations_workflow(define_asset_universe_input: DefineAssetUniverseOutput, list_service_providers_input: ListServiceProvidersOutput, **kwargs) -> DraftOperationsWorkflowOutput:
    """
    Builds a step‑by‑step operational workflow for trade execution, mapping
    responsibilities and vendor involvement.

    Parameters
    ----------
    asset_universe : dict
        Output of the `define_asset_universe` node containing
        `instrument_names`, `instrument_rationales`, and
        `asset_class_count`. Used to contextualize which assets will be
        traded.
    service_providers : dict
        Output of the `list_service_providers` node containing
        `provider_names` and `provider_functions`. Provides the names of key
        third‑party vendors.

    Returns
    -------
    dict
        Dictionary with keys `stages`, `responsible_parties`,
        `vendor_involved`, and `stage_descriptions`, each holding a list of
        strings or booleans.

    Raises
    ------
    ValueError
        Raised if either input dict is missing required keys.

    Examples
    --------
    >>> # Mock inputs
    >>> asset_universe = {
    ...     'instrument_names': ['S&P 500 Futures', 'Emerging Market Debt',
    'Crude Oil Futures'],
    ...     'instrument_rationales': ['Liquidity', 'Yield potential',
    'Diversification'],
    ...     'asset_class_count': 3
    >>> }
    >>> service_providers = {
    ...     'provider_names': ['Prime Broker', 'Custodian', 'Fund
    Administrator', 'Legal Counsel', 'Compliance Consultant'],
    ...     'provider_functions': ['Order routing', 'Safekeeping', 'NAV
    calculations', 'Contract review', 'AML monitoring']
    >>> }
    >>> output = draft_operations_workflow(asset_universe, service_providers)
    >>> print(output['stages'])
    ['Idea Generation', 'Signal Generation', 'Order Entry', 'Execution
    Management', 'Position Monitoring', 'Reconciliation', 'Settlement']

    >>> print(output['vendor_involved'])
    [False, False, False, True, False, True, True]

    """
    validate_input_requirements(asset_universe=define_asset_universe_input, service_providers=list_service_providers_input)
    
    workflow_stages: List[str] = define_operational_stages(asset_context=define_asset_universe_input)
    
    responsibility_mapping: List[str] = assign_stage_responsibilities(stages=workflow_stages, providers=list_service_providers_input)
    
    vendor_flags: List[bool] = determine_vendor_involvement(responsible_parties=responsibility_mapping)
    
    stage_descriptions: List[str] = generate_stage_descriptions(stages=workflow_stages, asset_universe=define_asset_universe_input)
    
    return DraftOperationsWorkflowOutput(
        stages=workflow_stages,
        responsible_parties=responsibility_mapping,
        vendor_involved=vendor_flags,
        stage_descriptions=stage_descriptions
    )