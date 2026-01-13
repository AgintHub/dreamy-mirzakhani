# count_distinct_asset_classes PRD

## Description
Counts the number of distinct asset classes represented in a list of instruments.


## Conceptual Info

This shim function takes a list of instruments as input and returns the number of distinct asset classes represented in the list.

## Docstring

### Summary
Counts the number of distinct asset classes in a list of instruments.

### Parameters

- **instruments** (str): A string representation of a list of instruments, where each instrument is associated with an asset class.

### Returns

int: The number of distinct asset classes in the input list of instruments.

### Raises

- ValueError: When the input string is not a valid representation of a list of instruments.
- TypeError: When the input is not a string.

### Examples

```python
>>> instruments = '[{"name": "Instrument 1", "asset_class": "Equity"}, {"name": "Instrument 2", "asset_class": "Fixed Income"}]'
>>> count_distinct_asset_classes(instruments)
2
```

```python
>>> instruments = '[{"name": "Instrument 1", "asset_class": "Equity"}, {"name": "Instrument 2", "asset_class": "Equity"}]'
>>> count_distinct_asset_classes(instruments)
1
```
