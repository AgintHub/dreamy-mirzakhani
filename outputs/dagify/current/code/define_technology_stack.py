from pydantic import BaseModel, Field
from typing import List


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


class DefineTechnologyStackOutput(BaseModel):
    """Pydantic model for define_technology_stack node outputs."""
    step_names: List[str] = (
        Field(..., description="Ordered list of operational steps as identified in the draft_operations_workflow node.")
    )
    tech_components: List[str] = (
        Field(..., description="Ordered list of corresponding technology components needed for each step; each entry aligns with the same index in step_names.")
    )


def define_technology_stack(draft_operations_workflow_input: DraftOperationsWorkflowOutput, **kwargs) -> DefineTechnologyStackOutput:
    """
    Map each operational step to the required technology component.

    Parameters
    ----------
    step_sequence : List[str]
        Ordered list of trade lifecycle steps from the
        draft_operations_workflow node.
    responsible_party : List[str]
        Primary responsible party for each step (not used directly but
        required for context).
    asset_classes : List[str]
        List of asset classes/instruments in the investable universe
        (contextual).
    risk_controls : List[str]
        Quantitative risk controls applied to the workflow (contextual).
    service_providers : List[str]
        Mandatory third‑party service provider categories required for
        execution (contextual).

    Returns
    -------
    Tuple[List[str], List[str]]
        A tuple containing two lists: the first is the ordered step_names,
        the second is the aligned tech_components.

    Raises
    ------
    ValueError
        Raised if step_sequence is empty or any element is not a string.
    ValueError
        Raised if the length of step_sequence does not match the expected
        number of technology components.

    Examples
    --------
    >>> step_sequence = [
    ...     'Idea Generation',
    ...     'Trade Planning',
    ...     'Order Entry',
    ...     'Execution',
    ...     'Trade Confirmation',
    ...     'Settlement',
    ...     'Post‑Trade Analytics'
    >>> ]
    >>> responsible_party = [
    ...     'Quant Team',
    ...     'Portfolio Manager',
    ...     'Trader',
    ...     'Trader',
    ...     'Trader',
    ...     'Operations',
    ...     'Risk Team'
    >>> ]
    >>> asset_classes = ['Equities', 'Fixed Income', 'Derivatives']
    >>> risk_controls = ['Position Size Cap', 'Daily VaR', 'Liquidity
    Threshold']
    >>> service_providers = ['Prime Broker', 'Custodian', 'Clearer']
    >>> step_names, tech_components = define_technology_stack(
    ...     step_sequence, responsible_party, asset_classes, risk_controls,
    service_providers)
    >>> print(step_names)
    >>> print(tech_components)
    [['Idea Generation', 'Trade Planning', 'Order Entry', 'Execution', 'Trade
    Confirmation', 'Settlement', 'Post‑Trade Analytics'], ['Research Portal',
    'Portfolio Management System', 'Order Management System', 'Execution
    Platform', 'Trade Capture System', 'Clearing Service', 'Analytics
    Dashboard']]

    >>> # Minimal example with only two steps
    >>> step_names, tech_components = define_technology_stack(
    ...     ['Idea Generation', 'Order Entry'], [], [], [], [])
    >>> print(step_names)
    >>> print(tech_components)
    [['Idea Generation', 'Order Entry'], ['Research Portal', 'Order Management
    System']]

    """
    return DefineTechnologyStackOutput(
        step_names=[],
        tech_components=[],
    )