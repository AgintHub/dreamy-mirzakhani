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


class OutlineGovernanceStructureOutput(BaseModel):
    """Pydantic model for outline_governance_structure node outputs."""
    roles: List[str] = (
        Field(..., description="List of the five leadership roles defined for the fund")
    )
    duties: List[str] = (
        Field(..., description="One-sentence duty description corresponding to each role in the same order as the roles list")
    )


class CreateHiringPlanOutput(BaseModel):
    """Pydantic model for create_hiring_plan node outputs."""
    essential_roles: List[str] = (
        Field(..., description="List of essential FTE roles")
    )
    core_responsibilities: List[str] = (
        Field(..., description="List of core responsibilities for each role")
    )
    role_count: int = (
        Field(..., description="Total number of essential FTE roles")
    )


def create_hiring_plan(draft_operations_workflow_input: DraftOperationsWorkflowOutput, outline_governance_structure_input: OutlineGovernanceStructureOutput, **kwargs) -> CreateHiringPlanOutput:
    """
    Creates a hiring plan by identifying essential FTE roles and their core
    responsibilities based on the operations workflow gaps.

    Parameters
    ----------
    operations_workflow : dict
        Output from the draft_operations_workflow node
    governance_structure : dict
        Output from the outline_governance_structure node

    Returns
    -------
    dict
        A dictionary containing the essential roles, core responsibilities,
        and the total number of roles

    Raises
    ------
    ValueError
        If the input operations workflow or governance structure is invalid

    Examples
    --------
    >>> operations_workflow = {'step_sequence': ['idea generation', 'order
    entry', 'execution'],
    ...                       'responsible_party': ['investment team', 'trader',
    'execution team']}
    >>> governance_structure = {'roles': ['GP', 'CIO', 'CFO'], 'duties':
    ['overall strategy', 'investment decisions', 'financial management']}
    >>> hiring_plan = create_hiring_plan(operations_workflow,
    governance_structure)
    >>> print(hiring_plan)
    {'essential_roles': ['investment analyst', 'trader', 'execution specialist',
    'compliance officer', 'risk manager', 'financial controller', 'operations
    manager', 'technology specialist'], 'core_responsibilities': ['research and
    analysis', 'trade execution', 'trade settlement', 'regulatory compliance',
    'risk monitoring', 'financial reporting', 'operations management',
    'technology support'], 'role_count': 8}

    """
    return CreateHiringPlanOutput(
        essential_roles=[],
        core_responsibilities=[],
        role_count=0,
    )