# determine_investor_types PRD

## Description
Determine the typical investor types based on the fund strategy and market analysis.


## Conceptual Info

The determine_investor_types shim function identifies potential investor types based on the provided fund strategy and market analysis.

## Docstring

### Summary
Determine the typical investor types based on the fund strategy and market analysis.

### Parameters

- **fund_strategy** (str): The fund strategy to consider when determining investor types.
- **market_analysis** (str): The market analysis to consider when determining investor types.

### Returns

List[str]: A list of typical investor types.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> determine_investor_types(fund_strategy='conservative', market_analysis='True')
['family offices', 'pensions']
```

```python
>>> determine_investor_types(fund_strategy='aggressive', market_analysis='False')
['hedge funds', 'venture capital']
```
