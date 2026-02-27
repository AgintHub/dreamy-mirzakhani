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


class CreateHiringPlanOutput(BaseModel):
    """Pydantic model for create_hiring_plan node outputs."""
    roles_needed: List[str] = (
        Field(..., description="List of essential full-time roles needed at launch, including their one-line responsibilities.")
    )
    count_roles: int = Field(..., description="Count of roles needed.")


class CompilePitchDeckOutlineOutput(BaseModel):
    """Pydantic model for compile_pitch_deck_outline node outputs."""
    objectives: str = Field(..., description="Objectives slide title")
    strategy: str = Field(..., description="Strategy slide title")
    team: str = Field(..., description="Team slide title")
    edge: str = Field(..., description="Edge slide title")
    risk_controls: str = Field(..., description="Risk controls slide title")
    fees: str = Field(..., description="Fees slide title")
    target_returns: str = Field(..., description="Target returns slide title")
    market_opportunity: str = (
        Field(..., description="Market opportunity slide title")
    )
    service_providers: str = (
        Field(..., description="Service providers slide title")
    )
    timeline: str = Field(..., description="Timeline slide title")


class DevelopTimelineAndMilestonesOutput(BaseModel):
    """Pydantic model for develop_timeline_and_milestones node outputs."""
    timeline_months: List[int] = (
        Field(..., description="List of month numbers from 1 to 12 representing each month in the timeline.")
    )
    milestones: List[str] = (
        Field(..., description="Corresponding list of milestone descriptions for each month.")
    )


def develop_timeline_and_milestones(draft_operations_workflow_input: DraftOperationsWorkflowOutput, define_technology_stack_input: DefineTechnologyStackOutput, create_hiring_plan_input: CreateHiringPlanOutput, compile_pitch_deck_outline_input: CompilePitchDeckOutlineOutput, **kwargs) -> DevelopTimelineAndMilestonesOutput:
    """
    This function constructs a 12-month launch timeline with monthly milestones.

    Parameters
    ----------
    inputs : dict
        A dictionary containing 'draft_operations_workflow',
        'define_technology_stack', 'create_hiring_plan', and
        'compile_pitch_deck_outline' outputs.

    Returns
    -------
    dict
        A dictionary containing 'timeline_months' and 'milestones',
        representing a phased schedule leading to fund launch.

    Raises
    ------
    ValueError
        If inputs are missing required outputs.

    Examples
    --------
    >>> from datetime import datetime
    >>> from tabulate import tabulate
    >>> from typing import Dict, List, Union
    >>> def develop_timeline_and_milestones(inputs: Dict) -> Dict:
    ...     timeline_months =
    inputs['draft_operations_workflow']['timeline_months'] +
    inputs['define_technology_stack']['timeline_months']
    ...     milestones = [f"Legal Formation" for _ in range(3)] + [f"Regulatory
    Filings" for _ in range(2)] + [f"Service Provider Contracts" for _ in
    range(2)] + [f"Tech Deployment" for _ in range(2)] + [f"Capital Raise" for _
    in range(1)] + [f"First Trade" for _ in range(1)]
    ...     return {'timeline_months': timeline_months, 'milestones':
    milestones}
    >>> result = develop_timeline_and_milestones({'draft_operations_workflow':
    {'timeline_months': [1, 2, 3]}, 'define_technology_stack':
    {'timeline_months': [4, 5, 6]}})
    {'timeline_months': [1, 2, 3, 4, 5, 6], 'milestones': ['Legal Formation',
    'Legal Formation', 'Legal Formation', 'Regulatory Filings', 'Regulatory
    Filings', 'Service Provider Contracts', 'Service Provider Contracts', 'Tech
    Deployment', 'Tech Deployment', 'Capital Raise', 'First Trade']}

    """
    return DevelopTimelineAndMilestonesOutput(
        timeline_months=[],
        milestones=[],
    )