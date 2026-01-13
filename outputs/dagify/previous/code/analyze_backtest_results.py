from pydantic import BaseModel, Field
from typing import List


class ExecuteInSampleBacktestOutput(BaseModel):
    """Pydantic model for execute_in_sample_backtest node outputs."""
    equity_curve_dates: List[str] = (
        Field(..., description="Sequential dates of the equity curve in YYYY-MM-DD format")
    )
    equity_curve_values: List[float] = (
        Field(..., description="Equity value for each date in the equity curve")
    )
    drawdown_series: List[float] = (
        Field(..., description="Cumulative drawdown percentage at each date in the equity curve")
    )
    trade_ids: List[str] = (
        Field(..., description="Unique identifiers for each executed trade")
    )
    trade_pnl: List[float] = (
        Field(..., description="Profit or loss for each trade")
    )
    sharpe_ratio: float = (
        Field(..., description="Annualized Sharpe ratio of the backtest")
    )
    max_drawdown: float = (
        Field(..., description="Maximum drawdown percentage observed during the backtest")
    )
    total_return: float = (
        Field(..., description="Total return percentage over the backtest period")
    )


class SetPerformanceBenchmarksOutput(BaseModel):
    """Pydantic model for set_performance_benchmarks node outputs."""
    cagr_target: float = (
        Field(..., description="Target compound annual growth rate in decimal form (e.g., 0.15 for 15%)")
    )
    annual_volatility_constraint: float = (
        Field(..., description="Maximum acceptable annual volatility in decimal form (e.g., 0.20 for 20%)")
    )
    drawdown_limit: float = (
        Field(..., description="Maximum allowable drawdown expressed as a decimal (e.g., 0.25 for 25%)")
    )
    sharpe_ratio_goal: float = (
        Field(..., description="Target Sharpe ratio to be achieved by the strategy")
    )


class AnalyzeBacktestResultsOutput(BaseModel):
    """Pydantic model for analyze_backtest_results node outputs."""
    performance_driver_1: str = (
        Field(..., description="Name or description of the largest performance driver")
    )
    performance_driver_2: str = (
        Field(..., description="Name or description of the second largest performance driver")
    )
    performance_driver_3: str = (
        Field(..., description="Name or description of the third largest performance driver")
    )
    constraint_violation_1: str = (
        Field(..., description="Description of the first major constraint violation")
    )
    constraint_violation_2: str = (
        Field(..., description="Description of the second major constraint violation")
    )
    constraint_violation_3: str = (
        Field(..., description="Description of the third major constraint violation")
    )
    parameter_adjustment_1: str = (
        Field(..., description="First suggested parameter adjustment")
    )
    parameter_adjustment_2: str = (
        Field(..., description="Second suggested parameter adjustment")
    )
    parameter_adjustment_3: str = (
        Field(..., description="Third suggested parameter adjustment")
    )


def analyze_backtest_results(execute_in_sample_backtest_input: ExecuteInSampleBacktestOutput, set_performance_benchmarks_input: SetPerformanceBenchmarksOutput, **kwargs) -> AnalyzeBacktestResultsOutput:
    """
    Analyze in‑sample backtest results against performance benchmarks and return
    top drivers, constraint violations, and parameter adjustment
    recommendations.

    Parameters
    ----------
    equity_curve_dates : List[str]
        Sequential dates of the equity curve in YYYY‑MM‑DD format.
    equity_curve_values : List[float]
        Equity value for each date in the equity curve.
    drawdown_series : List[float]
        Cumulative drawdown percentage at each date.
    trade_ids : List[str]
        Unique identifiers for each executed trade.
    trade_pnl : List[float]
        Profit or loss for each trade.
    sharpe_ratio : float
        Annualized Sharpe ratio of the backtest.
    max_drawdown : float
        Maximum drawdown percentage observed during the backtest.
    total_return : float
        Total return percentage over the backtest period.
    cagr_target : float
        Target CAGR in decimal form (e.g., 0.15 for 15%).
    annual_volatility_constraint : float
        Maximum acceptable annual volatility in decimal form.
    drawdown_limit : float
        Maximum allowable drawdown expressed as a decimal.
    sharpe_ratio_goal : float
        Target Sharpe ratio to be achieved by the strategy.

    Returns
    -------
    Dict[str, str]
        Dictionary containing the nine output fields specified in the node's
        output structure.

    Raises
    ------
    ValueError
        Raised if any required input list is empty or contains mismatched
        lengths.
    RuntimeError
        Raised if benchmark comparison fails due to inconsistent data types.

    Examples
    --------
    >>> result = analyze_backtest_results(
    ...     equity_curve_dates=['2020-01-01', '2020-01-02', '2020-01-03'],
    ...     equity_curve_values=[100000, 102000, 101500],
    ...     drawdown_series=[0.0, 0.0, -0.0025],
    ...     trade_ids=['T1', 'T2'],
    ...     trade_pnl=[2000, -500],
    ...     sharpe_ratio=1.5,
    ...     max_drawdown=0.025,
    ...     total_return=0.015,
    ...     cagr_target=0.12,
    ...     annual_volatility_constraint=0.18,
    ...     drawdown_limit=0.20,
    ...     sharpe_ratio_goal=1.4)
    >>> print(result['performance_driver_1'])
    "Positive correlation with S&P 500"

    >>> result = analyze_backtest_results(
    ...     equity_curve_dates=['2020-01-01', '2020-01-02'],
    ...     equity_curve_values=[100000, 99000],
    ...     drawdown_series=[0.0, -0.01],
    ...     trade_ids=['T1'],
    ...     trade_pnl=[-1000],
    ...     sharpe_ratio=0.8,
    ...     max_drawdown=0.01,
    ...     total_return=-0.01,
    ...     cagr_target=0.10,
    ...     annual_volatility_constraint=0.15,
    ...     drawdown_limit=0.10,
    ...     sharpe_ratio_goal=1.0)
    >>> print(result['constraint_violation_1'])
    "Sharpe ratio below target"

    """
    return AnalyzeBacktestResultsOutput(
        performance_driver_1="",
        performance_driver_2="",
        performance_driver_3="",
        constraint_violation_1="",
        constraint_violation_2="",
        constraint_violation_3="",
        parameter_adjustment_1="",
        parameter_adjustment_2="",
        parameter_adjustment_3="",
    )