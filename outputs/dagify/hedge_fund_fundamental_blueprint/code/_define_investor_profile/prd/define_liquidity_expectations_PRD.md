# define_liquidity_expectations PRD

## Description
Defines liquidity expectations based on investor types and fund strategy.


## Conceptual Info

This shim function generates a description of liquidity expectations based on the types of investors and the fund's strategy.

## Docstring

### Summary
Defines liquidity expectations based on investor types and fund strategy.

### Parameters

- **investor_types** (str): A string representing the types of investors (e.g., family offices, pensions).
- **fund_strategy** (str): A string representing the fund's strategy (e.g., growth, income, balanced).

### Returns

str: A description of the liquidity expectations.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> define_liquidity_expectations(investor_types='family offices', fund_strategy='growth')
>>> define_liquidity_expectations(investor_types='pensions', fund_strategy='income')
'Liquidity expectations for growth strategy with family offices', 'Liquidity expectations for income strategy with pensions'
```
