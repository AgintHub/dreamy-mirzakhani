from ._set_performance_and_risk_targets.validate_input_parameters import validate_input_parameters
from ._set_performance_and_risk_targets.get_strategy_target_template import get_strategy_target_template
from ._set_performance_and_risk_targets.adjust_targets_for_risk_profile import adjust_targets_for_risk_profile
from ._set_performance_and_risk_targets.extract_metric_names import extract_metric_names
from ._set_performance_and_risk_targets.extract_target_values import extract_target_values
from ._set_performance_and_risk_targets.generate_target_rationales import generate_target_rationales

from pydantic import BaseModel, Field
from typing import List


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


class SetPerformanceAndRiskTargetsOutput(BaseModel):
    """Pydantic model for set_performance_and_risk_targets node outputs."""
    metric_names: List[str] = (
        Field(..., description = (
            "Names of the performance and risk metrics (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).")
        )
    )
    target_values: List[float] = (
        Field(..., description = (
            "Numerical target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).")
        )
    )
    rationale_texts: List[str] = (
        Field(..., description = (
            "Brief rationale for each target, explaining how it aligns with strategy and risk appetite.")
        )
    )


def set_performance_and_risk_targets(choose_investment_strategy_input: ChooseInvestmentStrategyOutput, **kwargs) -> SetPerformanceAndRiskTargetsOutput:
    """
    Compute annual performance and risk targets based on the selected investment
    strategy.

    Parameters
    ----------
    strategy_category : str
        Primary investment strategy category selected by the parent node
        (e.g., 'Long/Short Equity', 'Event-Driven', 'Global Macro').
    strategy_rationale : str
        Textual justification for the strategy, used to inform target
        setting.
    risk_profile : str
        Brief description of the expected risk profile (e.g., 'Moderate
        volatility, high return potential').

    Returns
    -------
    dict
        A dictionary with three keys: 'metric_names' (List[str]),
        'target_values' (List[float]), and 'rationale_texts' (List[str]).

    Raises
    ------
    ValueError
        Raised if any of the input parameters are empty or not a string.
    KeyError
        Raised if the strategy_category is not recognized in the internal
        mapping of target templates.

    Examples
    --------
    >>> strategy_category = 'Long/Short Equity'
    >>> strategy_rationale = 'Targeting alpha from long positions while hedging
    with short bets.'
    >>> risk_profile = 'Moderate volatility, high return potential'
    >>> targets = set_performance_and_risk_targets(strategy_category,
    strategy_rationale, risk_profile)
    >>> print(targets['metric_names'])
    >>> print(targets['target_values'])
    >>> print(targets['rationale_texts'])
    "['Gross Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown']"
    "[0.15, 0.10, 1.5, 0.20]"
    "['A 15% return aligns with long/short alpha goals.', '10% volatility
    matches moderate risk appetite.', 'Sharpe of 1.5 indicates efficient
    risk‑adjusted returns.', '20% drawdown tolerance protects capital during
    market stress.']

    >>> strategy_category = 'Event-Driven'
    >>> strategy_rationale = 'Profit from merger arbitrage and distressed
    events.'
    >>> risk_profile = 'High volatility, low correlation to markets'
    >>> targets = set_performance_and_risk_targets(strategy_category,
    strategy_rationale, risk_profile)
    >>> print(targets['target_values'])
    [0.18, 0.15, 1.2, 0.25]

    """
    validate_input_parameters(
        strategy_category=choose_investment_strategy_input.strategy_category,
        strategy_rationale=choose_investment_strategy_input.rationale,
        risk_profile=choose_investment_strategy_input.risk_profile
    )
    
    base_targets: dict = get_strategy_target_template(strategy_category=choose_investment_strategy_input.strategy_category)
    
    adjusted_targets: dict = adjust_targets_for_risk_profile(
        base_targets=base_targets,
        risk_profile=choose_investment_strategy_input.risk_profile
    )
    
    metric_names: List[str] = extract_metric_names(targets=adjusted_targets)
    target_values: List[float] = extract_target_values(targets=adjusted_targets)
    
    rationale_texts: List[str] = generate_target_rationales(
        metric_names=metric_names,
        target_values=target_values,
        strategy_rationale=choose_investment_strategy_input.rationale,
        risk_profile=choose_investment_strategy_input.risk_profile
    )
    
    return SetPerformanceAndRiskTargetsOutput(
        metric_names=metric_names,
        target_values=target_values,
        rationale_texts=rationale_texts
    )