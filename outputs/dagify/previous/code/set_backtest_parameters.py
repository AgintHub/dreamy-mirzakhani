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


class SetBacktestParametersOutput(BaseModel):
    """Pydantic model for set_backtest_parameters node outputs."""
    in_sample_start: str = (
        Field(..., description="Start date of the in-sample period (YYYY-MM-DD)")
    )
    in_sample_end: str = (
        Field(..., description="End date of the in-sample period (YYYY-MM-DD)")
    )
    out_sample_start: str = (
        Field(..., description="Start date of the out-of-sample period (YYYY-MM-DD)")
    )
    out_sample_end: str = (
        Field(..., description="End date of the out-of-sample period (YYYY-MM-DD)")
    )
    montecarlo_min: int = (
        Field(..., description="Minimum number of Monte Carlo simulations to run")
    )
    montecarlo_max: int = (
        Field(..., description="Maximum number of Monte Carlo simulations to run")
    )
    walkforward_window_days: List[int] = (
        Field(..., description="List of window sizes (in days) for walk-forward analysis")
    )


def set_backtest_parameters(preprocess_data_input: PreprocessDataOutput, **kwargs) -> SetBacktestParametersOutput:
    """
    Configure the backtesting framework for a quantitative strategy.

    Parameters
    ----------
    in_sample_start : str
        Start date of the in-sample period in 'YYYY-MM-DD' format.
    in_sample_end : str
        End date of the in-sample period in 'YYYY-MM-DD' format.
    out_sample_start : str
        Start date of the out-of-sample period in 'YYYY-MM-DD' format.
    out_sample_end : str
        End date of the out-of-sample period in 'YYYY-MM-DD' format.
    montecarlo_min : int
        Minimum number of Monte Carlo simulations to run.
    montecarlo_max : int
        Maximum number of Monte Carlo simulations to run.
    walkforward_window_days : List[int]
        Sequence of window sizes (in days) for walk‑forward analysis. Each
        element defines the length of a training window before a test window
        is applied.

    Returns
    -------
    Dict[str, Any]
        Dictionary containing the seven configuration fields specified in
        `output_structure`.

    Raises
    ------
    ValueError
        If any date string is not in ISO format or if `in_sample_end`
        precedes `in_sample_start`.
    ValueError
        If `montecarlo_min` is greater than `montecarlo_max` or if any
        window size in `walkforward_window_days` is non‑positive.

    Examples
    --------
    >>> config = set_backtest_parameters(
    ...     in_sample_start='2020-01-01',
    ...     in_sample_end='2021-12-31',
    ...     out_sample_start='2022-01-01',
    ...     out_sample_end='2022-12-31',
    ...     montecarlo_min=1000,
    ...     montecarlo_max=5000,
    ...     walkforward_window_days=[90, 180, 360])
    {'in_sample_start': '2020-01-01', 'in_sample_end': '2021-12-31',
    'out_sample_start': '2022-01-01', 'out_sample_end': '2022-12-31',
    'montecarlo_min': 1000, 'montecarlo_max': 5000, 'walkforward_window_days':
    [90, 180, 360]}

    >>> # Invalid example: in_sample_end before start
    >>> set_backtest_parameters(
    ...     in_sample_start='2021-01-01',
    ...     in_sample_end='2020-12-31',
    ...     out_sample_start='2021-01-01',
    ...     out_sample_end='2021-12-31',
    ...     montecarlo_min=500,
    ...     montecarlo_max=2000,
    ...     walkforward_window_days=[30, 60])
    ValueError: in_sample_end must be after in_sample_start

    """
    return SetBacktestParametersOutput(
        in_sample_start="",
        in_sample_end="",
        out_sample_start="",
        out_sample_end="",
        montecarlo_min=0,
        montecarlo_max=0,
        walkforward_window_days=[],
    )