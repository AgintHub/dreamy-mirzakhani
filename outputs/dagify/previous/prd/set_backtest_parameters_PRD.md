# set_backtest_parameters PRD

## Description
Configure strategy evaluation framework


## Conceptual Info

This node establishes the temporal and stochastic bounds for backtesting a quantitative strategy. It defines the in‑sample and out‑of‑sample windows, the range of Monte Carlo simulation counts, and the schedule for walk‑forward validation. The configuration produced here is consumed by downstream nodes that execute the backtests, optimize parameters, and validate out‑of‑sample performance.

## Docstring

### Summary
Configure the backtesting framework for a quantitative strategy.

### Parameters

- **in_sample_start** (str): Start date of the in-sample period in 'YYYY-MM-DD' format.
- **in_sample_end** (str): End date of the in-sample period in 'YYYY-MM-DD' format.
- **out_sample_start** (str): Start date of the out-of-sample period in 'YYYY-MM-DD' format.
- **out_sample_end** (str): End date of the out-of-sample period in 'YYYY-MM-DD' format.
- **montecarlo_min** (int): Minimum number of Monte Carlo simulations to run.
- **montecarlo_max** (int): Maximum number of Monte Carlo simulations to run.
- **walkforward_window_days** (List[int]): Sequence of window sizes (in days) for walk‑forward analysis. Each element defines the length of a training window before a test window is applied.

### Returns

Dict[str, Any]: Dictionary containing the seven configuration fields specified in `output_structure`.

### Raises

- ValueError: If any date string is not in ISO format or if `in_sample_end` precedes `in_sample_start`.
- ValueError: If `montecarlo_min` is greater than `montecarlo_max` or if any window size in `walkforward_window_days` is non‑positive.

### Examples

```python
>>> config = set_backtest_parameters(
...     in_sample_start='2020-01-01',
...     in_sample_end='2021-12-31',
...     out_sample_start='2022-01-01',
...     out_sample_end='2022-12-31',
...     montecarlo_min=1000,
...     montecarlo_max=5000,
...     walkforward_window_days=[90, 180, 360])
{'in_sample_start': '2020-01-01', 'in_sample_end': '2021-12-31', 'out_sample_start': '2022-01-01', 'out_sample_end': '2022-12-31', 'montecarlo_min': 1000, 'montecarlo_max': 5000, 'walkforward_window_days': [90, 180, 360]}
```

```python
>>> # Invalid example: in_sample_end before start
>>> set_backtest_parameters(
...     in_sample_start='2021-01-01',
...     in_sample_end='2020-12-31',
...     out_sample_start='2021-01-01',
...     out_sample_end='2021-12-31',
...     montecarlo_min=500,
...     montecarlo_max=2000,
...     walkforward_window_days=[30, 60])
ValueError: in_sample_end must be after in_sample_start
```
