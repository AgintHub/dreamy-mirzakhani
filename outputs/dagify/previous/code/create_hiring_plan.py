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


class CreateHiringPlanOutput(BaseModel):
    """Pydantic model for create_hiring_plan node outputs."""
    roles_needed: List[str] = (
        Field(..., description="List of essential full-time roles needed at launch, including their one-line responsibilities.")
    )
    count_roles: int = Field(..., description="Count of roles needed.")


def create_hiring_plan(draft_operations_workflow_input: DraftOperationsWorkflowOutput, **kwargs) -> CreateHiringPlanOutput:
    """
    Determine initial staffing requirements based on drafted operations
    workflow.

    Parameters
    ----------
    tradelifecycle_steps : List[str]
        List of daily trade lifecycle steps from drafted operations
        workflow.

    Returns
    -------
    dict
        A dictionary containing 'roles_needed' and 'count_roles'.

    Raises
    ------
    ValueError
        If 'tradelifecycle_steps' is empty.

    Examples
    --------
    >>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order
    creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'])
    
    role_needed = roles_needed
    count_roles = count_roles
    print(role_needed)
    print(count_roles)

    >>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order
    creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation',
    'Market Analysis'])
    
    role_needed = roles_needed
    count_roles = count_roles
    print(role_needed)
    print(count_roles)

    """
    return CreateHiringPlanOutput(
        roles_needed=[],
        count_roles=0,
    )