# define_strategy_goals PRD

## Description
Specify high-level performance and risk targets for the strategy.


## Conceptual Info

This node specifies high-level performance and risk targets for the strategy, outlining primary objectives and serving as a blueprint for further development.

## Docstring

### Summary
Define the high-level performance and risk targets for a strategy, including target return, risk tolerance, time horizon, and trading frequency.

### Returns

Tuple[float, float, int, str, List[str]]: A tuple containing the target return percentage, risk tolerance percentage, time horizon in months, trading frequency, and a list of primary objectives.

### Examples

```python
>>> target_return = 0.02,
>>> risk_tolerance = 0.10,
>>> time_horizon = 12,
>>> trading_frequency = 'monthly',
>>> primary_objectives = ['maximize returns', 'minimize risk']
(0.02, 0.1, 12, 'monthly', ['maximize returns', 'minimize risk']
```

```python
>>> target_return = 0.03,
>>> risk_tolerance = 0.08,
>>> time_horizon = 18,
>>> trading_frequency = 'weekly',
>>> primary_objectives = ['maximize returns', 'minimize risk']
(0.03, 0.08, 18, 'weekly', ['maximize returns', 'minimize risk']
```
