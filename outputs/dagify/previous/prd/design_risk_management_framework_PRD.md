# design_risk_management_framework PRD

## Description
Outline core risk controls


## Conceptual Info

Generates a structured list of primary risk controls that tie directly to the fund’s quantitative performance and risk targets. Each control is mapped to a target metric and a numeric limit, forming the backbone of the fund’s risk‑management framework.

## Docstring

### Summary
Creates core risk controls aligned with annual performance and risk targets.

### Parameters

- **gross_return** (float): Target annual gross return percentage (e.g., 0.15 for 15%).
- **volatility** (float): Target annual volatility percentage (e.g., 0.25 for 25%).
- **sharpe_ratio** (float): Target annual Sharpe ratio (e.g., 1.5).
- **max_drawdown** (float): Target maximum annual drawdown percentage (e.g., 0.30 for 30%).

### Returns

dict: A dictionary containing three keys:
- 'control_name': List[str] of risk control names.
- 'target_metric': List[str] of metrics each control limits.
- 'limit_value': List[float] of numeric thresholds.

### Raises

- ValueError: If any target parameter is missing, None, or not a numeric type.

### Examples

```python
>>> controls = design_risk_management_framework(0.12, 0.20, 1.4, 0.25)
>>> print(controls['control_name'])
['Position Limit', 'VaR Limit', 'Stop‑Loss Rule']
```

```python
>>> controls = design_risk_management_framework(0.15, 0.22, 1.6, 0.28)
>>> print(controls['limit_value'])
[1.0, 0.02, 0.05]
```
