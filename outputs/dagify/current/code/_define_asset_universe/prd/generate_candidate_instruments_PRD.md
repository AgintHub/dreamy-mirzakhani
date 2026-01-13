# generate_candidate_instruments PRD

## Description
Generates a list of candidate instruments based on the provided strategy context.


## Conceptual Info

The generate_candidate_instruments shim function generates a list of candidate instruments based on the provided strategy context. This function plays a crucial role in the investment strategy definition process.

## Docstring

### Summary
Generates a list of candidate instruments based on the provided strategy context.

### Parameters

- **strategy_context** (str): A string representing the strategy context, including category, rationale, and risk profile.

### Returns

List[dict]: A list of dictionaries representing candidate instruments, each containing relevant details such as instrument name, type, and characteristics.

### Raises

- ValueError: When the input strategy context is invalid or incomplete.
- TypeError: When the input strategy context is not a string.

### Examples

```python
>>> generate_candidate_instruments(strategy_context={'category': 'equities', 'rationale': 'long-term growth', 'risk_profile': 'moderate'})
[{'instrument_name': 'AAPL', 'type': 'stock', 'characteristics': {...}}, {'instrument_name': 'GOOGL', 'type': 'stock', 'characteristics': {...}}]
```
