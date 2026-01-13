from pydantic import BaseModel, Field
from typing import List


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


class CalculatePositionSizingOutput(BaseModel):
    """Pydantic model for calculate_position_sizing node outputs."""
    risk_per_trade: float = Field(..., description="Risk percentage per trade")
    volatility_scaling_multiple: float = (
        Field(..., description="Volatility scaling multiple")
    )
    maximum_position_size: float = (
        Field(..., description="Maximum position size")
    )
    account_equity_reference: float = (
        Field(..., description="Account equity reference value")
    )
    position_sizing_algorithm: str = (
        Field(..., description="Position sizing algorithm description")
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


class BuildRiskRulesOutput(BaseModel):
    """Pydantic model for build_risk_rules node outputs."""
    portfolio_volatility_limit: float = (
        Field(..., description="The maximum allowed portfolio volatility")
    )
    sector_concentration_limit: float = (
        Field(..., description="The maximum allowed sector concentration")
    )
    drawdown_trigger_limit: float = (
        Field(..., description="The maximum allowed drawdown trigger")
    )
    position_correlation_limit: float = (
        Field(..., description="The maximum allowed position correlation")
    )
    risk_limit_rules: str = (
        Field(..., description="List of risk limit rules with their thresholds")
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


def execute_in_sample_backtest(develop_entry_rules_input: DevelopEntryRulesOutput, develop_exit_rules_input: DevelopExitRulesOutput, calculate_position_sizing_input: CalculatePositionSizingOutput, implement_slippage_model_input: ImplementSlippageModelOutput, build_risk_rules_input: BuildRiskRulesOutput, set_backtest_parameters_input: SetBacktestParametersOutput, **kwargs) -> ExecuteInSampleBacktestOutput:
    """
    Run an in‑sample backtest of the strategy and return performance metrics.

    Parameters
    ----------
    entry_conditions : List[str]
        Pseudo‑code expressions defining when to open positions.
    exit_conditions : List[str]
        Pseudo‑code expressions defining when to close positions.
    parameter_values : List[float]
        Numerical values associated with the entry/exit conditions.
    position_sizing_algo : str
        Description or identifier of the position sizing algorithm.
    slippage_params : dict
        Dictionary with keys 'bid_ask_spread_percent',
        'price_impact_coefficient', 'time_slippage_decay_factor'.
    risk_limits : dict
        Risk limits including portfolio volatility, sector concentration,
        drawdown trigger, and position correlation thresholds.
    backtest_params : dict
        Backtest configuration containing in‑sample start/end dates,
        walk‑forward windows, etc.
    historical_data : numpy.ndarray
        4‑D array of pre‑processed market data (assets × features × time ×
        channels).

    Returns
    -------
    dict
        Dictionary containing equity curve, drawdown series, trade details,
        and performance statistics.

    Raises
    ------
    ValueError
        If any required input (e.g., entry_conditions) is missing or empty.
    RuntimeError
        If the backtest simulation fails due to insufficient data or
        internal errors.

    Examples
    --------
    >>> # Example 1: Simple moving‑average crossover strategy
    >>> result = execute_in_sample_backtest(
    ...     entry_conditions=["price > sma_50"],
    ...     exit_conditions=["price < sma_20"],
    ...     parameter_values=[50, 20],
    ...     position_sizing_algo="risk_per_trade_1percent",
    ...     slippage_params={
    ...         "bid_ask_spread_percent": 0.1,
    ...         "price_impact_coefficient": 0.0005,
    ...         "time_slippage_decay_factor": 0.99
    ...     },
    ...     risk_limits={
    ...         "portfolio_volatility_limit": 0.15,
    ...         "sector_concentration_limit": 0.4,
    ...         "drawdown_trigger_limit": 0.2,
    ...         "position_correlation_limit": 0.7
    ...     },
    ...     backtest_params={
    ...         "in_sample_start": "2020-01-01",
    ...         "in_sample_end": "2022-12-31"
    ...     },
    ...     historical_data=market_array)
    >>> # Expected output (excerpt)
    >>> result["sharpe_ratio"]  # -> 1.25
    >>> result["max_drawdown"]   # -> 0.18
    >>> len(result["trade_ids"]) # -> 350
    "... (dictionary containing the full backtest report) ..."

    >>> # Example 2: Strategy with stop‑loss and profit‑target
    >>> result = execute_in_sample_backtest(
    ...     entry_conditions=["rsi < 30"],
    ...     exit_conditions=["rsi > 70", "price < stop_loss", "price >
    profit_target"],
    ...     parameter_values=[30, 70, 0.02, 0.05],
    ...     position_sizing_algo="volatility_scaling",
    ...     slippage_params={
    ...         "bid_ask_spread_percent": 0.2,
    ...         "price_impact_coefficient": 0.001,
    ...         "time_slippage_decay_factor": 0.95
    ...     },
    ...     risk_limits={
    ...         "portfolio_volatility_limit": 0.12,
    ...         "sector_concentration_limit": 0.3,
    ...         "drawdown_trigger_limit": 0.15,
    ...         "position_correlation_limit": 0.6
    ...     },
    ...     backtest_params={
    ...         "in_sample_start": "2018-01-01",
    ...         "in_sample_end": "2020-12-31"
    ...     },
    ...     historical_data=market_array)
    >>> # Expected output (excerpt)
    >>> result["total_return"]   # -> 0.48
    >>> result["drawdown_series"][:5] # -> [0.0, -0.02, -0.015, -0.025, -0.02]
    "... (dictionary containing the full backtest report) ..."

    """
    return ExecuteInSampleBacktestOutput(
        equity_curve_dates=[],
        equity_curve_values=[],
        drawdown_series=[],
        trade_ids=[],
        trade_pnl=[],
        sharpe_ratio=0.0,
        max_drawdown=0.0,
        total_return=0.0,
    )