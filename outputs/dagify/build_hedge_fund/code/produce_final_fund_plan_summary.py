from pydantic import BaseModel, Field
from typing import List


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
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


class ProduceFinalFundPlanSummaryOutput(BaseModel):
    """Pydantic model for produce_final_fund_plan_summary node outputs."""
    final_plan_document: str = (
        Field(..., description="The comprehensive final plan document.")
    )
    executive_summary_bullet_points: str = (
        Field(..., description="A list of bullet points summarizing key points in the final plan.")
    )
    fund_structure_details: str = (
        Field(..., description="A section detailing the fund's structural attributes.")
    )
    risk_management_controls: str = (
        Field(..., description="A section outlining the fund's risk management controls.")
    )
    operational_steps: str = (
        Field(..., description="A detailed section describing operational steps and processes.")
    )
    fee_schedule: str = (
        Field(..., description="A section detailing the fee structure of the fund.")
    )
    cost_model: str = (
        Field(..., description="A section describing the fund's cost model.")
    )
    compliance_framework: str = (
        Field(..., description="A section presenting the compliance framework.")
    )
    hiring_plan: str = (
        Field(..., description="A section outlining the hiring plan.")
    )
    technology_stack: str = (
        Field(..., description="A section detailing the technology stack supporting operations.")
    )
    launch_timeline: str = (
        Field(..., description="A timeline section describing key launch milestones.")
    )
    fundraising_materials: str = (
        Field(..., description="A section detailing fundraising materials for investor outreach.")
    )


def produce_final_fund_plan_summary(design_compliance_program_input: DesignComplianceProgramOutput, compile_pitch_deck_outline_input: CompilePitchDeckOutlineOutput, develop_timeline_and_milestones_input: DevelopTimelineAndMilestonesOutput, **kwargs) -> ProduceFinalFundPlanSummaryOutput:
    """
    Synthesizes prior generated components into a detailed final plan document,
    including sections on strategy, structure, risk controls, operations, fees,
    cost model, compliance, staffing, technology, timeline, and fundraising
    materials.

    Parameters
    ----------
    design_compliance_program_output : dict
        Output dictionary from the design_compliance_program node containing
        compliance details.
    compile_pitch_deck_outline_output : dict
        Output dictionary from the compile_pitch_deck_outline node with
        presentation structure.
    develop_timeline_and_milestones_output : dict
        Output dictionary from the develop_timeline_and_milestones node with
        timeline details.

    Returns
    -------
    dict
        A structured dictionary containing the final comprehensive plan
        document and summaries.

    Raises
    ------
    ValueError
        If any of the dependent outputs are missing or malformed.
    RuntimeError
        If synthesis process encounters internal errors.

    Examples
    --------
    >>> produce_final_fund_plan_summary()
    {final_plan_document: This is a comprehensive final plan for the hedge
    fund..., executive_summary_bullet_points: [- Strategy focuses on long/short
    equity..., - Risk controls include VaR caps and position limits., -
    Technology stack features OMS and risk management systems., - Timeline
    includes legal formation and initial capital raise., - Fund structure is a
    Delaware LP with offshore components., - Fees are aligned with industry
    standards...], fund_structure_details: The fund is organized as a Delaware
    Limited Partnership..., risk_management_controls: Includes position limits,
    VaR caps, and stop-loss levels..., operational_steps: Daily operations
    include order management, execution, and reconciliation., fee_schedule:
    Management fee of 2%, performance fee of 20%, with a hurdle rate of 8%.,
    cost_model: Annual operating costs estimated at $2 million, covering staff,
    technology, and compliance., compliance_framework: Aligned with SEC and CFTC
    requirements, including filings and internal policies., hiring_plan: Initial
    team includes PM, risk manager, compliance officer, and operations staff.,
    technology_stack: Uses Bloomberg EMS, internal risk engine, and data
    warehouse., launch_timeline: Legal formation in Month 1, regulatory filings
    in Month 2, deployment tech in Month 3, capital raise in Month 4.,
    fundraising_materials: A well-structured pitch deck targeting accredited
    investors and family offices...}

    """
    return ProduceFinalFundPlanSummaryOutput(
        final_plan_document="",
        executive_summary_bullet_points="",
        fund_structure_details="",
        risk_management_controls="",
        operational_steps="",
        fee_schedule="",
        cost_model="",
        compliance_framework="",
        hiring_plan="",
        technology_stack="",
        launch_timeline="",
        fundraising_materials="",
    )