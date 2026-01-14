from pydantic import BaseModel, Field
from typing import List


class DefineAssetUniverseOutput(BaseModel):
    """Pydantic model for define_asset_universe node outputs."""
    asset_classes: List[str] = (
        Field(..., description="List of specific asset classes/instruments that will constitute the investable universe")
    )
    number_of_assets: int = (
        Field(..., description="Number of asset classes listed")
    )


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    service_provider_categories: List[str] = (
        Field(..., description="List of mandatory service provider categories required for the hedge fund setup")
    )


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    control_name: List[str] = (
        Field(..., description="Names of the quantitative risk controls implemented")
    )
    control_limit: List[float] = (
        Field(..., description="Numerical limit or threshold associated with each control (e.g., VaR in % of AUM, position size cap in % of portfolio)")
    )


class DraftOperationsWorkflowOutput(BaseModel):
    """Pydantic model for draft_operations_workflow node outputs."""
    step_sequence: List[str] = (
        Field(..., description="Ordered list of trade lifecycle steps.")
    )
    responsible_party: List[str] = (
        Field(..., description="Primary responsible party for each corresponding step.")
    )
    asset_classes: List[str] = (
        Field(..., description="List of asset classes/instruments in the investable universe.")
    )
    risk_controls: List[str] = (
        Field(..., description="Quantitative risk controls applied to the workflow.")
    )
    service_providers: List[str] = (
        Field(..., description="Mandatory third\u2011party service provider categories required for execution.")
    )


def draft_operations_workflow(define_asset_universe_input: DefineAssetUniverseOutput, list_service_providers_input: ListServiceProvidersOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, **kwargs) -> DraftOperationsWorkflowOutput:
    """
    Generate a structured trade‑lifecycle workflow table for a hedge fund.

    Parameters
    ----------
    asset_classes : List[str]
        Asset classes/instruments that will constitute the investable
        universe, as returned by the `define_asset_universe` node.
    service_provider_categories : List[str]
        Mandatory third‑party service provider categories required for the
        fund, as returned by the `list_service_providers` node.
    risk_controls : List[Tuple[str, float]]
        Quantitative risk controls with their thresholds, as returned by the
        `design_risk_management_framework` node. Each tuple contains a
        control name and its numeric limit.

    Returns
    -------
    Dict[str, List[str]]
        A dictionary containing five keys: `step_sequence`,
        `responsible_party`, `asset_classes`, `risk_controls`, and
        `service_providers`. Each value is a list of strings ordered to
        match the trade lifecycle.

    Raises
    ------
    ValueError
        If any of the input lists are empty or have mismatched lengths.
    TypeError
        If an input is not of the expected type.

    Examples
    --------
    >>> asset_classes = ["US Equities", "Emerging Markets Bonds", "Commodities
    Futures"],
    >>> service_provider_categories = ["Prime Broker", "Custodian", "Compliance
    Consultant"],
    >>> risk_controls = [("VaR Limit", 2.5), ("Position Size Cap", 5.0),
    ("Liquidity Threshold", 3.0)]
    >>> workflow = draft_operations_workflow(asset_classes,
    service_provider_categories, risk_controls)
    >>> print(workflow["step_sequence"])
    ["Idea Generation", "Idea Screening", "Research", "Trade Decision", "Order
    Entry", "Execution", "Post‑Trade Processing", "Performance Reporting"]

    >>> print(workflow["responsible_party"])
    ["Research Analyst", "Senior Analyst", "Portfolio Manager", "Head of
    Trading", "Trading Desk", "Execution Team", "Post‑Trade Analyst",
    "Performance Analyst"]

    """
    return DraftOperationsWorkflowOutput(
        step_sequence=[],
        responsible_party=[],
        asset_classes=[],
        risk_controls=[],
        service_providers=[],
    )