# define_strategy_objectives PRD

## Description
Specify the primary goals of the trading strategy


## Conceptual Info

The define_strategy_objectives node captures the high‑level investment objectives that guide the design, optimization, and risk management of the quantitative trading strategy. It translates a user‑written textual description of return targets, risk limits, asset‑class focus, and trading cadence into a structured dictionary that downstream nodes can consume.

## Docstring

### Summary
Parse a textual description of investment objectives and return a structured dictionary containing target return, risk tolerance, asset classes, trading frequency, and any additional constraints.

### Parameters

- **prompt** (str): A string containing the user’s investment objective specification. The prompt should mention the annual return target, maximum risk tolerance, asset classes, trading frequency, and optionally any extra goals.

### Returns

dict: A dictionary with keys:

- annual_return_target_percentage (float)
- maximum_risk_tolerance_percentage (float)
- target_asset_classes (list of str)
- trading_frequency_per_month (int)
- additional_investment_goals (list of str)

Each key maps to the corresponding value extracted from the prompt.

### Raises

- ValueError: If any of the required fields (return target, risk tolerance, asset classes, or trading frequency) cannot be found or parsed from the prompt.
- TypeError: If the prompt argument is not a string.

### Examples

```python
>>> print(define_strategy_objectives('Annual return target: 20%; Max drawdown: 15%; Asset classes: equities, bonds; Trading frequency: 12; Additional goals: ESG compliance.'))
{'annual_return_target_percentage': 20.0, 'maximum_risk_tolerance_percentage': 15.0, 'target_asset_classes': ['equities', 'bonds'], 'trading_frequency_per_month': 12, 'additional_investment_goals': ['ESG compliance']}
```

```python
>>> print(define_strategy_objectives('Annual return target: 15%; Max risk tolerance: 10%; Asset classes: equities; Trading frequency: 8; Additional investment goals: low volatility.'))
{'annual_return_target_percentage': 15.0, 'maximum_risk_tolerance_percentage': 10.0, 'target_asset_classes': ['equities'], 'trading_frequency_per_month': 8, 'additional_investment_goals': ['low volatility']}
```
