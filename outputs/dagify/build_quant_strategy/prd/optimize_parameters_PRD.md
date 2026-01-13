# optimize_parameters PRD

## Description
Refine strategy inputs through testing


## Conceptual Info

The optimize_parameters node conducts a Bayesian optimization over a 5‑dimensional space of entry and exit rule parameters. It leverages back‑test results from the analyze_backtest_results node to guide the search and respects risk controls defined elsewhere. The output lists the three best parameter sets along with their Sharpe ratio, maximum drawdown, and total return, enabling downstream nodes to pick a robust configuration.

## Docstring

### Summary
Execute Bayesian optimization over 5‑dimensional entry/exit rule parameters and return the top 3 configurations with performance metrics.

### Parameters

- **analysis_results** (Dict[str, Any]): Dictionary containing back‑test performance metrics from analyze_backtest_results, typically including 'sharpe_ratio', 'max_drawdown', and 'total_return'.
- **risk_limits** (Dict[str, float]): Risk control thresholds such as maximum allowed drawdown and volatility constraints. Keys correspond to metric names used in the optimization objective.
- **parameter_space** (Dict[str, Tuple[float, float]]): Search domain for each of the five parameters. Each key maps to a tuple (min, max) defining the continuous bounds.
- **n_iter** (int): Number of Bayesian optimization iterations to perform.

### Returns

Tuple[List[str], List[float], List[float], List[float]]: A tuple containing (top3_parameters, top3_sharpe, top3_drawdown, top3_return). Each list has length three.

### Raises

- ValueError: If any required key is missing from analysis_results or parameter_space.
- RuntimeError: If the Bayesian optimizer fails to converge or encounters numerical instability.

### Examples

```python
>>> analysis_results = {
...     'sharpe_ratio': 1.2,
...     'max_drawdown': 0.15,
...     'total_return': 0.35
>>> }
>>> risk_limits = {'max_drawdown': 0.2, 'volatility': 0.25}
>>> parameter_space = {
...     'entry_threshold': (0.1, 0.5),
...     'exit_threshold': (0.05, 0.3),
...     'stop_loss': (0.01, 0.05),
...     'take_profit': (0.02, 0.1),
...     'lookback': (10, 60)
>>> }
>>> top3_params, top3_sharpe, top3_dd, top3_ret = optimize_parameters(
...     analysis_results, risk_limits, parameter_space, n_iter=50)
>>> print(top3_params)
>>> print(top3_sharpe)
['entry_threshold=0.34, exit_threshold=0.18, stop_loss=0.025, take_profit=0.06, lookback=30',
 'entry_threshold=0.31, exit_threshold=0.20, stop_loss=0.030, take_profit=0.07, lookback=45',
 'entry_threshold=0.36, exit_threshold=0.16, stop_loss=0.020, take_profit=0.05, lookback=25']
[1.45, 1.42, 1.38]
```
