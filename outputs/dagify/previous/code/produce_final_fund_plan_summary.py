from ._produce_final_fund_plan_summary.validate_required_inputs import validate_required_inputs
from ._produce_final_fund_plan_summary.extract_strategy_summary import extract_strategy_summary
from ._produce_final_fund_plan_summary.extract_target_returns import extract_target_returns
from ._produce_final_fund_plan_summary.synthesize_risk_controls import synthesize_risk_controls
from ._produce_final_fund_plan_summary.summarize_regulatory_structure import summarize_regulatory_structure
from ._produce_final_fund_plan_summary.extract_personnel_summary import extract_personnel_summary
from ._produce_final_fund_plan_summary.synthesize_technology_overview import synthesize_technology_overview
from ._produce_final_fund_plan_summary.create_launch_timeline import create_launch_timeline
from ._produce_final_fund_plan_summary.compile_executive_summary import compile_executive_summary

from pydantic import BaseModel, Field
from typing import List


class CompilePitchDeckOutlineOutput(BaseModel):
    """Pydantic model for compile_pitch_deck_outline node outputs."""
    slide_titles: List[str] = (
        Field(..., description="List of slide titles in the presentation")
    )
    core_messages: List[str] = (
        Field(..., description="List of core messages for each slide")
    )
    objectives_summary: str = (
        Field(..., description="Summary of the objectives slides")
    )
    strategy_overview: str = (
        Field(..., description="Overview of the strategy slides")
    )
    risk_return_analysis: str = (
        Field(..., description="Summary of the risk-return analysis slide")
    )
    team_description: str = (
        Field(..., description="Description of the team slide")
    )
    operations_compliance_summary: str = (
        Field(..., description="Summary of the operations/compliance slides")
    )
    financials_summary: str = (
        Field(..., description="Summary of the financials slides")
    )
    qa_topics: List[str] = Field(..., description="List of Q&A topics")


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_name: List[str] = (
        Field(..., description = (
            "Names of the service providers or cost categories")
        )
    )
    monthly_cost: List[float] = (
        Field(..., description="Monthly cost in USD for each service provider")
    )
    annual_total: List[float] = (
        Field(..., description = (
            "Annual total cost in USD for each service provider (Monthly Cost \u00d7 12)")
        )
    )
    total_monthly_budget: float = (
        Field(..., description="Sum of all monthly costs across providers")
    )
    total_annual_budget: float = (
        Field(..., description="Sum of all annual totals across providers")
    )
    line_item_count: int = (
        Field(..., description = (
            "Number of line items included in the cost matrix (typically 10\u201115)")
        )
    )
    budget_overview: str = (
        Field(..., description = (
            "Short textual summary of the overall budget, highlighting major cost drivers")
        )
    )


class DesignComplianceProgramOutput(BaseModel):
    """Pydantic model for design_compliance_program node outputs."""
    accreditation_items: List[str] = (
        Field(..., description = (
            "List of investor accreditation standard items required for compliance")
        )
    )
    accreditation_dates: List[str] = (
        Field(..., description = (
            "Implementation dates for each accreditation item (YYYY-MM-DD format)")
        )
    )
    subscription_items: List[str] = (
        Field(..., description = (
            "List of subscription verification procedures to be followed")
        )
    )
    subscription_dates: List[str] = (
        Field(..., description = (
            "Implementation dates for each subscription procedure (YYYY-MM-DD format)")
        )
    )
    aml_items: List[str] = (
        Field(..., description = (
            "List of anti-money laundering policy items to implement")
        )
    )
    aml_dates: List[str] = (
        Field(..., description = (
            "Implementation dates for each AML policy item (YYYY-MM-DD format)")
        )
    )


class ProduceFinalFundPlanSummaryOutput(BaseModel):
    """Pydantic model for produce_final_fund_plan_summary node outputs."""
    summary: str = Field(..., description="The executive summary text")
    strategy: str = Field(..., description="Summary of the investment strategy")
    target_returns: str = (
        Field(..., description="Description of target returns")
    )
    risk_controls: str = (
        Field(..., description="Overview of risk controls in place")
    )
    regulatory_structure: str = (
        Field(..., description="Description of the regulatory structure")
    )
    personnel: str = (
        Field(..., description="Summary of key personnel and their roles")
    )
    technology: str = Field(..., description="Overview of the technology stack")
    launch_timeline: str = (
        Field(..., description="Description of the launch timeline")
    )


def produce_final_fund_plan_summary(compile_pitch_deck_outline_input: CompilePitchDeckOutlineOutput, estimate_setup_and_operating_costs_input: EstimateSetupAndOperatingCostsOutput, design_compliance_program_input: DesignComplianceProgramOutput, **kwargs) -> ProduceFinalFundPlanSummaryOutput:
    """
    Produces a 200-word executive summary covering strategy, target returns,
    risk controls, regulatory structure, personnel, technology, and launch
    timeline.

    Parameters
    ----------
    pitch_deck_outline : dict
        Output from compile_pitch_deck_outline node
    costs_estimation : dict
        Output from estimate_setup_and_operating_costs node
    compliance_program : dict
        Output from design_compliance_program node

    Returns
    -------
    dict
        Dictionary containing the executive summary and its components

    Raises
    ------
    ValueError
        If any of the input nodes are missing required fields

    Examples
    --------
    >>> pitch_deck_outline = {'strategy_overview': 'Long/short equity',
    'risk_return_analysis': 'Target 15% annual return'}
    >>> costs_estimation = {'total_annual_budget': 1000000.0, 'budget_overview':
    'Detailed breakdown of costs'}
    >>> compliance_program = {'accreditation_items': ['Item 1', 'Item 2'],
    'aml_items': ['AML Item 1']}
    >>> produce_final_fund_plan_summary(pitch_deck_outline, costs_estimation,
    compliance_program)
    {'summary': '* Strategy: Long/short equity\n* Target Returns: 15% annual
    return\n* Risk Controls: Detailed risk management framework\n* Regulatory
    Structure: Registered with regulatory bodies\n* Personnel: Experienced team
    in place\n* Technology: State-of-the-art trading platform\n* Launch
    Timeline: Q1 2025'}

    """
    validate_required_inputs(pitch_deck_outline=compile_pitch_deck_outline_input, costs_estimation=estimate_setup_and_operating_costs_input, compliance_program=design_compliance_program_input)
    
    strategy_summary: str = extract_strategy_summary(strategy_overview=compile_pitch_deck_outline_input.strategy_overview)
    
    target_returns_summary: str = extract_target_returns(risk_return_analysis=compile_pitch_deck_outline_input.risk_return_analysis)
    
    risk_controls_summary: str = synthesize_risk_controls(operations_compliance=compile_pitch_deck_outline_input.operations_compliance_summary, compliance_items=design_compliance_program_input.aml_items)
    
    regulatory_structure_summary: str = summarize_regulatory_structure(accreditation_items=design_compliance_program_input.accreditation_items, subscription_items=design_compliance_program_input.subscription_items)
    
    personnel_summary: str = extract_personnel_summary(team_description=compile_pitch_deck_outline_input.team_description)
    
    technology_summary: str = synthesize_technology_overview(operations_summary=compile_pitch_deck_outline_input.operations_compliance_summary)
    
    launch_timeline_summary: str = create_launch_timeline(compliance_dates=design_compliance_program_input.accreditation_dates, budget_info=estimate_setup_and_operating_costs_input.budget_overview)
    
    executive_summary: str = compile_executive_summary(strategy=strategy_summary, target_returns=target_returns_summary, risk_controls=risk_controls_summary, regulatory_structure=regulatory_structure_summary, personnel=personnel_summary, technology=technology_summary, launch_timeline=launch_timeline_summary, target_word_count=200)
    
    return ProduceFinalFundPlanSummaryOutput(
        summary=executive_summary,
        strategy=strategy_summary,
        target_returns=target_returns_summary,
        risk_controls=risk_controls_summary,
        regulatory_structure=regulatory_structure_summary,
        personnel=personnel_summary,
        technology=technology_summary,
        launch_timeline=launch_timeline_summary,
    )