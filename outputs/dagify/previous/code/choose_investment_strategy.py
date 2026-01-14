from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_objectives: List[str] = (
        Field(..., description="A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.")
    )


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    chosen_strategy: str = (
        Field(..., description="The specific hedge fund strategy selected from the predefined categories")
    )
    alignment_explanation: str = (
        Field(..., description="A one-sentence explanation of how the chosen strategy supports the fund's objectives")
    )


def choose_investment_strategy(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> ChooseInvestmentStrategyOutput:
    """
    Selects a hedge fund strategy and explains its alignment with fund
    objectives.

    Parameters
    ----------
    investment_objectives : List[str]
        List of fund objectives defined in the clarify_fund_objectives node

    Returns
    -------
    {chosen_strategy: str, alignment_explanation: str}
        A dictionary containing the chosen strategy and its alignment
        explanation

    Raises
    ------
    ValueError
        If the chosen strategy is not one of the predefined categories

    Examples
    --------
    >>> investment_objectives = ['generate alpha', 'manage risk']
    >>> chosen_strategy = 'long/short equity'
    >>> alignment_explanation = 'The long/short equity strategy aligns with the
    objectives by generating alpha through stock selection and managing risk
    through hedging'
    {'chosen_strategy': 'long/short equity', 'alignment_explanation': 'The
    long/short equity strategy aligns with the objectives by generating alpha
    through stock selection and managing risk through hedging'}

    """
    return ChooseInvestmentStrategyOutput(
        chosen_strategy="",
        alignment_explanation="",
    )