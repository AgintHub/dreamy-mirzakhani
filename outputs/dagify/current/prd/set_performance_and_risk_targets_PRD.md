# set_performance_and_risk_targets PRD

## Description
Quantify financial and risk metrics for the hedge fund based on the selected investment strategy.


## Conceptual Info

This node translates the chosen investment strategy into concrete performance and risk benchmarks that guide the fund’s fee structure, risk management, and investor communications.

## Docstring

### Summary
Generate quantitative performance and risk targets for a hedge fund based on its investment strategy.

### Parameters

- **chosen_strategy** (str): The hedge fund strategy selected in the `choose_investment_strategy` node.

### Returns

dict: A dictionary containing four float fields: `annual_gross_return_target`, `volatility_limit_pct`, `sharpe_ratio_goal`, and `max_drawdown_pct`.

### Raises

- ValueError: If `chosen_strategy` is not one of the supported strategy categories.

### Examples

```python
>>> targets = set_performance_and_risk_targets('long/short equity')
>>> print(targets['annual_gross_return_target'])
0.12
```

```python
>>> targets = set_performance_and_risk_targets('global macro')
>>> print(targets['volatility_limit_pct'])
20.0
```
