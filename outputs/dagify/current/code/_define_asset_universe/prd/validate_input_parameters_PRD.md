# validate_input_parameters PRD

## Description
Validate that investment strategy inputs are non‑empty strings and conform to predefined categories before proceeding with asset universe construction


## Conceptual Info

This shim ensures that the investment strategy inputs received from the `choose_investment_strategy` node are syntactically and semantically valid before any downstream processing occurs.

## Docstring

### Summary
Validate strategy inputs to ensure they are non-empty strings and match allowed categories, raising errors otherwise.

### Parameters

- **strategy_category** (str): The primary investment strategy category selected by the user.
- **strategy_rationale** (str): A one‑paragraph explanation supporting the chosen strategy.
- **risk_profile** (str): The expected risk profile associated with the chosen strategy.

### Returns

str: A message confirming that all inputs passed validation (e.g., "Validation succeeded").

### Raises

- ValueError: Raised when any input is an empty string or does not match an allowed category/risk profile.
- TypeError: Raised when any input is not of type `str`.

### Examples

```python
>>> validate_input_parameters(strategy_category='Growth',
...                        strategy_rationale='We aim for capital appreciation.',
...                        risk_profile='High')
"Validation succeeded"
```

```python
>>> validate_input_parameters(strategy_category='',
                                     strategy_rationale='Missing category.',
                                     risk_profile='Low')
"ValueError: strategy_category must be a non‑empty string"
```
