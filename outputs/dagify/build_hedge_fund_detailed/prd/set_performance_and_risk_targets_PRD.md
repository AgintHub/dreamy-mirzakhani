# set_performance_and_risk_targets PRD

## Description
Quantify financial and risk goals


## Conceptual Info

Sets quantitative performance and risk benchmarks that guide strategy design, risk controls, and fee structuring.

## Docstring

### Summary
Generate annual financial and risk targets for a hedge fund based on the chosen investment strategy.

### Parameters

- **strategy_category** (str): Primary hedge fund strategy category selected by the `choose_investment_strategy` node.
- **strategy_rationale** (str): One‑sentence justification for the chosen strategy, provided by the parent node.

### Returns

dict: Dictionary containing the four numeric target fields: `gross_return`, `volatility`, `sharpe_ratio`, and `max_drawdown`.

### Raises

- ValueError: If any input is missing or empty.
- TypeError: If inputs are not of type `str`.

### Examples

```python
>>> targets = set_performance_and_risk_targets('Long/Short Equity', 'A blend of alpha generation and risk mitigation through directional bets.')
{'gross_return': 0.18, 'volatility': 0.22, 'sharpe_ratio': 1.64, 'max_drawdown': 0.28}
```

```python
>>> targets = set_performance_and_risk_targets('Global Macro', 'Leveraging macroeconomic trends across multiple markets.')
{'gross_return': 0.15, 'volatility': 0.30, 'sharpe_ratio': 1.25, 'max_drawdown': 0.35}
```
