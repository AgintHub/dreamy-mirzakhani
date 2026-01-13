# analyze_risk_profile PRD

## Description
Analyzes the risk profile based on the provided performance and risk metrics and their target values.


## Conceptual Info

The analyze_risk_profile shim function is responsible for analyzing the risk profile of a given set of performance and risk metrics and their target values. This function will provide a risk profile analysis output in the form of a dictionary.

## Docstring

### Summary
Analyzes the risk profile based on the provided performance and risk metrics and their target values.

### Parameters

- **metric_names** (str): A string of comma-separated performance and risk metric names (e.g., Gross Return, Volatility, Sharpe Ratio, Max Drawdown).
- **target_values** (str): A string of comma-separated target values corresponding to each metric (e.g., 0.15 for 15% gross return, 0.10 for 10% volatility).

### Returns

dict: A dictionary representing the risk profile analysis output.

### Raises

- ValueError: When the input metric names and target values do not match in length.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> analyze_risk_profile(metric_names='Gross Return,Volatility,Sharpe Ratio', target_values='0.15,0.10,1.2')
{'risk_profile': 'high', 'confidence_interval': [0.05, 0.15]}
```

```python
>>> analyze_risk_profile(metric_names='Max Drawdown,Sortino Ratio', target_values='0.20,1.5')
{'risk_profile': 'medium', 'recommendations': ['diversify portfolio']}
```
