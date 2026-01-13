# execute_in_sample_backtest PRD

## Description
Run strategy against historical data


## Conceptual Info

Executes an in‑sample backtest of a quant strategy by simulating trades on historical data using the previously defined entry/exit rules, position sizing, slippage model, and risk constraints. It produces a daily equity curve, drawdown series, and trade‑level PnL, along with key performance statistics.

## Docstring

### Summary
Run an in‑sample backtest of the strategy and return performance metrics.

### Parameters

- **entry_conditions** (List[str]): Pseudo‑code expressions defining when to open positions.
- **exit_conditions** (List[str]): Pseudo‑code expressions defining when to close positions.
- **parameter_values** (List[float]): Numerical values associated with the entry/exit conditions.
- **position_sizing_algo** (str): Description or identifier of the position sizing algorithm.
- **slippage_params** (dict): Dictionary with keys 'bid_ask_spread_percent', 'price_impact_coefficient', 'time_slippage_decay_factor'.
- **risk_limits** (dict): Risk limits including portfolio volatility, sector concentration, drawdown trigger, and position correlation thresholds.
- **backtest_params** (dict): Backtest configuration containing in‑sample start/end dates, walk‑forward windows, etc.
- **historical_data** (numpy.ndarray): 4‑D array of pre‑processed market data (assets × features × time × channels).

### Returns

dict: Dictionary containing equity curve, drawdown series, trade details, and performance statistics.

### Raises

- ValueError: If any required input (e.g., entry_conditions) is missing or empty.
- RuntimeError: If the backtest simulation fails due to insufficient data or internal errors.

### Examples

```python
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
```

```python
>>> # Example 2: Strategy with stop‑loss and profit‑target
>>> result = execute_in_sample_backtest(
...     entry_conditions=["rsi < 30"],
...     exit_conditions=["rsi > 70", "price < stop_loss", "price > profit_target"],
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
```
