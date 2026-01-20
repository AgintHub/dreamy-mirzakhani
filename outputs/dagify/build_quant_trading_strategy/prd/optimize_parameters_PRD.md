# optimize_parameters PRD

## Description
Refine model inputs


## Conceptual Info

This node applies a genetic algorithm to search the strategy parameter space defined by define_strategy_parameters, evaluating each candidate using performance metrics from calculate_performance_metrics to maximize the Sharpe ratio.

## Docstring

### Summary
Optimizes strategy parameters via a genetic algorithm to maximize Sharpe ratio, using performance metrics as evaluation and respecting specified convergence and population settings.

### Parameters

- **parameter_names** (List[str]): Names of the strategy's core parameters to be optimized.
- **parameter_min_values** (List[float]): Minimum bounds for each parameter in the search space.
- **parameter_max_values** (List[float]): Maximum bounds for each parameter in the search space.
- **population_size** (int): Number of candidate solutions in each generation of the genetic algorithm.
- **convergence_threshold** (float): Relative improvement threshold on the Sharpe ratio between successive generations to declare convergence.
- **max_generations** (int): Maximum number of generations to run if convergence is not reached earlier.

### Returns

Dict[str, Any]: A dictionary containing the optimized parameter values, achieved Sharpe ratio, convergence status, generations run, population size used, and parameter names.

### Raises

- ValueError: If the lengths of parameter lists do not match or if any min bound is greater than its corresponding max bound.
- RuntimeError: If the genetic algorithm fails to converge within the specified max_generations.
- Exception: If evaluation of a candidate parameter set fails due to invalid configuration or runtime errors.

### Examples

```python
>>> result = optimize_parameters(
...     parameter_names=['macd_fast', 'macd_slow', 'vol_decay', 'factor_weight', 'stop_loss'],
...     parameter_min_values=[5, 12, 0.01, 0.1, 0.01],
...     parameter_max_values=[20, 50, 0.5, 1.0, 0.1],
...     population_size=50,
...     convergence_threshold=0.01,
...     max_generations=100
>>> )
{'optimized_parameter_values': [12.3, 28.5, 0.123, 0.78, 0.045], 'sharpe_ratio_achieved': 2.45, 'convergence_reached': True, 'generations_run': 35, 'population_size': 50, 'parameter_names': ['macd_fast', 'macd_slow', 'vol_decay', 'factor_weight', 'stop_loss']}
```

```python
>>> result_small = optimize_parameters(
...     parameter_names=['param1', 'param2', 'param3'],
...     parameter_min_values=[1, 0.5, 0.1],
...     parameter_max_values=[10, 5, 1],
...     population_size=20,
...     convergence_threshold=0.02,
...     max_generations=50
>>> )
{'optimized_parameter_values': [5.2, 2.7, 0.45], 'sharpe_ratio_achieved': 1.78, 'convergence_reached': False, 'generations_run': 50, 'population_size': 20, 'parameter_names': ['param1', 'param2', 'param3']}
```
