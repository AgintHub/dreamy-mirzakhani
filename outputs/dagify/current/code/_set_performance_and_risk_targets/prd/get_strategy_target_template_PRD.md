# get_strategy_target_template PRD

## Description
This shim function generates a base target template for performance and risk metrics based on the chosen investment strategy category.


## Conceptual Info

The get_strategy_target_template shim is responsible for providing initial target values for key performance and risk metrics based on the selected investment strategy, serving as a foundation for further adjustments and refinements.

## Docstring

### Summary
Generates a base target template for performance and risk metrics based on the chosen investment strategy category, returning a dictionary with metric names as keys and target values as values.

### Parameters

- **strategy_category** (str): The category of the investment strategy (e.g., conservative, moderate, aggressive).

### Returns

dict: A dictionary containing the base target metrics and their values for the specified strategy category.

### Raises

- ValueError: Raised when the strategy category is not recognized or supported.
- TypeError: Raised when the input strategy category is not a string.

### Examples

```python
>>> base_targets = get_strategy_target_template(strategy_category='conservative')
>>> print(base_targets)
{'Gross Return': 0.08, 'Volatility': 0.05, 'Sharpe Ratio': 1.2}
```

```python
>>> base_targets = get_strategy_target_template(strategy_category='aggressive')
>>> print(base_targets)
{'Gross Return': 0.15, 'Volatility': 0.12, 'Sharpe Ratio': 1.5}
```
