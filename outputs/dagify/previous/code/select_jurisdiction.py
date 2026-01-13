from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_objectives: List[str] = (
        Field(..., description="A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.")
    )


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    jurisdiction_name: str = (
        Field(..., description="The chosen fund domicile name")
    )
    rationale: str = (
        Field(..., description="One sentence explanation for selecting this jurisdiction")
    )
    pros: List[str] = (
        Field(..., description="Two key advantages of the chosen jurisdiction")
    )
    cons: List[str] = (
        Field(..., description="Two key disadvantages or challenges of the chosen jurisdiction")
    )


def select_jurisdiction(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> SelectJurisdictionOutput:
    """
    Chooses a fund domicile and returns a rationale, pros, and cons based on
    investment objectives.

    Parameters
    ----------
    investment_objectives : List[str]
        A list of up to eight bullet points outlining the hedge fund's
        primary business objectives, covering investment purpose,
        risk/reward expectations, and target market differentiation.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the chosen jurisdiction name, a one‑sentence
        rationale, two pros, and two cons.

    Raises
    ------
    ValueError
        If `investment_objectives` is empty or None.

    Examples
    --------
    >>> investment_objectives = [
    ...     "Generate high risk‑adjusted returns via long/short equity",
    ...     "Maintain volatility below 12%",
    ...     "Target institutional investors in North America"
    >>> ]
    >>> result = select_jurisdiction(investment_objectives)
    {
      "jurisdiction_name": "Cayman Islands",
      "rationale": "The Cayman Islands provide a flexible regulatory environment
    and tax neutrality that align with the fund's high‑return, low‑volatility
    strategy.",
      "pros": ["Tax‑free jurisdiction", "Well‑established legal framework for
    funds"],
      "cons": ["Limited investor protection compared to EU jurisdictions",
    "Higher compliance costs for certain regulatory filings"]
    }

    >>> investment_objectives = [
    ...     "Focus on global macro opportunities",
    ...     "Cap volatility at 15%",
    ...     "Target both institutional and accredited retail investors"
    >>> ]
    >>> result = select_jurisdiction(investment_objectives)
    {
      "jurisdiction_name": "Delaware, USA",
      "rationale": "Delaware offers a mature legal system and favorable
    corporate law for global macro funds seeking a U.S. presence.",
      "pros": ["Strong legal precedent", "Ease of accessing U.S. capital
    markets"],
      "cons": ["U.S. corporate tax implications", "Mandatory SEC reporting
    requirements"]
    }

    """
    return SelectJurisdictionOutput(
        jurisdiction_name="",
        rationale="",
        pros=[],
        cons=[],
    )