# parse_fund_objectives PRD

## Description
Parses a list of objective bullets into a structured dictionary for downstream analysis.


## Conceptual Info

This shim converts unstructured textual bullet points about a fund's objectives into a machine‑readable dictionary that downstream nodes can consume for investor profiling, risk assessment, and market analysis.

## Docstring

### Summary
Parses a list of objective bullets and returns a structured JSON string.

### Parameters

- **objectives_bullets** (str): A JSON array string of up to 8 bullet points describing the fund's investment purpose, strategy, target returns, and long‑term vision.

### Returns

str: A JSON string representing a dictionary with keys: 'purpose', 'strategy', 'target_return', and 'vision'. Each value is a concise text extracted from the input bullets.

### Raises

- ValueError: Raised if the input JSON string does not decode to a list of strings or if any bullet is empty.
- TypeError: Raised if the input is not a string.

### Examples

```python
>>> parse_fund_objectives('["Deliver alpha through ESG investing", "Focus on renewable energy", "Target 8% IRR over 5 years"]')
"{\n  \"purpose\": \"Deliver alpha through ESG investing\",\n  \"strategy\": \"Focus on renewable energy\",\n  \"target_return\": \"Target 8% IRR over 5 years\",\n  \"vision\": \"\"\n}"
```

```python
>>> parse_fund_objectives('["Global macro strategy", "Liquidity horizon: 2 years", "Risk tolerance: moderate"]')
"{\n  \"purpose\": \"Global macro strategy\",\n  \"strategy\": \"Liquidity horizon: 2 years\",\n  \"target_return\": \"Risk tolerance: moderate\",\n  \"vision\": \"\"\n}"
```
