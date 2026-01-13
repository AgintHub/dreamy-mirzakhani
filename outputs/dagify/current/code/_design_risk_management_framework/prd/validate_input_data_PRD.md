# validate_input_data PRD

## Description
Validates that the lists of metric names, target values, rationale texts, instrument names, and instrument rationales are non‑empty, correctly typed, and of matching lengths, returning a summary string if all checks pass.


## Conceptual Info

This shim enforces consistency and correctness of the core input data that drives the risk‑management framework, ensuring downstream functions receive well‑structured and matched lists.

## Docstring

### Summary
Validate core input lists for consistency, types, and non‑emptiness.

### Parameters

- **metric_names** (str): Comma‑separated list of metric names (e.g., "Gross Return,Volatility").
- **target_values** (str): Comma‑separated list of numeric target values corresponding to metric_names (e.g., "0.15,0.10").
- **rationale_texts** (str): Comma‑separated list of brief rationales for each metric.
- **instrument_names** (str): Comma‑separated list of selected instrument names.
- **instrument_rationales** (str): Comma‑separated list of brief rationales for each instrument.

### Returns

str: A confirmation string of the form "Validation successful: X metrics, Y instruments."

### Raises

- ValueError: If any list is empty or lengths of the lists do not match.
- TypeError: If any argument is not a string or cannot be parsed into the expected list.

### Examples

```python
>>> result = validate_input_data(

...     metric_names="Gross Return,Volatility",

...     target_values="0.15,0.10",

...     rationale_texts="High return,Low volatility",

...     instrument_names="SPY,TLT",

...     instrument_rationales="Large cap equity,Long term Treasury"

>>> )
"Validation successful: 2 metrics, 2 instruments."
```

```python
>>> validate_input_data(

...     metric_names="",

...     target_values="0.15",

...     rationale_texts="High return",

...     instrument_names="SPY",

...     instrument_rationales="Large cap equity"

>>> )
ValueError: metric_names must not be empty
```
