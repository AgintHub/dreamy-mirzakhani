# execute_backtesting PRD

## Description
Apply algorithm to historical data


## Conceptual Info

Executes a walk-forward backtest of a quantitative strategy over the historical period 2018‑2022, incorporating transaction costs and slippage, to produce daily and cumulative performance metrics for later evaluation.

## Docstring

### Summary
Simulate strategy execution over 2018‑2022 using walk‑forward analysis, generating position sizes, applying transaction costs and slippage, and producing daily and cumulative returns along with key performance indicators.

### Parameters

- **price_data** (object): Cleaned historical price series for all instruments (e.g., a DataFrame or nested list).
- **fundamental_data** (object): Cleaned fundamental metrics aligned with price data (e.g., earnings, revenue).
- **signal_algo** (object): Callable or object that implements the signal generation logic produced by `implement_signal_processing`.

### Returns

dict: Dictionary mapping output keys (backtest_dates, strategy_positions, etc.) to their computed values.

### Raises

- ValueError: Raised when required input data is missing or improperly formatted.
- RuntimeError: Raised if the backtesting simulation fails (e.g., due to inconsistent dates or missing market data).

### Examples

```python
>>> price_data = {'prices': [100, 102, 101, 103, 104]}
>>> fundamental_data = {'eps': [3.2, 3.4, 3.5, 3.6, 3.7]}
>>> signal_algo = lambda dates: [1, 0, -1, 1, 0]
>>> results = execute_backtesting(price_data, fundamental_data, signal_algo)
{
  'backtest_dates': ['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-06'],
  'strategy_positions': [0.5, 0.0, -0.5, 0.5, 0.0],
  'daily_returns': [0.01, 0.0, -0.015, 0.02, 0.0],
  'transaction_costs': [0.001, 0.001, 0.001, 0.001, 0.001],
  'slippage_costs': [0.0005, 0.0005, 0.0005, 0.0005, 0.0005],
  'cumulative_returns': [0.009, 0.009, -0.006, 0.014, 0.014],
  'trade_signals': [1, 0, -1, 1, 0],
  'number_of_trades': 4,
  'max_drawdown': 0.02,
  'backtest_success_flag': True
}
```
