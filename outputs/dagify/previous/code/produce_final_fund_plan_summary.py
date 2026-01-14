from pydantic import BaseModel, Field
from typing import List


class DevelopTimelineAndMilestonesOutput(BaseModel):
    """Pydantic model for develop_timeline_and_milestones node outputs."""
    month_numbers: List[int] = (
        Field(..., description="Sequence of month numbers (1-12) for the roadmap")
    )
    milestone_names: List[str] = (
        Field(..., description="Short name of each milestone corresponding to each month")
    )
    milestone_descriptions: List[str] = (
        Field(..., description="Brief description of each milestone activity for the given month")
    )


class CompilePitchDeckOutlineOutput(BaseModel):
    """Pydantic model for compile_pitch_deck_outline node outputs."""
    slide_titles: List[str] = (
        Field(..., description="An ordered list of the 10 slide titles for the investor pitch deck.")
    )


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
    regulations: List[str] = (
        Field(..., description="List of regulatory requirements identified for the fund")
    )
    policies_controls: List[str] = (
        Field(..., description="List of corresponding internal policies or controls mapped to each regulatory requirement")
    )
    entry_count: int = (
        Field(..., description="Total number of regulatory-policy/control entries created (should be between 7 and 10)")
    )


class ProduceFinalFundPlanSummaryOutput(BaseModel):
    """Pydantic model for produce_final_fund_plan_summary node outputs."""
    strategy_bullet_points: List[str] = (
        Field(..., description="Bullet points summarizing the investment strategy")
    )
    structure_bullet_points: List[str] = (
        Field(..., description="Bullet points summarizing the legal entity and organizational structure")
    )
    risk_framework_bullet_points: List[str] = (
        Field(..., description="Bullet points outlining the risk management framework")
    )
    operational_plan_bullet_points: List[str] = (
        Field(..., description="Bullet points describing the operational workflow and staffing")
    )
    fee_model_bullet_points: List[str] = (
        Field(..., description="Bullet points detailing the management and performance fee structure")
    )
    timeline_bullet_points: List[str] = (
        Field(..., description="Bullet points presenting the 12\u2011month implementation timeline")
    )
    word_count: int = (
        Field(..., description="Total word count of the executive summary")
    )


def produce_final_fund_plan_summary(develop_timeline_and_milestones_input: DevelopTimelineAndMilestonesOutput, compile_pitch_deck_outline_input: CompilePitchDeckOutlineOutput, design_compliance_program_input: DesignComplianceProgramOutput, **kwargs) -> ProduceFinalFundPlanSummaryOutput:
    """
    Produces a consolidated launch document summarizing fund strategy,
    structure, risk framework, operational plan, fee model, and timeline.

    Parameters
    ----------
    timeline_milestones : dict
        A dictionary containing the 12-month implementation timeline
        milestones from the develop_timeline_and_milestones node.
    pitch_deck_outline : dict
        A dictionary containing the investor pitch deck outline from the
        compile_pitch_deck_outline node.
    compliance_program : dict
        A dictionary containing the regulatory compliance framework from the
        design_compliance_program node.

    Returns
    -------
    dict
        A dictionary containing the executive summary bullet points and word
        count.

    Raises
    ------
    ValueError
        If any of the input dictionaries are missing required keys or have
        incorrect data types.

    Examples
    --------
    >>> inputs = {
    ...   'timeline_milestones': ['Milestone 1', 'Milestone 2'],
    ...   'pitch_deck_outline': ['Slide 1', 'Slide 2'],
    ...   'compliance_program': ['Regulation 1', 'Regulation 2']
    >>> }
    >>> output = produce_final_fund_plan_summary(inputs)
    {'strategy_bullet_points': [...], 'structure_bullet_points': [...], ...}

    """
    return ProduceFinalFundPlanSummaryOutput(
        strategy_bullet_points=[],
        structure_bullet_points=[],
        risk_framework_bullet_points=[],
        operational_plan_bullet_points=[],
        fee_model_bullet_points=[],
        timeline_bullet_points=[],
        word_count=0,
    )