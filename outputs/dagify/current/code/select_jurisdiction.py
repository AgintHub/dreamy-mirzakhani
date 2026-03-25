from pydantic import BaseModel, Field


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_purpose: str = Field(..., description="Investment purpose")
    target_return_profile: str = Field(..., description="Target return profile")
    competitive_advantage: str = Field(..., description="Competitive advantage")
    long_term_vision: str = Field(..., description="Long-term vision")
    other_objectives: str = Field(..., description="Other fund objectives")


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    chosen_jurisdiction: str = (
        Field(..., description="The selected jurisdiction for the fund (e.g., Cayman, Delaware, Luxembourg).")
    )
    advantages: str = (
        Field(..., description="A list containing two advantages of the chosen jurisdiction.")
    )
    disadvantages: str = (
        Field(..., description="A list containing two disadvantages of the chosen jurisdiction.")
    )
    rationale: str = (
        Field(..., description="The reasoning behind selecting this jurisdiction, including strategic, regulatory, and operational factors.")
    )


def select_jurisdiction(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> SelectJurisdictionOutput:
    """
    Selects a suitable jurisdiction for the hedge fund based on fund objectives
    and strategic considerations.

    Parameters
    ----------
    clarify_fund_objectives : dict
        The output dictionary from the clarify_fund_objectives node
        containing core fund objectives.

    Returns
    -------
    dict
        A dictionary with the selected jurisdiction, its advantages,
        disadvantages, and accompanying rationale.

    Raises
    ------
    ValueError
        Raised if fund objectives are insufficiently specified or missing
        necessary details for jurisdiction analysis.

    Examples
    --------
    >>> select_jurisdiction({'investment_purpose': 'Capital growth',
    'target_return_profile': '8-12%', 'competitive_advantage': 'Tax efficiency',
    'long_term_vision': 'Global expansion', 'other_objectives': 'Liquidity
    flexibility'})
    {'chosen_jurisdiction': 'Cayman', 'advantages': ['Tax neutrality', 'Flexible
    fund structuring'], 'disadvantages': ['Less investor transparency',
    'Perceived regulatory laxity'], 'rationale': 'Cayman aligns with objectives
    due to tax benefits and flexible legal frameworks suited for offshore
    structures.'}

    >>> select_jurisdiction({'investment_purpose': 'Stable income',
    'target_return_profile': '6-10%', 'competitive_advantage': 'Robust
    regulation', 'long_term_vision': 'Regional focus', 'other_objectives':
    'Liquidity retention'})
    {'chosen_jurisdiction': 'Delaware', 'advantages': ['Solid legal precedent',
    'Familiar regulatory environment'], 'disadvantages': ['Taxation on fund
    offshore', 'Less favorable for non-US investors'], 'rationale': 'Delaware is
    chosen for its well-established legal system and familiarity in US-based
    funds.'}

    """
    return SelectJurisdictionOutput(
        chosen_jurisdiction="",
        advantages="",
        disadvantages="",
        rationale="",
    )