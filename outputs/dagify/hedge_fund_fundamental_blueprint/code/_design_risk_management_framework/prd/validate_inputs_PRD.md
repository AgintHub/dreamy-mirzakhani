# validate_inputs PRD

## Description
Validates and normalizes the input data for performance, risk, and asset universe parameters before they are used to design a risk management framework.


## Conceptual Info

The `validate_inputs` shim acts as a gatekeeper, ensuring that all downstream nodes receive consistent, correctly typed, and logically coherent data. It checks that lists are of matching lengths, that numeric targets are within sensible bounds, that rationales are non‑empty, and that asset class counts reflect the supplied instrument list.

## Docstring

### Summary
Validate and normalize input parameters for the risk management framework.

### Parameters

- **metric_names** (List[str]): Names of the performance and risk metrics (e.g., ['Gross Return', 'Volatility']).
- **target_values** (List[float]): Numerical target values corresponding to each metric.
- **rationale_texts** (List[str]): Rationale explaining each target.
- **instrument_names** (List[str]): Names of the selected tradable instruments.
- **instrument_rationales** (List[str]): Rationale for selecting each instrument.
- **asset_class_count** (int): Number of distinct asset classes represented among the instruments.

### Returns

str: A success message if all inputs are valid; otherwise an error message describing the first validation failure.

### Raises

- ValueError: Raised when any list is empty, when list lengths do not match, or when numeric targets are out of acceptable bounds.
- TypeError: Raised when an input parameter is not of the expected type.

### Examples

```python
>>> validate_inputs(metric_names=['Gross Return', 'Volatility'],
...                 target_values=[0.15, 0.10],
...                 rationale_texts=['Aim for 15% return', 'Limit volatility to 10%'],
...                 instrument_names=['AAPL', 'MSFT', 'TSLA'],
...                 instrument_rationales=['Tech exposure', 'Large cap stability', 'Growth potential'],
...                 asset_class_count=1)
'Validation successful: all inputs are coherent.'
```

```python
>>> validate_inputs(metric_names=['Gross Return'],
...                 target_values=[0.15, 0.10],
...                 rationale_texts=['Aim for 15% return'],
...                 instrument_names=['AAPL'],
...                 instrument_rationales=['Tech exposure'],
...                 asset_class_count=1)
ValueError: Length mismatch between metrics (1) and target values (2).
```
