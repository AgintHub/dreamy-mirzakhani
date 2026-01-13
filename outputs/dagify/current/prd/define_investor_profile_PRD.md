# define_investor_profile PRD

## Description
Characterize target capital sources


## Conceptual Info

Characterize target capital sources by defining ideal investor demographics

## Docstring

### Summary
Define the ideal investor demographic for a hedge fund

### Parameters

- **fund_objectives** (str): Primary business objectives for launching the hedge fund

### Returns

dict: A dictionary containing typical investor types, required minimum investment, liquidity expectations, risk tolerance levels, and geographic focus

### Raises

- ValueError: If required minimum investment is not a positive integer

### Examples

```python
>>> define_investor_profile(fund_objectives='Maximize returns while minimizing risk')
>>> print(output['typical_investor_types'])  # Output: ['family offices', 'pensions']
>>> print(output['required_minimum_investment'])  # Output: 1000000
>>> print(output['liquidity_expectations'])  # Output: 'Quarterly redemptions'
>>> print(output['risk_tolerance_levels'])  # Output: ['aggressive', 'conservative']
>>> print(output['geographic_focus'])  # Output: 'North America'
{'typical_investor_types': ['family offices', 'pensions'], 'required_minimum_investment': 1000000, 'liquidity_expectations': 'Quarterly redemptions', 'risk_tolerance_levels': ['aggressive', 'conservative'], 'geographic_focus': 'North America'}
```
