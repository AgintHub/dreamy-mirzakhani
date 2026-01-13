from pydantic import BaseModel, Field
from typing import List


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


class DefineTechnologyStackOutput(BaseModel):
    """Pydantic model for define_technology_stack node outputs."""
    workflow_stages: List[str] = (
        Field(..., description = (
            "Ordered list of workflow stages (e.g., Idea Generation, Signal Generation, Order Entry, Execution Management, Position Monitoring, Reconciliation, Settlement).")
        )
    )
    technology_solutions: List[str] = (
        Field(..., description = (
            "Corresponding technology solution for each stage (e.g., Data Analytics Platform, Portfolio Management System, OMS, FIX Gateway, Risk Engine, Reconciliation Tool).")
        )
    )
    vendor_in_house_flags: List[bool] = (
        Field(..., description = (
            "Boolean flag for each stage indicating whether the solution is implemented in-house (true) or outsourced to a vendor (false).")
        )
    )


def define_technology_stack(draft_operations_workflow_input: DraftOperationsWorkflowOutput, **kwargs) -> DefineTechnologyStackOutput:
    """
    Generate a technology stack mapping for the hedge fund’s operational
    workflow.

    Parameters
    ----------
    workflow_stages : List[str]
        Ordered list of workflow stages as produced by
        `draft_operations_workflow`.
    stage_descriptions : List[str]
        Brief description of activities performed in each stage (used for
        contextual mapping).

    Returns
    -------
    Dict[str, List[Any]]
        A dictionary containing three keys: - `workflow_stages` (List[str])
        - `technology_solutions` (List[str]) - `vendor_in_house_flags`
        (List[bool])

    Raises
    ------
    ValueError
        If the length of `workflow_stages` and `stage_descriptions` do not
        match.
    KeyError
        If a known workflow stage is not present in the internal mapping.

    Examples
    --------
    >>> workflow_stages = ["Idea Generation", "Signal Generation", "Order
    Entry", "Execution Management", "Position Monitoring", "Reconciliation",
    "Settlement"],
    >>> stage_descriptions = [
    ...     "Generate investment ideas via research and data analysis.",
    ...     "Generate buy/sell signals from quantitative models.",
    ...     "Create order records in the OMS.",
    ...     "Route orders to market via FIX gateway.",
    ...     "Track open positions and P&L.",
    ...     "Automated P&L and trade reconciliation.",
    ...     "Confirm settlements with custodians and counterparties."]
    >>> result = define_technology_stack(workflow_stages, stage_descriptions)
    >>> print(result)
    {
      "workflow_stages": ["Idea Generation", "Signal Generation", "Order Entry",
    "Execution Management", "Position Monitoring", "Reconciliation",
    "Settlement"],
      "technology_solutions": ["Data Analytics Platform", "Quant Model Engine",
    "Order Management System", "FIX Gateway", "Risk Engine", "Reconciliation
    Tool", "Settlement Service"],
      "vendor_in_house_flags": [true, true, false, false, true, false, false]
    }

    >>> # Using a shortened workflow workflow_stages = ["Signal Generation",
    "Order Entry", "Execution Management"],
    >>> stage_descriptions = [
    ...     "Generate buy/sell signals.",
    ...     "Create orders.",
    ...     "Route to market."]
    >>> print(define_technology_stack(workflow_stages, stage_descriptions))
    {
      "workflow_stages": ["Signal Generation", "Order Entry", "Execution
    Management"],
      "technology_solutions": ["Quant Model Engine", "Order Management System",
    "FIX Gateway"],
      "vendor_in_house_flags": [true, false, false]
    }

    """
    return DefineTechnologyStackOutput(
        workflow_stages=[],
        technology_solutions=[],
        vendor_in_house_flags=[],
    )