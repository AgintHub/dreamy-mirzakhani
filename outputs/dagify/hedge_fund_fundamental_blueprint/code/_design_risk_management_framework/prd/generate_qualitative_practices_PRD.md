# generate_qualitative_practices PRD

## Description
Generate a list of qualitative risk practices based on the risk profile, asset class count, and metric names.


## Conceptual Info

The generate_qualitative_practices shim function generates a list of qualitative risk practices based on the risk profile, asset class count, and metric names. This function is used to support the design of a risk management framework.

## Docstring

### Summary
Generate a list of qualitative risk practices based on the risk profile, asset class count, and metric names.

### Parameters

- **risk_profile** (str): The risk profile of the portfolio, which can be 'low', 'medium', or 'high'.
- **asset_class_count** (str): The number of distinct asset classes represented in the portfolio.
- **metric_names** (str): The names of the performance and risk metrics, such as 'Gross Return', 'Volatility', 'Sharpe Ratio', etc.

### Returns

List[str]: A list of qualitative risk practices, such as 'Regular portfolio rebalancing', 'Stress testing', etc.

### Raises

- ValueError: When the risk profile is not one of 'low', 'medium', or 'high'.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> generate_qualitative_practices(risk_profile='medium', asset_class_count='5', metric_names='Gross Return, Volatility')
['Regular portfolio rebalancing', 'Stress testing']
```

```python
>>> generate_qualitative_practices(risk_profile='high', asset_class_count='10', metric_names='Gross Return, Volatility, Sharpe Ratio')
['Daily portfolio monitoring', 'Regular portfolio rebalancing', 'Stress testing']
```
