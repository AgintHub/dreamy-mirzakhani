from pydantic import BaseModel, Field
from typing import List


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


class ImplementSlippageModelOutput(BaseModel):
    """Pydantic model for implement_slippage_model node outputs."""
    bid_ask_spread_percent: float = (
        Field(..., description="Estimated average bid\u2011ask spread as a percentage of price")
    )
    price_impact_coefficient: float = (
        Field(..., description="Coefficient representing price impact per unit of trade size")
    )
    time_slippage_decay_factor: float = (
        Field(..., description="Decay factor for slippage over time during execution")
    )


def implement_slippage_model(preprocess_data_input: PreprocessDataOutput, **kwargs) -> ImplementSlippageModelOutput:
    """
    Generate a three‑parameter slippage model from a pre‑processed market data
    set.

    Parameters
    ----------
    preprocessed_metadata : dict
        Dictionary returned by `preprocess_data` containing `array_shape`,
        `num_assets`, `num_time_steps`, `price_normalized`,
        `volatility_calculated`, and `data_integrity` flags.
    market_liquidity_stats : dict
        Optional dictionary with pre‑computed liquidity statistics (e.g.,
        average spread, average depth, trade size distribution). If omitted,
        the function will compute these statistics directly from the
        pre‑processed array.

    Returns
    -------
    dict
        Dictionary with keys `bid_ask_spread_percent`,
        `price_impact_coefficient`, and `time_slippage_decay_factor`, each
        mapped to a float value.

    Raises
    ------
    ValueError
        Raised if `preprocessed_metadata` is missing required keys or if
        `data_integrity` is False.
    TypeError
        Raised if `market_liquidity_stats` contains non‑numeric values.

    Examples
    --------
    >>> # Example 1: Using only pre‑processed metadata
    >>> model = implement_slippage_model(preprocessed_metadata={
    ...     'array_shape': [10, 5, 252, 1],
    ...     'num_assets': 10,
    ...     'num_time_steps': 252,
    ...     'price_normalized': True,
    ...     'volatility_calculated': True,
    ...     'data_integrity': True
    >>> })
    >>> print(model['bid_ask_spread_percent'])
    0.0012

    >>> # Example 2: Providing explicit liquidity statistics
    >>> model = implement_slippage_model(preprocessed_metadata={
    ...     'array_shape': [5, 4, 500, 1],
    ...     'num_assets': 5,
    ...     'num_time_steps': 500,
    ...     'price_normalized': True,
    ...     'volatility_calculated': True,
    ...     'data_integrity': True
    >>> }, market_liquidity_stats={
    ...     'avg_spread': 0.0015,
    ...     'avg_depth': 2000,
    ...     'avg_trade_size': 1000
    >>> })
    >>> print(model['price_impact_coefficient'])
    0.000003

    """
    return ImplementSlippageModelOutput(
        bid_ask_spread_percent=0.0,
        price_impact_coefficient=0.0,
        time_slippage_decay_factor=0.0,
    )