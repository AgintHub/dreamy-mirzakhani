# execute_out_of_sample PRD

## Description
Validate generalization capability of the strategy by executing it on an unseen 6-month data set, calculating out-of-sample performance metrics, and comparing them against the training period metrics.


## Conceptual Info

This node evaluates the strategy's generalization ability by applying it to a 6-month period that was not seen during training. It generates a full set of performance metrics for that period and then calculates the percentage differences between each metric and its counterpart from the training data, flagging any significant divergence.

## Docstring

### Summary
Run the full strategy on a 6-month out-of-sample period and compare key performance metrics to the training period.

### Parameters

- **training_cagr** (float): CAGR of the training period (used for comparison).
- **training_sharpe** (float): Sharpe ratio of the training period (used for comparison).
- **training_max_drawdown** (float): Maximum drawdown of the training period (used for comparison).
- **training_win_rate** (float): Win rate (0-1) of the training period (used for comparison).
- **training_ulcer_index** (float): Ulcer index of the training period (used for comparison).
- **training_calmar_ratio** (float): Calmar ratio of the training period (used for comparison).
- **strategy_config** (dict): Dictionary containing strategy parameters and risk‑management rules to be applied during the out-of-sample run.

### Returns

dict: Dictionary containing the out-of-sample performance metrics, the start/end dates, the percentage differences to training metrics, and a divergence flag.

### Raises

- ValueError: If any of the required training metric inputs are None or not numeric.
- RuntimeError: If the out-of-sample run fails due to missing data or internal errors.

### Examples

```python
>>> # Dummy training metrics
>>> train_cagr = 0.15
>>> train_sharpe = 1.5
>>> train_max_drawdown = 0.20
>>> train_win_rate = 0.55
>>> train_ulcer = 10.0
>>> train_calmar = 0.75
>>> # Run the node
>>> result = run_out_of_sample(train_cagr, train_sharpe, train_max_drawdown, train_win_rate, train_ulcer, train_calmar, {})
>>> print(result['out_of_sample_cagr'], result['cagr_difference_pct'])
0.142 -6.666666666666664
```

```python
>>> # Second example with a larger divergence
>>> train_cagr = 0.10
>>> train_sharpe = 1.2
>>> train_max_drawdown = 0.15
>>> train_win_rate = 0.60
>>> train_ulcer = 8.0
>>> train_calmar = 0.60
>>> # Simulated out-of-sample metrics: worse performance
>>> result = run_out_of_sample(train_cagr, train_sharpe, train_max_drawdown, train_win_rate, train_ulcer, train_calmar, {})
>>> print(result['performance_divergence_flag'])
True
```
