# design_risk_management_framework PRD

## Description
Create risk mitigation mechanism


## Conceptual Info

This node specifies the quantitative risk controls that will govern the hedge fund’s trading activities.  It takes the investment strategy and the performance‑and‑risk targets defined upstream to produce a concise list of control names and their numeric thresholds, enabling downstream nodes to incorporate these limits into the pitch deck, compliance program, and operations workflow.

## Docstring

### Summary
Generate a list of quantitative risk controls and their numeric limits based on the chosen investment strategy and performance targets.

### Parameters

- **chosen_strategy** (str): The hedge fund strategy selected in the `choose_investment_strategy` node (e.g., "long/short equity", "market neutral", etc.).
- **annual_gross_return_target** (float): Target annual gross return expressed as a decimal (e.g., 0.12 for 12%).
- **volatility_limit_pct** (float): Maximum acceptable annual volatility expressed as a percentage (e.g., 15 for 15%).
- **sharpe_ratio_goal** (float): Desired Sharpe ratio target for the fund.
- **max_drawdown_pct** (float): Maximum acceptable peak‑to‑trough drawdown expressed as a percentage (e.g., 20 for 20%).

### Returns

Tuple[List[str], List[float]]: Two lists: control_name and control_limit, each element corresponding by index.

### Raises

- ValueError: If any numeric target is negative or out of a realistic range (e.g., VaR > 100%).
- KeyError: If a required input key is missing from the arguments.

### Examples

```python
>>> control_name, control_limit = design_risk_management_framework(
...     chosen_strategy="long/short equity",
...     annual_gross_return_target=0.15,
...     volatility_limit_pct=12.0,
...     sharpe_ratio_goal=1.5,
...     max_drawdown_pct=18.0)
>>> ]
"control_name": ["VaR limit", "Position size cap", "Liquidity threshold", "Stop‑loss level"],\n"control_limit": [2.5, 10.0, 5.0, 3.0]
```

```python
>>> control_name, control_limit = design_risk_management_framework(
...     chosen_strategy="market neutral",
...     annual_gross_return_target=0.10,
...     volatility_limit_pct=8.0,
...     sharpe_ratio_goal=1.2,
...     max_drawdown_pct=12.0)
>>> ]
"control_name": ["VaR limit", "Position size cap", "Liquidity threshold"],\n"control_limit": [1.8, 8.0, 4.0]
```
