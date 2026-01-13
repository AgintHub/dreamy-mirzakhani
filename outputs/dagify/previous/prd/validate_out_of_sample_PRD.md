# validate_out_of_sample PRD

## Description
Test the top‑ranked parameter combination on fresh market data outside the training window, quantify its performance relative to the in‑sample period, and apply statistical tests to flag potential over‑fitting.


## Conceptual Info

Runs the best parameter combination identified by Bayesian optimisation on a held‑out data window, compares key risk‑return metrics to the in‑sample period, and applies three statistical tests to detect over‑fitting.

## Docstring

### Summary
Validate a strategy on out‑of‑sample data and detect over‑fitting.

### Parameters

- **top3_parameters** (list[str]): List of the top three parameter‑set strings produced by ``optimize_parameters``.
- **top3_sharpe** (list[float]): Sharpe ratios corresponding to each of the top three parameter sets.
- **in_sample_equity** (dict): Dictionary containing in‑sample equity curve data with keys ``dates`` and ``values``.
- **out_sample_start** (str): ISO format start date of the out‑sample window (YYYY‑MM‑DD).
- **out_sample_end** (str): ISO format end date of the out‑sample window (YYYY‑MM‑DD).
- **backtest_function** (Callable): Callable that accepts a parameter set string and returns a dict with ``sharpe`` and ``max_drawdown`` for a given date range.

### Returns

dict: A dictionary containing the selected parameter set identifier, in‑sample and out‑of‑sample Sharpe ratios, max drawdowns, and over‑fitting test results.

### Raises

- ValueError: If the ``top3_parameters`` list is empty or does not contain the selected set.
- RuntimeError: If the backtest function fails to return a valid performance metric.

### Examples

```python
>>> top3_parameters = ['alpha=0.1,beta=0.2,gamma=0.3',
...                 'alpha=0.15,beta=0.25,gamma=0.35',
...                 'alpha=0.2,beta=0.3,gamma=0.4']
>>> top3_sharpe = [1.25, 1.10, 0.95]
>>> in_sample_equity = {
...     'dates': ['2020-01-01', '2020-01-02'],
...     'values': [100000, 102500]}
>>> def dummy_backtest(param_set):
...     return {'sharpe': 1.05 if 'alpha=0.1' in param_set else 0.9,
...             'max_drawdown': 0.12}
>>> result = validate_out_of_sample(
...     top3_parameters=top3_parameters,
...     top3_sharpe=top3_sharpe,
...     in_sample_equity=in_sample_equity,
...     out_sample_start='2020-02-01',
...     out_sample_end='2020-04-01',
...     backtest_function=dummy_backtest)
{
  'selected_param_set': 'alpha=0.1,beta=0.2,gamma=0.3',
  'in_sample_sharpe': 1.25,
  'out_of_sample_sharpe': 1.05,
  'in_sample_max_drawdown': 0.12,
  'out_of_sample_max_drawdown': 0.12,
  'overfitting_tests_passed': [True, False, True],
  'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
}
```

```python
>>> # Using the second best parameter set
result2 = validate_out_of_sample(
...     top3_parameters=top3_parameters,
...     top3_sharpe=top3_sharpe,
...     in_sample_equity=in_sample_equity,
...     out_sample_start='2020-02-01',
...     out_sample_end='2020-04-01',
...     backtest_function=dummy_backtest)
{
  'selected_param_set': 'alpha=0.15,beta=0.25,gamma=0.35',
  'in_sample_sharpe': 1.10,
  'out_of_sample_sharpe': 0.90,
  'in_sample_max_drawdown': 0.12,
  'out_of_sample_max_drawdown': 0.12,
  'overfitting_tests_passed': [False, False, True],
  'overfitting_test_names': ['t-test', 'Diebold-Mariano', 'ADF']
}
```
