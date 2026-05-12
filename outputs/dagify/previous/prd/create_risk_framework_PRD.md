# create_risk_framework PRD

## Description
Define capital protection rules


## Conceptual Info

Creates a comprehensive risk framework that protects capital by defining how large each position can be, the exposure limits per instrument, the drawdown threshold that will trigger a trading halt, the daily profit/loss ceiling, and a final rule such as volatility‑based sizing or a stop‑loss mechanism. The framework adapts to the chosen strategy type and the optimized parameter set to ensure the strategy operates within acceptable risk limits.

## Docstring

### Summary
Creates a risk framework specifying position sizing, exposure limits, drawdown halts, daily P&L thresholds, and an additional control rule based on the chosen strategy type and optimized parameters.

### Parameters

- **strategy_type** (str): Primary strategy category (e.g., 'market neutral', 'trend following', etc.).
- **optimized_parameters** (List[float]): List of optimized values for each core strategy parameter returned by the genetic algorithm.
- **parameter_names** (List[str]): Names of the core strategy parameters corresponding to the optimized_parameters list.

### Returns

dict: Dictionary containing the risk framework fields: position_sizing_rule, max_exposure_per_instrument, drawdown_threshold, daily_pnl_limit, and additional_control_rule.

### Raises

- ValueError: Raised if strategy_type is not one of the supported categories.
- ValueError: Raised if lengths of optimized_parameters and parameter_names do not match.

### Examples

```python
>>> framework = create_risk_framework(strategy_type='market neutral', optimized_parameters=[0.3, 0.2, 0.5], parameter_names=['beta', 'volatility', 'alpha'])
>>> print(framework)
{'position_sizing_rule': 'Equal weight long and short with 1% equity per trade', 'max_exposure_per_instrument': 0.02, 'drawdown_threshold': 0.15, 'daily_pnl_limit': 5000.0, 'additional_control_rule': 'Volatility-based sizing: size ∝ 1/(σ * √lookback)'}
```

```python
>>> framework = create_risk_framework(strategy_type='trend following', optimized_parameters=[0.25, 0.35, 0.4], parameter_names=['alpha', 'beta', 'gamma'])
>>> print(framework)
{'position_sizing_rule': 'Kelly criterion based on win/loss ratio', 'max_exposure_per_instrument': 0.05, 'drawdown_threshold': 0.20, 'daily_pnl_limit': 10000.0, 'additional_control_rule': 'Trailing stop of 1.5× ATR'}
```
