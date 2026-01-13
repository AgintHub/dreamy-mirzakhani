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


class DevelopEntryRulesOutput(BaseModel):
    """Pydantic model for develop_entry_rules node outputs."""
    entry_conditions: List[str] = (
        Field(..., description="List of quantitative entry conditions as pseudo\u2011code equations")
    )
    parameter_values: List[float] = (
        Field(..., description="List of specific parameter values for the entry conditions")
    )
    condition_descriptions: List[str] = (
        Field(..., description="Brief description for each entry condition")
    )
    is_valid: bool = (
        Field(..., description="Whether the entry conditions are valid and can be used for initiating positions")
    )


def develop_entry_rules(choose_strategy_approach_input: ChooseStrategyApproachOutput, preprocess_data_input: PreprocessDataOutput, **kwargs) -> DevelopEntryRulesOutput:
    """
    Generate a list of entry conditions, parameters, descriptions, and a
    validity flag for a rule‑based trading strategy.

    Parameters
    ----------
    strategy_methodology : str
        Chosen strategy framework from `choose_strategy_approach`; one of
        'rule-based', 'machine-learning', or 'hybrid'.  Only 'rule-based'
        and 'hybrid' are supported for explicit pseudo‑code generation.
    preprocessed_data_meta : dict
        Metadata dictionary returned by `preprocess_data` indicating
        available indicators, asset count, and time steps.  The function
        uses this to validate that required inputs (e.g., EMA, ATR) exist.

    Returns
    -------
    dict
        Dictionary with keys: - `entry_conditions`: List[str] -
        `parameter_values`: List[float] - `condition_descriptions`:
        List[str] - `is_valid`: bool

    Raises
    ------
    ValueError
        If `strategy_methodology` is not supported or required indicators
        are missing from `preprocessed_data_meta`.
    TypeError
        If input types do not match the expected signatures.

    Examples
    --------
    >>> entry_rules = develop_entry_rules(
    ...     strategy_methodology='rule-based',
    ...     preprocessed_data_meta={'indicators': ['EMA20', 'EMA50', 'ATR',
    'StdDev2']})
    {
      'entry_conditions': [
        'EMA20 > EMA50',
        'Close > EMA20 + 2 * ATR',
        'StdDev2 > 1.5'
      ],
      'parameter_values': [20.0, 50.0, 2.0, 1.5],
      'condition_descriptions': [
        'Short‑term EMA crossing above long‑term EMA',
        'Price breaks above two‑ATR volatility breakout',
        'Standard deviation exceeds 1.5 standard deviations'
      ],
      'is_valid': True
    }

    >>> entry_rules = develop_entry_rules(
    ...     strategy_methodology='machine-learning',
    ...     preprocessed_data_meta={'indicators': ['EMA20']})
    ValueError: Unsupported strategy_methodology 'machine-learning' for entry
    rule generation.

    """
    return DevelopEntryRulesOutput(
        entry_conditions=[],
        parameter_values=[],
        condition_descriptions=[],
        is_valid=False,
    )