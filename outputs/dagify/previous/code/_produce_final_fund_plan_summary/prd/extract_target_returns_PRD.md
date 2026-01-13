# extract_target_returns PRD

## Description
Extracts target returns summary from risk-return analysis input.


## Conceptual Info

The extract_target_returns shim function takes risk-return analysis input and extracts a concise summary of target returns.

## Docstring

### Summary
Extracts target returns summary from risk-return analysis input.

### Parameters

- **risk_return_analysis** (str): Input risk-return analysis

### Returns

str: Target returns summary

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> extract_target_returns(risk_return_analysis='The fund aims to achieve annual returns of 8-12% with a maximum drawdown of 10%.')
'The fund aims to achieve annual returns of 8-12% with a maximum drawdown of 10%.'
```

```python
>>> extract_target_returns(risk_return_analysis='Target returns are 9-11% per annum with a risk profile of moderate.')
>>> print(output)
'Target returns are 9-11% per annum with a risk profile of moderate.'
```
