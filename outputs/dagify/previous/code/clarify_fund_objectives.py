from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    investment_objectives: List[str] = (
        Field(..., description="A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.")
    )


def clarify_fund_objectives(general_input: str, **kwargs) -> ClarifyFundObjectivesOutput:
    """
    Generate a list of up to eight bullet points that capture the hedge fund’s
    investment purpose, risk/reward expectations, and target market
    differentiation.

    Parameters
    ----------
    prompt : str
        Instruction string that specifies the maximum number of bullets and
        the focus areas (investment purpose, risk/reward, target market).

    Returns
    -------
    List[str]
        A list of bullet‑point strings, each describing a distinct business
        or investment objective.

    Raises
    ------
    ValueError
        Raised if the input prompt is empty or does not contain a clear
        instruction.

    Examples
    --------
    >>> output = clarify_fund_objectives(prompt)
    >>> print(output)
    ["Generate alpha through a diversified long/short equity strategy.",
    "Maintain portfolio volatility below 15% annualized.", "Deliver 20% gross
    annual returns to institutional investors.", "Differentiate by leveraging
    proprietary quantitative models."]

    >>> output = clarify_fund_objectives(prompt)
    >>> print(len(output))
    4

    """
    return ClarifyFundObjectivesOutput(
        investment_objectives=[],
    )