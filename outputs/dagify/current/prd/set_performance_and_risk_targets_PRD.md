# set_performance_and_risk_targets PRD

## Description
This node specifies the quantitative performance and risk targets for the hedge fund strategy, translating high-level objectives into numerical goals. It outputs key metrics like expected returns, volatility, Sharpe ratio, and maximum drawdown, based on the selected investment strategy.


## Conceptual Info

This node captures the specific numerical goals for the fund's performance, aligning strategy with measurable targets to guide risk management and performance assessment.

## Docstring

### Summary
Defines numerical performance and risk targets for the hedge fund strategy, outputting key metrics such as expected return, volatility, Sharpe ratio, and max drawdown.

### Parameters

- **annual_gross_return** (float): The targeted annual gross return for the strategy, expressed as a percentage.
- **annual_volatility** (float): The targeted annual volatility (standard deviation) of returns, expressed as a percentage.
- **Sharpe_ratio** (float): The desired Sharpe ratio, representing risk-adjusted return.
- **maximum_drawdown** (float): The maximum allowable peak-to-trough loss during the investment period, expressed as a percentage.

### Returns

dict: A dictionary containing all defined performance and risk metrics, including targets.

### Raises

- ValueError: If any of the inputs are out of realistic range or improperly specified.

### Examples

```python
>>> set_performance_and_risk_targets(
...     annual_gross_return=15.0,
...     annual_volatility=10.0,
...     Sharpe_ratio=1.5,
...     maximum_drawdown=20.0
>>> )
{'annual_gross_return': 15.0, 'annual_volatility': 10.0, 'Sharpe_ratio': 1.5, 'maximum_drawdown': 20.0, 'performance_targets': [15.0], 'risk_targets': [10.0, 1.5, 20.0]}
```

```python
>>> set_performance_and_risk_targets(
...     annual_gross_return=8.0,
...     annual_volatility=12.0,
...     Sharpe_ratio=0.8,
...     maximum_drawdown=30.0
>>> )
{'annual_gross_return': 8.0, 'annual_volatility': 12.0, 'Sharpe_ratio': 0.8, 'maximum_drawdown': 30.0, 'performance_targets': [8.0], 'risk_targets': [12.0, 0.8, 30.0]}
```
