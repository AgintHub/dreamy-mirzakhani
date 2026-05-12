from pydantic import BaseModel, Field


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_purpose: str = Field(..., description="Investment purpose")
    target_return_profile: str = Field(..., description="Target return profile")
    competitive_advantage: str = Field(..., description="Competitive advantage")
    long_term_vision: str = Field(..., description="Long-term vision")
    other_objectives: str = Field(..., description="Other fund objectives")


class DefineInvestorProfileOutput(BaseModel):
    """Pydantic model for define_investor_profile node outputs."""
    investor_type: str = (
        Field(..., description="The type of investor (e.g., family offices, pension funds, high-net-worth individuals)")
    )
    ticket_size: int = (
        Field(..., description="The typical ticket size for the investor")
    )
    risk_tolerance: float = (
        Field(..., description="The investor's risk tolerance")
    )
    liquidity_preference: str = (
        Field(..., description="The investor's liquidity preference")
    )
    geographic_focus: str = (
        Field(..., description="The investor's geographic focus")
    )


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_investment_strategy: str = (
        Field(..., description="The chosen high-level investment strategy")
    )
    justification: str = (
        Field(..., description="A one-sentence justification for the chosen investment strategy")
    )


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    annual_gross_return: float = (
        Field(..., description="Target annual gross return for the chosen strategy")
    )
    annual_volatility: float = (
        Field(..., description="Target annual volatility for the chosen strategy")
    )
    Sharpe_ratio: float = (
        Field(..., description="Target Sharpe ratio for the chosen strategy")
    )
    maximum_drawdown: float = (
        Field(..., description="Target maximum drawdown for the strategy")
    )
    performance_targets: float = (
        Field(..., description="A list of key performance metric targets for the strategy")
    )
    risk_targets: float = (
        Field(..., description="A list of risk metric targets for the strategy")
    )


class DraftFeeStructureOutput(BaseModel):
    """Pydantic model for draft_fee_structure node outputs."""
    management_fees: str = (
        Field(..., description="Management fees percentage or structure")
    )
    performance_fees: str = (
        Field(..., description="Performance fees percentage or structure")
    )
    hurdle_rate: str = (
        Field(..., description="Hurdle rate or other performance targets")
    )
    fee_schedules: str = (
        Field(..., description="List of fee schedules or payment structures")
    )


class DesignRiskManagementFrameworkOutput(BaseModel):
    """Pydantic model for design_risk_management_framework node outputs."""
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


def compile_pitch_deck_outline(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, define_investor_profile_input: DefineInvestorProfileOutput, choose_investment_strategy_input: ChooseInvestmentStrategyOutput, set_performance_and_risk_targets_input: SetPerformanceAndRiskTargetsOutput, draft_fee_structure_input: DraftFeeStructureOutput, design_risk_management_framework_input: DesignRiskManagementFrameworkOutput, **kwargs) -> CompilePitchDeckOutlineOutput:
    """
    Creates a 10-slide outline for an investor pitch deck.

    Parameters
    ----------
    investment_purpose : str
        Investment purpose from clarify_fund_objectives
    strategy : str
        Investment strategy from clarify_fund_objectives
    team : str
        Team title from define_investor_profile
    edge : str
        Edge title from clarify_fund_objectives
    risk_controls : str
        Risk controls title from design_risk_management_framework
    fees : str
        Fees title from draft_fee_structure
    target_returns : str
        Target returns title from set_performance_and_risk_targets
    market_opportunity : str
        Market opportunity title from clarify_fund_objectives
    service_providers : str
        Service providers title from list_service_providers
    timeline : str
        Timeline title from develop_timeline_and_milestones

    Returns
    -------
    -> dict[str, str]
        A dictionary with 10 keys representing the slide titles

    Raises
    ------
    ValueError
        If any input is missing

    Examples
    --------
    >>> investment_purpose = 'Invest in stocks and bonds'
    >>> strategy = 'Grow and diversify assets'
    >>> team = 'Our Investment Team'
    >>> edge = 'Our edge in the market'
    >>> risk_controls = 'Risk controls in place'
    >>> fees = 'Management and performance fees'
    >>> target_returns = 'Target return on investment'
    >>> market_opportunity = 'Market opportunity'
    >>> service_providers = 'Service providers'
    >>> timeline = 'Launch timeline'
    {'objectives': 'Objectives slide title', 'strategy': 'Strategy slide title',
    'team': 'Team slide title', 'edge': 'Edge slide title', 'risk_controls':
    'Risk controls slide title', 'fees': 'Fees slide title', 'target_returns':
    'Target returns slide title', 'market_opportunity': 'Market opportunity
    slide title', 'service_providers': 'Service providers slide title',
    'timeline': 'Timeline slide title'}

    """
    return CompilePitchDeckOutlineOutput(
        objectives="",
        strategy="",
        team="",
        edge="",
        risk_controls="",
        fees="",
        target_returns="",
        market_opportunity="",
        service_providers="",
        timeline="",
    )