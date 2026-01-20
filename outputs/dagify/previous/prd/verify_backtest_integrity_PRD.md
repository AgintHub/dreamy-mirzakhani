# verify_backtest_integrity PRD

## Description
Test results robustness


## Conceptual Info

The verify_backtest_integrity node performs a rigorous integrity check on a quantitative strategy by running an out‑of‑sample backtest on the latest market data, comparing the resulting performance metrics to those from the training period, evaluating the effect of ±20% parameter perturbations to quantify sensitivity, and determining whether the strategy passes predefined robustness thresholds.

## Docstring

### Summary
Run out‑of‑sample backtesting on 2023‑2024 data, compare metrics with training period, compute parameter sensitivity, and return a comprehensive integrity report.

### Parameters

- **training_backtest** (dict): Dictionary containing the outputs from execute_backtesting (backtest_dates, strategy_positions, daily_returns, etc.) representing the training period results.
- **risk_framework** (dict): Dictionary containing the outputs from create_risk_framework (position_sizing_rule, max_exposure_per_instrument, etc.) to ensure risk rules are enforced during the out‑of‑sample run.

### Returns

dict: A dictionary matching the node's output structure, containing the random seed, performance metrics for training and out‑of‑sample periods, differences, parameter sensitivity index, trade counts, and the integrity flag.

### Raises

- ValueError: If any required key is missing from the training_backtest or risk_framework inputs.
- RuntimeError: If the out‑of‑sample backtest fails to complete due to data or execution errors.

### Examples

```python
>>> # Example 1: Simple deterministic training data and risk framework
>>> training_backtest = {
...     'number_of_trades': 100,
...     'cumulative_returns': [0.1, 0.2, 0.15, 0.25],
...     'max_drawdown': 0.05,
...     'daily_returns': [0.01, 0.02, -0.015, 0.025],
...     'training_cagr': 0.12,
...     'training_sharpe': 1.5,
...     'training_win_rate': 0.55
>>> }
>>> risk_framework = {
...     'max_exposure_per_instrument': 0.02,
...     'drawdown_threshold': 0.1,
...     'daily_pnl_limit': 1000
>>> }
>>> result = verify_backtest_integrity(training_backtest, risk_framework)
>>> # Expected output (illustrative):
>>> print(result['backtest_integrity_passed'])
>>> True
True
```

```python
>>> # Example 2: Failure case when training data missing a key
>>> bad_training_backtest = { 'number_of_trades': 50 }
>>> risk_framework = { 'max_exposure_per_instrument': 0.02 }
>>> try:
...     verify_backtest_integrity(bad_training_backtest, risk_framework)
>>> except ValueError as e:
...     print(str(e))
>>> # Expected output:
>>> KeyError: 'training_cagr'
KeyError: 'training_cagr'
```
