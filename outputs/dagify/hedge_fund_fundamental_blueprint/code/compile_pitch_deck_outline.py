from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    objectives_bullets: List[str] = (
        Field(..., description="Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets)")
    )


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    strategy_category: str = (
        Field(..., description="The chosen primary investment strategy category.")
    )
    rationale: str = (
        Field(..., description="A one-paragraph explanation aligning the strategy with the fund's objectives.")
    )
    risk_profile: str = (
        Field(..., description="A concise description of the expected risk profile associated with the chosen strategy.")
    )


class DefineInvestorProfileOutput(BaseModel):
    """Pydantic model for define_investor_profile node outputs."""
    typical_investor_types: List[str] = (
        Field(..., description="List of typical investor types (e.g., family offices, pensions)")
    )
    required_minimum_investment: int = (
        Field(..., description="Required minimum investment in USD")
    )
    liquidity_expectations: str = (
        Field(..., description="Description of liquidity expectations")
    )
    risk_tolerance_levels: List[str] = (
        Field(..., description="List of risk tolerance levels (e.g., aggressive, conservative)")
    )
    geographic_focus: str = (
        Field(..., description="Description of geographic focus")
    )


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    metric_names: List[str] = (
        Field(..., description="Names of the performance and risk metrics (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).")
    )
    target_values: List[float] = (
        Field(..., description="Numerical target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).")
    )
    rationale_texts: List[str] = (
        Field(..., description="Brief rationale for each target, explaining how it aligns with strategy and risk appetite.")
    )


class EstimateSetupAndOperatingCostsOutput(BaseModel):
    """Pydantic model for estimate_setup_and_operating_costs node outputs."""
    service_provider_name: List[str] = (
        Field(..., description="Names of the service providers or cost categories")
    )
    monthly_cost: List[float] = (
        Field(..., description="Monthly cost in USD for each service provider")
    )
    annual_total: List[float] = (
        Field(..., description="Annual total cost in USD for each service provider (Monthly Cost \u00d7 12)")
    )
    total_monthly_budget: float = (
        Field(..., description="Sum of all monthly costs across providers")
    )
    total_annual_budget: float = (
        Field(..., description="Sum of all annual totals across providers")
    )
    line_item_count: int = (
        Field(..., description="Number of line items included in the cost matrix (typically 10\u201115)")
    )
    budget_overview: str = (
        Field(..., description="Short textual summary of the overall budget, highlighting major cost drivers")
    )


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
    num_quant_controls: int = (
        Field(..., description="Number of quantifiable risk controls specified")
    )
    quant_controls_desc: List[str] = (
        Field(..., description="Descriptions of each quantifiable risk control")
    )
    num_qual_practices: int = (
        Field(..., description="Number of qualitative risk practices specified")
    )
    qual_practices_desc: List[str] = (
        Field(..., description="Descriptions of each qualitative risk practice")
    )


class DraftOperationsWorkflowOutput(BaseModel):
    """Pydantic model for draft_operations_workflow node outputs."""
    stages: List[str] = (
        Field(..., description="Ordered list of operational stages from idea generation to settlement")
    )
    responsible_parties: List[str] = (
        Field(..., description="Corresponding responsible party for each stage (e.g., \"In-house\", \"Prime Broker\")")
    )
    vendor_involved: List[bool] = (
        Field(..., description="Boolean flag per stage indicating whether a vendor is involved (true = vendor, false = in-house)")
    )
    stage_descriptions: List[str] = (
        Field(..., description="Brief description of activities performed in each stage")
    )


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


def compile_pitch_deck_outline(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, choose_investment_strategy_input: ChooseInvestmentStrategyOutput, define_investor_profile_input: DefineInvestorProfileOutput, set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, estimate_setup_and_operating_costs_input: EstimateSetupAndOperatingCostsOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, draft_operations_workflow_input: DraftOperationsWorkflowOutput, **kwargs) -> CompilePitchDeckOutlineOutput:
    """
    Compile a comprehensive outline for a 15-slide investor pitch deck,
    integrating insights from fund objectives, investment strategy, risk
    management, and operational compliance.

    Parameters
    ----------
    objectives : List[str]
        List of bullet points summarizing investment purpose, competitive
        advantages, target return profiles, and long-term vision.
    strategy : str
        Chosen primary investment strategy category.
    investor_profile : Dict[str, str]
        Dictionary containing typical investor types, required minimum
        investments, liquidity expectations, risk tolerance levels, and
        geographic focus.
    performance_targets : List[float]
        Numerical target values for performance metrics such as gross
        return, volatility, Sharpe ratio, and maximum drawdown tolerance.
    operating_costs : List[float]
        List of monthly costs in USD for each service provider, including
        vendor fees, technology implementation, and operational overhead.
    risk_management : List[str]
        List of quantifiable risk controls and qualitative risk practices
        aligned with performance targets.
    operations_workflow : List[str]
        Ordered list of operational stages from idea generation to
        settlement, including responsible parties and vendor involvement.

    Returns
    -------
    Dict[str, str or List[str]]
        A dictionary containing the compiled pitch deck outline, including
        slide titles, core messages, summaries of key sections, and Q&A
        topics.

    Raises
    ------
    ValueError
        If any of the input parameters are invalid or missing required
        information.

    Examples
    --------
    >>> compile_pitch_deck_outline({
    ...   'objectives': ['Investment purpose', 'Competitive advantages'],
    ...   'strategy': 'Long/Short Equity',
    ...   'investor_profile': {'typical_investor_types': ['Family Offices'],
    'required_minimum_investment': 1000000},
    ...   'performance_targets': [0.15, 0.10, 1.5, 0.20],
    ...   'operating_costs': [10000.0, 5000.0, 20000.0],
    ...   'risk_management': ['Position Limits', 'VaR', 'Liquidity Thresholds'],
    ...   'operations_workflow': ['Idea Generation', 'Portfolio Signal
    Generation', 'Order Entry']
    >>> })
    {'slide_titles': ['Introduction', 'Investment Strategy'], 'core_messages':
    ['Overview of investment approach', 'Details of strategy implementation'],
    ...}

    """
    return CompilePitchDeckOutlineOutput(
        slide_titles=[],
        core_messages=[],
        objectives_summary="",
        strategy_overview="",
        risk_return_analysis="",
        team_description="",
        operations_compliance_summary="",
        financials_summary="",
        qa_topics=[],
    )