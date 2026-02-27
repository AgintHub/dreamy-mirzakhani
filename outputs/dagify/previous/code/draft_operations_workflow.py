from pydantic import BaseModel, Field
from typing import List


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    asset_classes_instruments: str = (
        Field(..., description="A list of specific asset classes or instruments that the strategy will trade, with a maximum of ten entries.")
    )


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    provider_categories: str = (
        Field(..., description="List of provider categories such as prime broker, fund administrator, auditor, legal counsel, compliance consultant, and custodian.")
    )
    num_providers: int = (
        Field(..., description="Number of service providers in each listed category.")
    )


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    risk_control_1: str = (
        Field(..., description="First risk control (e.g., position limits)")
    )
    risk_control_2: str = (
        Field(..., description="Second risk control (e.g., VaR caps)")
    )
    risk_control_3: str = (
        Field(..., description="Third risk control (e.g., stop-loss levels)")
    )
    risk_control_4: str = (
        Field(..., description="Fourth risk control (e.g., liquidity thresholds)")
    )
    risk_control_5: str = (
        Field(..., description="Fifth risk control (optional)")
    )
    risk_control_6: str = (
        Field(..., description="Sixth risk control (optional)")
    )


class DraftOperationsWorkflowOutput(BaseModel):
    """Pydantic model for draft_operations_workflow node outputs."""
    tradelifecycle_steps: List[str] = (
        Field(..., description="Sequence of daily trade lifecycle steps from idea generation to reconciliation.")
    )
    responsible_parties: List[str] = (
        Field(..., description="Primary responsible parties (internal team or external providers) for each trade lifecycle step.")
    )


def draft_operations_workflow(define_asset_universe_input: DefineAssetUniverseOutput, list_service_providers_input: ListServiceProvidersOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, **kwargs) -> DraftOperationsWorkflowOutput:
    """
    Maps and outlines the end-to-end daily trading and post-trade workflow,
    specifying operational steps and responsible entities.

    Parameters
    ----------
    define_asset_universe : list of str
        Predefined list of tradable assets and instruments used to inform
        operational procedures.
    list_service_providers : list of str
        Identifies external service providers involved in trade lifecycle
        steps.
    design_risk_management_framework : list of str
        Framework outlining risk controls influencing operational workflows.

    Returns
    -------
    dict
        Dictionary with 'tradelifecycle_steps' (list of trade steps) and
        'responsible_parties' (respective responsible entities).

    Raises
    ------
    ValueError
        If required dependencies are missing or contain invalid data.

    Examples
    --------
    >>> draft_operations_workflow()
    {tradelifecycle_steps: [Idea Generation, Order Creation, Execution,
    Confirmation, Settlement, Reconciliation], responsible_parties: [Internal
    Research Team, Trading Desk, Broker Provider, Clearinghouse, Internal
    Operations, Compliance and Risk Team]}

    """
    return DraftOperationsWorkflowOutput(
        tradelifecycle_steps=[],
        responsible_parties=[],
    )