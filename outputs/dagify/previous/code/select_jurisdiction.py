from ._select_jurisdiction.validate_objectives_input import validate_objectives_input
from ._select_jurisdiction.extract_fund_requirements import extract_fund_requirements
from ._select_jurisdiction.get_jurisdiction_candidates import get_jurisdiction_candidates
from ._select_jurisdiction.score_jurisdictions import score_jurisdictions
from ._select_jurisdiction.select_optimal_jurisdiction import select_optimal_jurisdiction
from ._select_jurisdiction.extract_key_advantages import extract_key_advantages
from ._select_jurisdiction.extract_key_disadvantages import extract_key_disadvantages
from ._select_jurisdiction.generate_justification import generate_justification

from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    objectives_bullets: List[str] = (
        Field(..., description = (
            "Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets)")
        )
    )


class SelectJurisdictionOutput(BaseModel):
    """Pydantic model for select_jurisdiction node outputs."""
    chosen_jurisdiction: str = (
        Field(..., description="The name of the selected fund domicile")
    )
    advantages: List[str] = (
        Field(..., description = (
            "A list of two key advantages of the chosen jurisdiction")
        )
    )
    disadvantages: List[str] = (
        Field(..., description = (
            "A list of two key disadvantages of the chosen jurisdiction")
        )
    )
    justification: str = (
        Field(..., description = (
            "Brief explanation linking the jurisdiction to the fund\u2019s objectives and strategy")
        )
    )


def select_jurisdiction(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> SelectJurisdictionOutput:
    """
    Selects an optimal regulatory domicile for a hedge fund based on tax
    efficiency, regulatory simplicity, and investor appeal.

    Parameters
    ----------
    objectives_bullets : List[str]
        Bullet points summarizing the fund's primary business objectives, as
        produced by the clarify_fund_objectives node.

    Returns
    -------
    dict
        A dictionary containing the chosen jurisdiction, its advantages and
        disadvantages, and a justification string.

    Raises
    ------
    ValueError
        If `objectives_bullets` is empty or not a list of strings.

    Examples
    --------
    >>> # Assume objectives_bullets derived from clarify_fund_objectives
    >>> objectives_bullets = [
    ...     "High alpha generation via event-driven strategies",
    ...     "Target annual gross return of 20%",
    ...     "Limited regulatory reporting to speed decision-making",
    ...     "Appeal to family offices and pension funds",
    >>> ]
    >>> result = select_jurisdiction(objectives_bullets)
    >>> print(result['chosen_jurisdiction'])
    "Cayman Islands"

    >>> print(result['advantages'])
    >>> print(result['disadvantages'])
    >>> print(result['justification'])
    "['Zero corporate tax', 'Flexible regulatory regime']"
    "['Perceived political risk', 'Limited local investor base']"
    "'The Cayman Islands provide a tax-neutral environment and minimal reporting
    requirements, aligning with the fund’s aggressive return target and speed of
    execution, while acknowledging the geopolitical and market liquidity
    concerns.'

    """
    validate_objectives_input(objectives=clarify_fund_objectives_input.objectives_bullets)
    
    parsed_requirements: dict = extract_fund_requirements(objectives=clarify_fund_objectives_input.objectives_bullets)
    
    candidate_jurisdictions: List[dict] = get_jurisdiction_candidates()
    
    scored_jurisdictions: List[dict] = score_jurisdictions(
        candidates=candidate_jurisdictions,
        requirements=parsed_requirements
    )
    
    best_jurisdiction: dict = select_optimal_jurisdiction(scored_options=scored_jurisdictions)
    
    advantages: List[str] = extract_key_advantages(jurisdiction_data=best_jurisdiction, count=2)
    disadvantages: List[str] = extract_key_disadvantages(jurisdiction_data=best_jurisdiction, count=2)
    
    justification_text: str = generate_justification(
        jurisdiction=best_jurisdiction['name'],
        objectives=clarify_fund_objectives_input.objectives_bullets,
        advantages=advantages,
        disadvantages=disadvantages
    )
    
    return SelectJurisdictionOutput(
        chosen_jurisdiction=best_jurisdiction['name'],
        advantages=advantages,
        disadvantages=disadvantages,
        justification=justification_text
    )