# set_performance_and_risk_targets PRD

## Description
Establish quantitative performance metrics for the hedge fund.


## Conceptual Info

This node translates the chosen investment strategy into concrete, quantitative performance and risk objectives that guide portfolio construction and risk management.

## Docstring

### Summary
Compute annual performance and risk targets based on the selected investment strategy.

### Parameters

- **strategy_category** (str): Primary investment strategy category selected by the parent node (e.g., 'Long/Short Equity', 'Event-Driven', 'Global Macro').
- **strategy_rationale** (str): Textual justification for the strategy, used to inform target setting.
- **risk_profile** (str): Brief description of the expected risk profile (e.g., 'Moderate volatility, high return potential').

### Returns

dict: A dictionary with three keys: 'metric_names' (List[str]), 'target_values' (List[float]), and 'rationale_texts' (List[str]).

### Raises

- ValueError: Raised if any of the input parameters are empty or not a string.
- KeyError: Raised if the strategy_category is not recognized in the internal mapping of target templates.

### Examples

```python
>>> strategy_category = 'Long/Short Equity'
>>> strategy_rationale = 'Targeting alpha from long positions while hedging with short bets.'
>>> risk_profile = 'Moderate volatility, high return potential'
>>> targets = set_performance_and_risk_targets(strategy_category, strategy_rationale, risk_profile)
>>> print(targets['metric_names'])
>>> print(targets['target_values'])
>>> print(targets['rationale_texts'])
"['Gross Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown']"
"[0.15, 0.10, 1.5, 0.20]"
"['A 15% return aligns with long/short alpha goals.', '10% volatility matches moderate risk appetite.', 'Sharpe of 1.5 indicates efficient risk‑adjusted returns.', '20% drawdown tolerance protects capital during market stress.']
```

```python
>>> strategy_category = 'Event-Driven'
>>> strategy_rationale = 'Profit from merger arbitrage and distressed events.'
>>> risk_profile = 'High volatility, low correlation to markets'
>>> targets = set_performance_and_risk_targets(strategy_category, strategy_rationale, risk_profile)
>>> print(targets['target_values'])
[0.18, 0.15, 1.2, 0.25]
```
