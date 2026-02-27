from pydantic import BaseModel, Field


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_purpose: str = Field(..., description="Investment purpose")
    target_return_profile: str = Field(..., description="Target return profile")
    competitive_advantage: str = Field(..., description="Competitive advantage")
    long_term_vision: str = Field(..., description="Long-term vision")
    other_objectives: str = Field(..., description="Other fund objectives")


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_investment_strategy: str = (
        Field(..., description="The chosen high-level investment strategy")
    )
    justification: str = (
        Field(..., description="A one-sentence justification for the chosen investment strategy")
    )


def choose_investment_strategy(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> ChooseInvestmentStrategyOutput:
    """
    Selects a primary hedge-fund strategy category that best serves the
    objectives.

    Parameters
    ----------
    fund_objectives : dict
        Output from 'clarify_fund_objectives' node containing primary
        business objectives.

    Returns
    -------
    dict
        A dictionary containing the 'chosen_investment_strategy' and
        'justification' values.

    Examples
    --------
    >>> fund_objectives = {'investment_purpose': 'Capital appreciation',
    'target_return_profile': 'Above market', 'competitive_advantage': 'Active
    management', 'long_term_vision': 'Long-term growth'}"
    "chosen_investment_strategy, justification =
    choose_investment_strategy(fund_objectives)
    {'chosen_investment_strategy': 'Activemanagement', 'justification': 'To
    capture above-market returns through active management'}

    """
    return ChooseInvestmentStrategyOutput(
        chosen_investment_strategy="",
        justification="",
    )