# define_strategy_parameters PRD

## Description
Establish model rules in mathematical terms


## Conceptual Info

Defines the quantitative hyper‑parameters that govern signal generation and risk management for a selected strategy type. The node produces a set of parameter names, their mathematical definitions, and feasible search ranges for subsequent optimisation.

## Docstring

### Summary
Generate core strategy parameters from a strategy type. The function receives the chosen strategy category and returns four parallel lists containing parameter names, their mathematical expressions, and min/max bounds for hyper‑parameter tuning.

### Parameters

- **strategy_type** (str): Primary strategy category returned by `choose_strategy_type`. Expected values are 'market neutral', 'statistical arbitrage', 'momentum', 'mean reversion', or 'trend following'.

### Returns

dict: A dictionary with keys 'parameter_names', 'parameter_expressions', 'parameter_min_values', and 'parameter_max_values', each mapping to a list of strings or floats. The lists are aligned by index so that the i‑th element of each list corresponds to the same parameter.

### Raises

- ValueError: If `strategy_type` is not one of the recognised strategy categories.

### Examples

```python
>>> params = define_strategy_parameters('momentum')
>>> print(params)
{'parameter_names': ['fast_period', 'slow_period', 'volatility_window', 'factor_weight', 'signal_threshold'], 'parameter_expressions': ['EMA(price, fast_period)', 'EMA(price, slow_period)', 'sqrt(Var(price, volatility_window))', 'weight * factor', 'threshold'], 'parameter_min_values': [5.0, 20.0, 10.0, 0.1, 0.01], 'parameter_max_values': [20.0, 50.0, 60.0, 1.0, 0.1]}
```

```python
>>> params = define_strategy_parameters('mean reversion')
>>> print(params['parameter_min_values'])
>>> print(params['parameter_max_values'])
[5.0, 10.0, 15.0, 0.2, 0.05]
[30.0, 60.0, 45.0, 1.0, 0.15]
```
