from pydantic import BaseModel, Field
from typing import List


class ChooseStrategyApproachOutput(BaseModel):
    """Pydantic model for choose_strategy_approach node outputs."""
    methodology: str = (
        Field(..., description="Chosen methodology type: 'rule-based', 'machine-learning', or 'hybrid'")
    )
    justifications: List[str] = (
        Field(..., description="Short bullet points explaining why the chosen methodology is suitable for the strategy objective")
    )
    technical_reasons: List[str] = (
        Field(..., description="Specific technical reasons (e.g., data availability, model interpretability, computational cost) supporting the methodology choice")
    )


class PreprocessDataOutput(BaseModel):
    """Pydantic model for preprocess_data node outputs."""
    array_shape: List[int] = (
        Field(..., description="Dimensions of the 4D numpy array (e.g., [n_assets, n_features, n_time_steps, n_channels])")
    )
    num_assets: int = (
        Field(..., description="Number of distinct assets included in the dataset")
    )
    num_time_steps: int = (
        Field(..., description="Total number of time steps after alignment")
    )
    price_normalized: bool = (
        Field(..., description="Indicates whether price values have been normalized")
    )
    volatility_calculated: bool = (
        Field(..., description="Indicates whether volatility metrics have been computed")
    )
    data_integrity: bool = (
        Field(..., description="True if the dataset passes all integrity checks (no missing values, consistent timestamps)")
    )


class DevelopExitRulesOutput(BaseModel):
    """Pydantic model for develop_exit_rules node outputs."""
    exit_conditions: List[str] = (
        Field(..., description="List of quantitative exit conditions expressed as pseudo-code equations.")
    )
    parameter_values: List[float] = (
        Field(..., description="Parameter values associated with each exit condition.")
    )
    exit_order_types: List[str] = (
        Field(..., description="Order type for each exit condition (e.g., 'market', 'limit').")
    )
    is_valid: bool = (
        Field(..., description="Whether the generated exit rules satisfy all validation checks.")
    )


def develop_exit_rules(choose_strategy_approach_input: ChooseStrategyApproachOutput, preprocess_data_input: PreprocessDataOutput, **kwargs) -> DevelopExitRulesOutput:
    """
    Generate a validated set of quantitative exit rules for a trading strategy.

    Parameters
    ----------
    methodology : str
        Strategy framework selected by `choose_strategy_approach` ('rule-
        based', 'machine-learning', or 'hybrid').
    data_meta : dict
        Metadata dictionary from `preprocess_data` (contains asset list,
        volatility metrics, etc.).

    Returns
    -------
    dict
        Dictionary containing exit_conditions (List[str]), parameter_values
        (List[float]), exit_order_types (List[str]), and is_valid (bool).

    Raises
    ------
    ValueError
        If the methodology string is not one of the supported types.
    KeyError
        If required keys (e.g., 'ATR', 'volatility') are missing from the
        data_meta.

    Examples
    --------
    >>> # Assume a rule‑based strategy and pre‑processed data containing 14‑day
    ATR
    >>> rules = develop_exit_rules(methodology='rule-based',
    data_meta={'ATR_14': 0.012, 'volatility': 0.18})
    >>> print(rules['exit_conditions'])
    ['price <= entry_price * (1 - 0.02 * ATR_14)',
     'price >= entry_price * (1 + 0.03 * ATR_14)',
     'time_in_position >= 10']

    >>> # Machine‑learning strategy with volatility‑based exit
    >>> rules = develop_exit_rules(methodology='machine-learning',
    data_meta={'volatility': 0.22})
    >>> print(rules['exit_order_types'])
    ['market', 'market', 'limit']

    """
    return DevelopExitRulesOutput(
        exit_conditions=[],
        parameter_values=[],
        exit_order_types=[],
        is_valid=False,
    )