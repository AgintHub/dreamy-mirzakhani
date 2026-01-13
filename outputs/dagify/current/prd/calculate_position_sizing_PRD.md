# calculate_position_sizing PRD

## Description
Determine capital allocation logic


## Conceptual Info

This node determines the capital allocation logic for a quant strategy by designing a position sizing algorithm with three rules: risk per trade, volatility scaling, and maximum position size. It also references the account equity in its calculations.

## Docstring

### Summary
This function calculates the position sizing parameters based on the provided risk per trade, volatility scaling multiple, and maximum position size, while considering the account equity.

### Parameters

- **cagr_target** (float): Target compound annual growth rate
- **annual_volatility_constraint** (float): Maximum acceptable annual volatility
- **drawdown_limit** (float): Maximum allowable drawdown
- **sharpe_ratio_goal** (float): Target Sharpe ratio

### Returns

dict: A dictionary containing the calculated position sizing parameters: risk per trade, volatility scaling multiple, maximum position size, account equity reference, and position sizing algorithm description.

### Raises

- ValueError: If any of the input parameters are invalid or inconsistent.

### Examples

```python
>>> calculate_position_sizing(cagr_target=0.15, annual_volatility_constraint=0.20, drawdown_limit=0.25, sharpe_ratio_goal=1.5)
{'risk_per_trade': 0.02, 'volatility_scaling_multiple': 1.5, 'maximum_position_size': 10000.0, 'account_equity_reference': 100000.0, 'position_sizing_algorithm': 'Risk-based position sizing'}
```
