# generate_target_rationales PRD

## Description
Generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.


## Conceptual Info

The generate_target_rationales shim function generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.

## Docstring

### Summary
Generates brief rationales for each target, explaining how it aligns with strategy and risk appetite.

### Parameters

- **metric_names** (str): Names of the performance and risk metrics (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).
- **target_values** (str): Numerical target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).
- **strategy_rationale** (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- **risk_profile** (str): A concise description of the expected risk profile associated with the chosen strategy.

### Returns

LIST_STR: List of brief rationales for each target

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> generate_target_rationales(metric_names='Gross Return, Volatility', target_values='0.15, 0.10', strategy_rationale='This is a strategy rationale.', risk_profile='This is a risk profile.')
['Rationale for Gross Return: ...', 'Rationale for Volatility: ...']
```
