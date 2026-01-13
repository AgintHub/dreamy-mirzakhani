# generate_instrument_rationales PRD

## Description
Generate brief rationales for a list of selected investment instruments based on a given strategy category.


## Conceptual Info

The generate_instrument_rationales shim function generates brief rationales for a list of selected investment instruments based on a given strategy category. This function plays a crucial role in providing explanations for the chosen instruments.

## Docstring

### Summary
Generate brief rationales for a list of selected investment instruments based on a given strategy category.

### Parameters

- **instruments** (str): A string representation of the selected instruments.
- **strategy_category** (str): A string representing the strategy category.

### Returns

List[str]: A list of brief rationales for each of the selected instruments.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> generate_instrument_rationales(instruments=['Instrument1', 'Instrument2'], strategy_category='Conservative')
>>> => ['Rationale for Instrument1', 'Rationale for Instrument2']
['Rationale for Instrument1', 'Rationale for Instrument2']
```

```python
>>> generate_instrument_rationales(instruments=['Instrument3', 'Instrument4'], strategy_category='Aggressive')
>>> => ['Rationale for Instrument3', 'Rationale for Instrument4']
['Rationale for Instrument3', 'Rationale for Instrument4']
```
