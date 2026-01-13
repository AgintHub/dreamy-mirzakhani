# filter_instruments_by_strategy PRD

## Description
Filters a list of available instruments based on a specified investment strategy category and rationale.


## Conceptual Info

This shim function filters a list of available instruments based on a specified investment strategy category and rationale, and returns a list of dictionaries representing the filtered instruments.

## Docstring

### Summary
Filters a list of available instruments based on a specified investment strategy category and rationale.

### Parameters

- **instruments** (List[dict]): A list of dictionaries representing the available instruments.
- **strategy_category** (str): The primary investment strategy category.
- **strategy_rationale** (str): A one-paragraph explanation aligning the strategy with the fund's objectives.

### Returns

List[dict]: A list of dictionaries representing the filtered instruments.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> available_instruments = [{'name': 'Instrument 1', 'asset_class': 'Stock'}, {'name': 'Instrument 2', 'asset_class': 'Bond'}]
>>> filtered_instruments = filter_instruments_by_strategy(instruments=available_instruments, strategy_category='Conservative', strategy_rationale='Low risk tolerance')
>>> print(filtered_instruments)
[{'name': 'Instrument 2', 'asset_class': 'Bond'}]
```

```python
>>> available_instruments = [{'name': 'Instrument 1', 'asset_class': 'Stock'}, {'name': 'Instrument 2', 'asset_class': 'Bond'}]
>>> filtered_instruments = filter_instruments_by_strategy(instruments=available_instruments, strategy_category='Aggressive', strategy_rationale='High risk tolerance')
>>> print(filtered_instruments)
[{'name': 'Instrument 1', 'asset_class': 'Stock'}]
```
