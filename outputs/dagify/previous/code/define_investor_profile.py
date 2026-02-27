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


def define_investor_profile(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> DefineInvestorProfileOutput:
    """
    Define the target investor segment for the fund.

    Parameters
    ----------
    fund_objectives : dict
        Fund objectives as defined by the `clarify_fund_objectives` node.

    Returns
    -------
    dict
        Defined investor profile as a dictionary with keys for investor
        type, ticket size, risk tolerance, liquidity preference, and
        geographic focus.

    Examples
    --------
    >>> define_investor_profile(fund_objectives={
    ...     'investment_purpose': 'capital appreciation',
    ...     'target_return_profile': 'high return',
    ...     'competitive_advantage': 'unique investment strategy',
    ...     'long_term_vision': 'long-term growth',
    ...     'other_objectives': 'diversification'"
                "})
    {'investor_type': 'family offices', 'ticket_size': 1000000,
    'risk_tolerance': 0.7, 'liquidity_preference': 'medium', 'geographic_focus':
    'global'}

    """
    return DefineInvestorProfileOutput(
        investor_type="",
        ticket_size=0,
        risk_tolerance=0.0,
        liquidity_preference="",
        geographic_focus="",
    )