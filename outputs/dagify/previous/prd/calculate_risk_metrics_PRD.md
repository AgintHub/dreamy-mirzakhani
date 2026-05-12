# calculate_risk_metrics PRD

## Description
Produce detailed risk metrics.


## Conceptual Info

This node calculates position-level risk metrics from the trade log.

## Docstring

### Summary
Calculate risk metrics from trade log.

### Parameters

- **trade_log** (str): Trade log data.
- **frequency** (int): Frequency of calculations (e.g., daily, weekly, monthly).

### Returns

Dict[str, List[str|float|int]]: Dict of risk metrics with lists of values.

### Raises

- ValueError: Invalid input data format.

### Examples

```python
>>> risk_metrics = calculate_risk_metrics(trade_log="trade_data.csv", frequency=1)
{'var_95': [0.1, 0.2, 0.3], 'exposure_limits': [100, 200, 300], 'liquidity_risk': 0.5}
```
