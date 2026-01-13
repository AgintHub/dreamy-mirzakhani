# set_performance_benchmarks PRD

## Description
Define quantifiable success metrics


## Conceptual Info

The node translates a textual specification of performance goals into a structured dictionary of numerical benchmarks. These benchmarks serve as inputs for downstream risk, sizing, and validation modules.

## Docstring

### Summary
Parse performance benchmark parameters from user input and return a dictionary of numerical metrics.

### Parameters

- **input_text** (str): Raw prompt response containing numeric values for CAGR, volatility, drawdown, and Sharpe ratio. Example: "0.12, 0.18, 0.25, 1.5".

### Returns

Dict[str, float]: Dictionary with keys 'cagr_target', 'annual_volatility_constraint', 'drawdown_limit', and 'sharpe_ratio_goal', each mapped to a float value.

### Raises

- ValueError: If the input cannot be parsed into exactly four numeric values or if any value is out of a reasonable range (e.g., negative CAGR).
- TypeError: If the input is not a string.

### Examples

```python
>>> benchmarks = set_performance_benchmarks('0.15, 0.20, 0.25, 1.8')
{'cagr_target': 0.15, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}
```

```python
>>> benchmarks = set_performance_benchmarks('12%, 20%, 25%, 1.8')
{'cagr_target': 0.12, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.8}
```
