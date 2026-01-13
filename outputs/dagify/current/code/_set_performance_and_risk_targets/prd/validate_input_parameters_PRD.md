# validate_input_parameters PRD

## Description
Validates that the provided investment strategy parameters are non‑empty and of correct type before further processing.


## Conceptual Info

This shim ensures that the core parameters required to determine investment strategy—namely the strategy category, rationale, and risk profile—are present, non‑empty, and properly typed before any downstream calculations occur.

## Docstring

### Summary
Validate that strategy_category, strategy_rationale, and risk_profile are non‑empty strings and raise appropriate errors otherwise.

### Parameters

- **strategy_category** (str): The chosen primary investment strategy category.
- **strategy_rationale** (str): A one‑paragraph explanation aligning the strategy with the fund's objectives.
- **risk_profile** (str): A concise description of the expected risk profile associated with the chosen strategy.

### Returns

str: A confirmation message such as "Validation successful" when all inputs are valid.

### Raises

- ValueError: Raised when any of the input strings are empty or contain only whitespace.
- TypeError: Raised when any of the inputs is not of type str.

### Examples

```python
>>> validate_input_parameters(strategy_category='Growth',
...                       strategy_rationale='Focus on high growth stocks.',
...                       risk_profile='High')
'Validation successful'
```

```python
>>> try:
...     validate_input_parameters(strategy_category='',
...                               strategy_rationale='Growth',
...                               risk_profile='Medium')
>>> except ValueError as e:
...     print(e)
'strategy_category cannot be empty'
```
