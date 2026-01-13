# calculate_minimum_investment PRD

## Description
Calculates the minimum investment required based on the strategy type and investor base.


## Conceptual Info

The calculate_minimum_investment shim function determines the minimum investment required for a specific investment strategy and investor base.

## Docstring

### Summary
Calculates the minimum investment required based on the strategy type and investor base.

### Parameters

- **strategy_type** (str): The type of investment strategy.
- **investor_base** (str): The type of investor.

### Returns

int: The minimum investment required in USD.

### Raises

- ValueError: When the calculated minimum investment is not a positive integer.
- TypeError: When the input strategy type or investor base is not a string.

### Examples

```python
>>> calculate_minimum_investment(strategy_type='conservative', investor_base='individual')
>>> 100000
100000
```

```python
>>> calculate_minimum_investment(strategy_type='aggressive', investor_base='institutional')
>>> 500000
500000
```
