from ._clarify_fund_objectives.validate_prompt_text import validate_prompt_text
from ._clarify_fund_objectives.preprocess_prompt_for_objectives import preprocess_prompt_for_objectives
from ._clarify_fund_objectives.generate_objectives_from_prompt import generate_objectives_from_prompt
from ._clarify_fund_objectives.format_objectives_bullets import format_objectives_bullets
from ._clarify_fund_objectives.validate_bullet_constraints import validate_bullet_constraints

from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    objectives_bullets: List[str] = (
        Field(..., description = (
            "Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets)")
        )
    )


def clarify_fund_objectives(general_input: str, **kwargs) -> ClarifyFundObjectivesOutput:
    """
    Generate a concise list of up to eight bullet points that articulate the
    hedge fund’s investment purpose, competitive advantages, target return
    expectations, and long‑term vision.

    Parameters
    ----------
    prompt_text : str
        Raw textual instruction supplied by the user or orchestrator. The
        function consumes this prompt verbatim to produce the bullet list.

    Returns
    -------
    Dict[str, List[str]]
        Dictionary with a single key `objectives_bullets` mapping to a list
        of strings, each string being a bullet point.

    Raises
    ------
    ValueError
        If `prompt_text` is empty or not a string.
    RuntimeError
        If the generated list exceeds eight bullets or contains non‑string
        elements.

    Examples
    --------
    >>> output = clarify_fund_objectives("State the primary business objectives
    for launching the hedge fund. List investment purpose, competitive
    advantages, target return profiles, and long‑term vision in concise bullet
    points (max 8 bullets)")
    {'objectives_bullets': ['Deliver alpha through long/short equity strategies
    targeting 20% annual gross returns.', 'Leverage proprietary quantitative
    models for edge in volatility forecasting.', 'Maintain a diversified
    portfolio across U.S. and EU markets to mitigate geopolitical risk.', 'Offer
    transparent fee structures to attract family offices.', 'Invest in
    ESG‑compliant assets to align with investor values.', 'Build a scalable
    technology platform to support high‑frequency data analytics.', 'Scale to
    $500M AUM within five years by tapping institutional capital.', 'Commit to a
    10‑year growth roadmap with quarterly performance reviews.']}

    >>> output = clarify_fund_objectives("Provide concise objectives for a hedge
    fund focused on event‑driven opportunities.")
    {'objectives_bullets': ['Capture mispricing from corporate events with a 15%
    gross return target.', 'Utilize a concentrated portfolio of 10‑20 positions
    for high conviction.', 'Maintain liquidity through short‑term debt and cash
    reserves.', 'Employ a risk‑parity framework to cap volatility at 12%.',
    'Offer fee‑structured performance incentives to align manager and investor
    interests.', 'Leverage a network of deal partners for early access to
    events.', 'Expand to $250M AUM over three years.', 'Commit to ESG compliance
    and regular third‑party audits.']}

    """
    validated_prompt: str = validate_prompt_text(prompt_text=general_input)
    processed_prompt: str = preprocess_prompt_for_objectives(prompt=validated_prompt)
    raw_objectives: List[str] = generate_objectives_from_prompt(processed_prompt=processed_prompt)
    formatted_objectives: List[str] = format_objectives_bullets(raw_bullets=raw_objectives)
    validated_bullets: List[str] = validate_bullet_constraints(bullets=formatted_objectives, max_count=8)
    return ClarifyFundObjectivesOutput(objectives_bullets=validated_bullets)