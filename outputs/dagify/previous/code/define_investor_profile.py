from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_objectives: List[str] = (
        Field(..., description="A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.")
    )


class DefineInvestorProfileOutput(BaseModel):
    """Pydantic model for define_investor_profile node outputs."""
    investor_profile_characteristics: List[str] = (
        Field(..., description="List of 4 key characteristics of the target investor profile")
    )


def define_investor_profile(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> DefineInvestorProfileOutput:
    """
    Generates a concise list of four key traits defining the target investor
    demographic.

    Parameters
    ----------
    investment_objectives : List[str]
        Bullet list of the hedge fund’s primary business objectives, as
        produced by the `clarify_fund_objectives` node.

    Returns
    -------
    Dict[str, List[str]]
        Dictionary containing the key‑characteristics list under the key
        `investor_profile_characteristics`.

    Raises
    ------
    ValueError
        Raised if `investment_objectives` is empty or not a list of strings.

    Examples
    --------
    >>> investment_objectives = [
    ...     "Generate >12% annual gross return",
    ...     "Maintain volatility below 12%",
    ...     "Target institutional investors in North America",
    ...     "Offer 30‑day liquidity window"
    >>> ]
    >>> result = define_investor_profile(investment_objectives)
    >>> print(result['investor_profile_characteristics'])
    ["Institutional investors", "North America", "Minimum investment $5M",
    "30‑day liquidity window"]

    >>> investment_objectives = ["Focus on macro opportunities", "Target high
    net worth retail"]
    >>> result = define_investor_profile(investment_objectives)
    >>> print(result['investor_profile_characteristics'])
    ["High net worth retail", "Global reach", "Minimum investment $500k",
    "Monthly liquidity"]

    """
    return DefineInvestorProfileOutput(
        investor_profile_characteristics=[],
    )