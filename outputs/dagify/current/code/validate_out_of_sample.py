from pydantic import BaseModel, Field
from typing import List


class OptimizeParametersOutput(BaseModel):
    """Pydantic model for optimize_parameters node outputs."""
    top3_parameters: List[str] = (
        Field(..., description="String representations of the top 3 parameter combinations, formatted as key=value pairs separated by commas")
    )
    top3_sharpe: List[float] = (
        Field(..., description="Sharpe ratio values corresponding to each of the top 3 parameter sets")
    )
    top3_drawdown: List[float] = (
        Field(..., description="Maximum drawdown percentages corresponding to each of the top 3 parameter sets")
    )
    top3_return: List[float] = (
        Field(..., description="Total return percentages corresponding to each of the top 3 parameter sets")
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


class ValidateOutOfSampleOutput(BaseModel):
    """Pydantic model for validate_out_of_sample node outputs."""
    selected_param_set: str = (
        Field(..., description="Identifier of the parameter set used for the out-of-sample test")
    )
    in_sample_sharpe: float = (
        Field(..., description="Sharpe ratio calculated on the in-sample period")
    )
    out_of_sample_sharpe: float = (
        Field(..., description="Sharpe ratio calculated on the out-of-sample period")
    )
    in_sample_max_drawdown: float = (
        Field(..., description="Maximum drawdown percentage on the in-sample period")
    )
    out_of_sample_max_drawdown: float = (
        Field(..., description="Maximum drawdown percentage on the out-of-sample period")
    )
    overfitting_tests_passed: bool = (
        Field(..., description="Boolean results for each of the three statistical overfitting tests (true if passed)")
    )
    overfitting_test_names: str = (
        Field(..., description="Names of the statistical tests performed (e.g., t-test, Diebold-Mariano, etc.)")
    )


def validate_out_of_sample(optimize_parameters_input: OptimizeParametersOutput, set_backtest_parameters_input: SetBacktestParametersOutput, **kwargs) -> ValidateOutOfSampleOutput:
    """
    Validate a strategy on out‑of‑sample data and detect over‑fitting.

    Parameters
    ----------
    top3_parameters : list[str]
        List of the top three parameter‑set strings produced by
        ``optimize_parameters``.
    top3_sharpe : list[float]
        Sharpe ratios corresponding to each of the top three parameter sets.
    in_sample_equity : dict
        Dictionary containing in‑sample equity curve data with keys
        ``dates`` and ``values``.
    out_sample_start : str
        ISO format start date of the out‑sample window (YYYY‑MM‑DD).
    out_sample_end : str
        ISO format end date of the out‑sample window (YYYY‑MM‑DD).
    backtest_function : Callable
        Callable that accepts a parameter set string and returns a dict with
        ``sharpe`` and ``max_drawdown`` for a given date range.

    Returns
    -------
    dict
        A dictionary containing the selected parameter set identifier,
        in‑sample and out‑of‑sample Sharpe ratios, max drawdowns, and
        over‑fitting test results.

    Raises
    ------
    ValueError
        If the ``top3_parameters`` list is empty or does not contain the
        selected set.
    RuntimeError
        If the backtest function fails to return a valid performance metric.

    Examples
    --------
    >>> top3_parameters = ['alpha=0.1,beta=0.2,gamma=0.3',
    ...                 'alpha=0.15,beta=0.25,gamma=0.35',
    ...                 'alpha=0.2,beta=0.3,gamma=0.4']
    >>> top3_sharpe = [1.25, 1.10, 0.95]
    >>> in_sample_equity = {
    ...     'dates': ['2020-01-01', '2020-01-02'],
    ...     'values': [100000, 102500]}
    >>> def dummy_backtest(param_set):
    ...     return {'sharpe': 1.05 if 'alpha=0.1' in param_set else 0.9,
    ...             'max_drawdown': 0.12}
    >>> result = validate_out_of_sample(
    ...     top3_parameters=top3_parameters,
    ...     top3_sharpe=top3_sharpe,
    ...     in_sample_equity=in_sample_equity,
    ...     out_sample_start='2020-02-01',
    ...     out_sample_end='2020-04-01',
    ...     backtest_function=dummy_backtest)
    {
      'selected_param_set': 'alpha=0.1,beta=0.2,gamma=0.3',
      'in_sample_sharpe': 1.25,
      'out_of_sample_sharpe': 1.05,
      'in_sample_max_drawdown': 0.12,
      'out_of_sample_max_drawdown': 0.12,
      'overfitting_tests_passed': [True, False, True],
      'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
    }

    >>> # Using the second best parameter set
result2 = validate_out_of_sample(
    ...     top3_parameters=top3_parameters,
    ...     top3_sharpe=top3_sharpe,
    ...     in_sample_equity=in_sample_equity,
    ...     out_sample_start='2020-02-01',
    ...     out_sample_end='2020-04-01',
    ...     backtest_function=dummy_backtest)
    {
      'selected_param_set': 'alpha=0.15,beta=0.25,gamma=0.35',
      'in_sample_sharpe': 1.10,
      'out_of_sample_sharpe': 0.90,
      'in_sample_max_drawdown': 0.12,
      'out_of_sample_max_drawdown': 0.12,
      'overfitting_tests_passed': [False, False, True],
      'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
    }

    """
    return ValidateOutOfSampleOutput(
        selected_param_set="",
        in_sample_sharpe=0.0,
        out_of_sample_sharpe=0.0,
        in_sample_max_drawdown=0.0,
        out_of_sample_max_drawdown=0.0,
        overfitting_tests_passed=False,
        overfitting_test_names="",
    )