# generate_instrument_rationales PRD

## Description
Generates brief rationales for a list of selected investment instruments based on a given strategy context.


## Conceptual Info

This shim function generates brief rationales for a list of selected investment instruments based on a given strategy context. It is used to provide a concise explanation for each instrument in the Define Asset Universe step.

## Docstring

### Summary
Generate brief rationales for a list of selected investment instruments based on a given strategy context.

### Parameters

- **instruments** (str): A string representation of the list of selected investment instruments
- **strategy_context** (str): A string representation of the strategy context

### Returns

List[str]: A list of brief rationales for each of the selected instruments

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> generate_instrument_rationales(instruments=['Instrument 1', 'Instrument 2'], strategy_context='Conservative')
['Rationale for Instrument 1', 'Rationale for Instrument 2']
```

```python
>>> generate_instrument_rationales(instruments=['Instrument 3', 'Instrument 4'], strategy_context='Aggressive')
['Rationale for Instrument 3', 'Rationale for Instrument 4']
```
