# build_strategy_context PRD

## Description
Creates a strategy context dictionary based on the provided investment strategy category, rationale, and risk profile.


## Conceptual Info

The build_strategy_context shim function generates a strategy context dictionary that captures key information about an investment strategy, including its category, rationale, and risk profile. This context is used to inform subsequent decisions in the investment process.

## Docstring

### Summary
Creates a strategy context dictionary based on the provided investment strategy category, rationale, and risk profile.

### Parameters

- **category** (str): The primary investment strategy category.
- **rationale** (str): A one-paragraph explanation aligning the strategy with the fund's objectives.
- **risk_profile** (str): A concise description of the expected risk profile associated with the chosen strategy.

### Returns

dict: A dictionary representing the strategy context, containing the provided category, rationale, and risk profile.

### Raises

- ValueError: When any of the input parameters are missing or empty.
- TypeError: When the input parameters are of incorrect types.

### Examples

```python
>>> build_strategy_context(category='Growth', rationale='This is a growth strategy.', risk_profile='Moderate')
{'category': 'Growth', 'rationale': 'This is a growth strategy.', 'risk_profile': 'Moderate'}
```

```python
>>> build_strategy_context(category='Income', rationale='This is an income strategy.', risk_profile='Low')
{'category': 'Income', 'rationale': 'This is an income strategy.', 'risk_profile': 'Low'}
```
