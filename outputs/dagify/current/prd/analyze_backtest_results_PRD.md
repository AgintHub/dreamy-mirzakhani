# analyze_backtest_results PRD

## Description
Evaluate in‑sample backtest performance against predefined benchmarks, distill key drivers and infractions, and recommend actionable parameter tweaks.


## Conceptual Info

The node aggregates quantitative backtest outcomes and benchmark definitions to surface actionable insights. It transforms raw equity curves, trade‑level PnL, and risk metrics into concise, human‑readable summaries that highlight performance levers and compliance breaches.

## Docstring

### Summary
Analyze in‑sample backtest results against performance benchmarks and return top drivers, constraint violations, and parameter adjustment recommendations.

### Parameters

- **equity_curve_dates** (List[str]): Sequential dates of the equity curve in YYYY‑MM‑DD format.
- **equity_curve_values** (List[float]): Equity value for each date in the equity curve.
- **drawdown_series** (List[float]): Cumulative drawdown percentage at each date.
- **trade_ids** (List[str]): Unique identifiers for each executed trade.
- **trade_pnl** (List[float]): Profit or loss for each trade.
- **sharpe_ratio** (float): Annualized Sharpe ratio of the backtest.
- **max_drawdown** (float): Maximum drawdown percentage observed during the backtest.
- **total_return** (float): Total return percentage over the backtest period.
- **cagr_target** (float): Target CAGR in decimal form (e.g., 0.15 for 15%).
- **annual_volatility_constraint** (float): Maximum acceptable annual volatility in decimal form.
- **drawdown_limit** (float): Maximum allowable drawdown expressed as a decimal.
- **sharpe_ratio_goal** (float): Target Sharpe ratio to be achieved by the strategy.

### Returns

Dict[str, str]: Dictionary containing the nine output fields specified in the node's output structure.

### Raises

- ValueError: Raised if any required input list is empty or contains mismatched lengths.
- RuntimeError: Raised if benchmark comparison fails due to inconsistent data types.

### Examples

```python
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
```

```python
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
```
