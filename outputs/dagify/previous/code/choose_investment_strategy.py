from ._choose_investment_strategy.validate_objectives_bullets import validate_objectives_bullets
from ._choose_investment_strategy.parse_fund_objectives import parse_fund_objectives
from ._choose_investment_strategy.determine_strategy_category import determine_strategy_category
from ._choose_investment_strategy.generate_strategy_rationale import generate_strategy_rationale
from ._choose_investment_strategy.assess_risk_profile import assess_risk_profile

from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    objectives_bullets: List[str] = (
        Field(..., description = (
            "Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets)")
        )
    )


class ChooseInvestmentStrategyOutput(BaseModel):
    """Pydantic model for choose_investment_strategy node outputs."""
    strategy_category: str = (
        Field(..., description = (
            "The chosen primary investment strategy category.")
        )
    )
    rationale: str = (
        Field(..., description = (
            "A one-paragraph explanation aligning the strategy with the fund's objectives.")
        )
    )
    risk_profile: str = (
        Field(..., description = (
            "A concise description of the expected risk profile associated with the chosen strategy.")
        )
    )


def choose_investment_strategy(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> ChooseInvestmentStrategyOutput:
    """
    Selects the primary investment strategy category and generates a rationale
    and risk profile based on the fund's objectives.

    Parameters
    ----------
    objectives_bullets : List[str]
        Bullet points summarizing the fund’s investment purpose, competitive
        advantages, target return profiles, and long-term vision (maximum 8
        bullets). These are the outputs of the parent node
        `clarify_fund_objectives`.

    Returns
    -------
    Dict[str, str]
        A dictionary with keys `strategy_category`, `rationale`, and
        `risk_profile`, each mapping to a string describing the chosen
        strategy, its alignment with objectives, and the anticipated risk
        characteristics.

    Raises
    ------
    ValueError
        Raised if `objectives_bullets` is empty or does not contain any
        actionable points.
    RuntimeError
        Raised if no suitable strategy category can be inferred from the
        provided objectives.

    Examples
    --------
    >>> strategy = choose_investment_strategy(objectives_bullets=[
    ...     "Generate 15% annual gross return through diversified equity
    strategies.",
    ...     "Maintain low correlation with global macro factors.",
    ...     "Leverage proprietary quantitative models.",
    ...     "Target a volatility of 8-10%.",
    ...     "Seek alpha in both bull and bear markets.",
    ...     "Operate within a liquid asset universe.",
    ...     "Aim for a Sharpe ratio above 1.5.",
    ...     "Focus on long-term capital preservation."] )
    >>> print(strategy['strategy_category'])
    >>> print(strategy['rationale'])
    >>> print(strategy['risk_profile'])
    "Event‑Driven Equity"\n"The fund will focus on exploiting corporate event
    catalysts such as M&A, restructurings, and spin‑offs, leveraging its
    quantitative edge to generate asymmetric returns in both bullish and bearish
    market regimes. This aligns with the objective of producing 15% gross annual
    returns while maintaining low correlation to macro trends.\n"The strategy
    offers medium to high volatility with potential for sharp downside during
    illiquid event periods, but mitigated by strict position limits and
    liquidity buffers. Expected volatility: 8‑10% with drawdown controls at
    25%."

    >>> strategy = choose_investment_strategy(objectives_bullets=[
    ...     "Provide long‑term growth for institutional pension funds.",
    ...     "Capitalize on global macro opportunities.",
    ...     "Maintain a conservative risk appetite."] )
    >>> print(strategy['strategy_category'])
    "Global Macro"

    """
    objectives_bullets = clarify_fund_objectives_input.objectives_bullets
    
    validated_objectives: List[str] = validate_objectives_bullets(objectives_bullets=objectives_bullets)
    
    parsed_objectives: dict = parse_fund_objectives(objectives_bullets=validated_objectives)
    
    strategy_category: str = determine_strategy_category(parsed_objectives=parsed_objectives)
    
    rationale: str = generate_strategy_rationale(strategy_category=strategy_category, objectives=parsed_objectives)
    
    risk_profile: str = assess_risk_profile(strategy_category=strategy_category, objectives=parsed_objectives)
    
    return ChooseInvestmentStrategyOutput(
        strategy_category=strategy_category,
        rationale=rationale,
        risk_profile=risk_profile
    )