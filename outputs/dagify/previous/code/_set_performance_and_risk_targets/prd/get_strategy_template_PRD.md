# get_strategy_template PRD

## Description
Retrieves a strategy template based on the provided strategy category.


## Conceptual Info

The get_strategy_template shim function provides a strategy template based on the input strategy category, which is used to set performance and risk targets.

## Docstring

### Summary
Retrieves a strategy template based on the provided strategy category.

### Parameters

- **strategy_category** (str): The primary investment strategy category.

### Returns

dict: A dictionary containing the strategy template, including metric names and target values.

### Raises

- ValueError: When the input strategy category is invalid or not supported.
- TypeError: When the input strategy category is not a string.

### Examples

```python
>>> get_strategy_template(strategy_category='conservative')
{'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.05, 0.10]}
```

```python
>>> get_strategy_template(strategy_category='aggressive')
{'metric_names': ['Gross Return', 'Volatility'], 'target_values': [0.10, 0.20]}
```
