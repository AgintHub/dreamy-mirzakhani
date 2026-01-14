# calculate_minimum_investment PRD

## Description
Calculates the minimum investment required based on the fund strategy and target investors.


## Conceptual Info

The calculate_minimum_investment shim function determines the minimum investment required for a fund based on its strategy and target investors.

## Docstring

### Summary
Calculates the minimum investment required in USD based on the fund strategy and target investors.

### Parameters

- **fund_strategy** (str): The fund strategy, e.g., objectives, competitive advantages, target return profiles, and long-term vision.
- **target_investors** (str): The target investors, e.g., family offices, pensions.

### Returns

int: The minimum investment required in USD.

### Raises

- ValueError: When the minimum investment is not a positive integer.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> calculate_minimum_investment(fund_strategy='conservative', target_investors='family offices')
>>> 100000
100000
```

```python
>>> calculate_minimum_investment(fund_strategy='aggressive', target_investors='pensions')
>>> 500000
500000
```
