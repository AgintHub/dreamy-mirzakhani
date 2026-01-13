# assess_risk_tolerance_levels PRD

## Description
Evaluates a fund’s objectives and its target investors to produce a list of suitable risk tolerance levels.


## Conceptual Info

This shim translates high‑level fund objectives and investor profiles into concrete risk tolerance categories that the fund can offer. It serves as a bridge between strategic intent and practical investment product design.

## Docstring

### Summary
Generate risk tolerance levels for a fund based on its objectives and target investor types.

### Parameters

- **fund_objectives** (dict): Dictionary containing parsed fund objectives, typically including strategy type, target return, time horizon, and geographical focus.
- **target_investors** (list): List of strings representing the types of investors the fund intends to attract (e.g., ['family_office', 'pension_fund']).

### Returns

list[str]: A list of risk tolerance levels appropriate for the given fund objectives and investor base.

### Raises

- ValueError: Raised if `fund_objectives` is empty or missing required keys.
- TypeError: Raised if `fund_objectives` is not a dict or `target_investors` is not a list.

### Examples

```python
>>> fund_obj = {"strategy_type": "growth", "target_return": 0.12, "time_horizon": 5, "geo_focus": "global"}
>>> investors = ["family_office", "institutional"]
>>> levels = assess_risk_tolerance_levels(fund_objectives=fund_obj, target_investors=investors)
>>> print(levels)
["Aggressive", "Moderate"]
```

```python
>>> fund_obj = {"strategy_type": "income", "target_return": 0.04, "time_horizon": 10, "geo_focus": "US"}
>>> investors = ["retirement_fund"]
>>> levels = assess_risk_tolerance_levels(fund_objectives=fund_obj, target_investors=investors)
>>> print(levels)
["Conservative"]
```
