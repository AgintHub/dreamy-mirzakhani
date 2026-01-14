# generate_quantitative_controls PRD

## Description
Generates a list of quantifiable risk controls based on risk profile, portfolio complexity, target values, and asset class count.


## Conceptual Info

The shim encapsulates the logic for translating high‑level risk parameters into actionable, numeric risk controls that can be applied within the portfolio.

## Docstring

### Summary
Generate a set of quantifiable risk controls based on the supplied risk profile, portfolio complexity, target values, and asset class count.

### Parameters

- **risk_profile** (str): Categorical description of the portfolio’s risk appetite (e.g., 'conservative', 'moderate', 'aggressive').
- **portfolio_complexity** (str): Assessment of portfolio complexity (e.g., 'simple', 'moderate', 'complex') derived from instrument count and diversification.
- **target_values** (str): JSON‑encoded list of numeric target values corresponding to each performance metric.
- **asset_class_count** (str): JSON‑encoded integer indicating how many distinct asset classes are represented in the portfolio.

### Returns

LIST_STR: A list of human‑readable control descriptions, e.g., ['Limit VaR to 5% of portfolio value', 'Cap concentration to 10% per asset class'].

### Raises

- ValueError: Raised when any input string cannot be parsed into the expected format (e.g., malformed JSON).
- TypeError: Raised when input types do not match the expected signatures.

### Examples

```python
>>> import json
>>> risk_profile = 'aggressive'
>>> portfolio_complexity = 'complex'
>>> target_values = json.dumps([0.20, 0.10])
>>> asset_class_count = json.dumps(4)
>>> controls = generate_quantitative_controls(risk_profile, portfolio_complexity, target_values, asset_class_count)
['Cap VaR at 7% of portfolio value', 'Maintain turnover below 15% annually', 'Ensure no single asset class exceeds 12% of total value']
```

```python
>>> risk_profile = 'conservative'
>>> portfolio_complexity = 'simple'
>>> target_values = json.dumps([0.05, 0.02])
>>> asset_class_count = json.dumps(2)
>>> controls = generate_quantitative_controls(risk_profile, portfolio_complexity, target_values, asset_class_count)
['Limit VaR to 3% of portfolio value', 'Restrict concentration to 8% per asset class']
```
