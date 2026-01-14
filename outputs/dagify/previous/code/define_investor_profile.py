from ._define_investor_profile.extract_fund_objectives import extract_fund_objectives
from ._define_investor_profile.analyze_target_investor_types import analyze_target_investor_types
from ._define_investor_profile.calculate_minimum_investment import calculate_minimum_investment
from ._define_investor_profile.determine_liquidity_expectations import determine_liquidity_expectations
from ._define_investor_profile.assess_risk_tolerance_levels import assess_risk_tolerance_levels
from ._define_investor_profile.define_geographic_focus import define_geographic_focus

from pydantic import BaseModel, Field
from typing import List


class ClarifyFundObjectivesOutput(BaseModel):
    """Pydantic model for clarify_fund_objectives node outputs."""
    objectives_bullets: List[str] = (
        Field(..., description = (
            "Bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets)")
        )
    )


class DefineInvestorProfileOutput(BaseModel):
    """Pydantic model for define_investor_profile node outputs."""
    typical_investor_types: List[str] = (
        Field(..., description = (
            "List of typical investor types (e.g., family offices, pensions)")
        )
    )
    required_minimum_investment: int = (
        Field(..., description="Required minimum investment in USD")
    )
    liquidity_expectations: str = (
        Field(..., description="Description of liquidity expectations")
    )
    risk_tolerance_levels: List[str] = (
        Field(..., description = (
            "List of risk tolerance levels (e.g., aggressive, conservative)")
        )
    )
    geographic_focus: str = (
        Field(..., description="Description of geographic focus")
    )


def define_investor_profile(clarify_fund_objectives_input: ClarifyFundObjectivesOutput, **kwargs) -> DefineInvestorProfileOutput:
    """
    Define the ideal investor demographic for a hedge fund

    Parameters
    ----------
    fund_objectives : str
        Primary business objectives for launching the hedge fund

    Returns
    -------
    dict
        A dictionary containing typical investor types, required minimum
        investment, liquidity expectations, risk tolerance levels, and
        geographic focus

    Raises
    ------
    ValueError
        If required minimum investment is not a positive integer

    Examples
    --------
    >>> define_investor_profile(fund_objectives='Maximize returns while
    minimizing risk')
    >>> print(output['typical_investor_types'])  # Output: ['family offices',
    'pensions']
    >>> print(output['required_minimum_investment'])  # Output: 1000000
    >>> print(output['liquidity_expectations'])  # Output: 'Quarterly
    redemptions'
    >>> print(output['risk_tolerance_levels'])  # Output: ['aggressive',
    'conservative']
    >>> print(output['geographic_focus'])  # Output: 'North America'
    {'typical_investor_types': ['family offices', 'pensions'],
    'required_minimum_investment': 1000000, 'liquidity_expectations': 'Quarterly
    redemptions', 'risk_tolerance_levels': ['aggressive', 'conservative'],
    'geographic_focus': 'North America'}

    """
    fund_objectives: str = extract_fund_objectives(objectives_bullets=clarify_fund_objectives_input.objectives_bullets)
    
    investor_types: List[str] = analyze_target_investor_types(objectives=fund_objectives)
    
    minimum_investment: int = calculate_minimum_investment(fund_strategy=fund_objectives, target_investors=investor_types)
    
    if minimum_investment <= 0:
        raise ValueError("If required minimum investment is not a positive integer")
    
    liquidity_terms: str = determine_liquidity_expectations(investor_types=investor_types, fund_objectives=fund_objectives)
    
    risk_levels: List[str] = assess_risk_tolerance_levels(fund_strategy=fund_objectives, target_demographics=investor_types)
    
    geographic_target: str = define_geographic_focus(objectives=fund_objectives, investor_base=investor_types)
    
    return DefineInvestorProfileOutput(
        typical_investor_types=investor_types,
        required_minimum_investment=minimum_investment,
        liquidity_expectations=liquidity_terms,
        risk_tolerance_levels=risk_levels,
        geographic_focus=geographic_target
    )