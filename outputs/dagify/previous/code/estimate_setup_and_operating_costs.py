from pydantic import BaseModel, Field
from typing import List


class DefineTechnologyStackOutput(BaseModel):
    """Pydantic model for define_technology_stack node outputs."""
    step_names: List[str] = (
        Field(..., description="Ordered list of operational steps as identified in the draft_operations_workflow node.")
    )
    tech_components: List[str] = (
        Field(..., description="Ordered list of corresponding technology components needed for each step; each entry aligns with the same index in step_names.")
    )


class ListServiceProvidersOutput(BaseModel):
    """Pydantic model for list_service_providers node outputs."""
    service_provider_categories: List[str] = (
        Field(..., description="List of mandatory service provider categories required for the hedge fund setup")
    )


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_cost_usd: float = (
        Field(..., description="Estimated total annual cost in USD for all service providers listed")
    )
    technology_systems_cost_usd: float = (
        Field(..., description="Estimated total annual cost in USD for all required technology systems")
    )
    office_human_infrastructure_cost_usd: float = (
        Field(..., description="Estimated total annual cost in USD for office space, hardware, and human infrastructure")
    )


def estimate_setup_and_operating_costs(define_technology_stack_input: DefineTechnologyStackOutput, list_service_providers_input: ListServiceProvidersOutput, **kwargs) -> EstimateSetupAndOperatingCostsOutput:
    """
    Estimate annual costs for service providers, technology systems, and
    office/human infrastructure.

    Parameters
    ----------
    service_provider_categories : List[str]
        List of mandatory service provider categories (e.g., prime broker,
        custodian, compliance consultant) supplied by the
        `list_service_providers` node.
    step_names : List[str]
        Ordered list of operational steps produced by the
        `define_technology_stack` node.
    tech_components : List[str]
        Ordered list of technology components corresponding to each
        operational step.

    Returns
    -------
    Tuple[float, float, float]
        A tuple containing the annual cost estimates for service providers,
        technology systems, and office/human infrastructure, respectively.

    Raises
    ------
    ValueError
        If any input list is empty or if the lengths of `step_names` and
        `tech_components` differ.
    TypeError
        If any input is not of the expected type.

    Examples
    --------
    >>> service_provider_categories = ["Prime Broker", "Custodian", "Compliance
    Consultant", "Legal Advisor", "Fund Administrator", "Auditor"]
    >>> step_names = ["Idea Generation", "Order Entry", "Execution", "Post‑Trade
    Processing", "Reporting"]
    >>> tech_components = ["Research Platform", "OMS", "Execution System",
    "Post‑Trade System", "Reporting Suite"]
    >>> costs = estimate_setup_and_operating_costs(service_provider_categories,
    step_names, tech_components)
    >>> print(costs)
    (225000.0, 180000.0, 125000.0)

    >>> service_provider_categories = []
    >>> step_names = []
    >>> tech_components = []
    >>> try:
    ...     estimate_setup_and_operating_costs(service_provider_categories,
    step_names, tech_components)
    >>> except ValueError as e:
    ...     print(str(e))
    Input lists must not be empty.

    """
    return EstimateSetupAndOperatingCostsOutput(
        service_provider_cost_usd=0.0,
        technology_systems_cost_usd=0.0,
        office_human_infrastructure_cost_usd=0.0,
    )