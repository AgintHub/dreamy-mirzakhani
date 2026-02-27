from pydantic import BaseModel, Field
from typing import List


class DraftOperationsWorkflowOutput(BaseModel):
    """Pydantic model for draft_operations_workflow node outputs."""
    tradelifecycle_steps: List[str] = (
        Field(..., description="Sequence of daily trade lifecycle steps from idea generation to reconciliation.")
    )
    responsible_parties: List[str] = (
        Field(..., description="Primary responsible parties (internal team or external providers) for each trade lifecycle step.")
    )


class DefineTechnologyStackOutput(BaseModel):
    """Pydantic model for define_technology_stack node outputs."""
    ops_steps: List[str] = Field(..., description="List of operation steps")
    tech_components: List[str] = (
        Field(..., description="List of technology components")
    )
    tech_stack: str = Field(..., description="The final technology stack")


def define_technology_stack(draft_operations_workflow_input: DraftOperationsWorkflowOutput, **kwargs) -> DefineTechnologyStackOutput:
    """
    This node takes a workflow with operation steps and specifies the technology
    components required for each step to create the final technology stack.

    Parameters
    ----------
    workflow : List[str]
        List of operation steps in the workflow

    Returns
    -------
    Tuple[List[str], List[str], str]
        A tuple containing the list of operation steps, list of technology
        components, and the final technology stack

    Examples
    --------
    >>> ops_steps = ['Step 1', 'Step 2', 'Step 3']
    >>> tech_components = []
    >>> def define_technology_stack(workflow):
    ...     for op in workflow:
    ...         tech_components.append('Component 1')
    ...     return ops_steps, tech_components, ','.join(tech_components)
    (['Step 1', 'Step 2', 'Step 3'], ['Component 1', 'Component 1', 'Component
    1'], 'Component 1,Component 1,Component 1')

    >>> ops_steps = ['Step 4', 'Step 5', 'Step 6']
    >>> tech_components = []
    >>> def define_technology_stack(workflow):
    ...     for op in workflow:
    ...         tech_components.append('Component 2')
    ...     return ops_steps, tech_components, ','.join(tech_components)
    (['Step 4', 'Step 5', 'Step 6'], ['Component 2', 'Component 2', 'Component
    2'], 'Component 2,Component 2,Component 2')

    """
    return DefineTechnologyStackOutput(
        ops_steps=[],
        tech_components=[],
        tech_stack="",
    )