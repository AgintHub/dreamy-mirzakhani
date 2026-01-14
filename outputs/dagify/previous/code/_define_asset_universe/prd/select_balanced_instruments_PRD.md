# select_balanced_instruments PRD

## Description
Selects a balanced set of instruments from an input list to meet a target count while preserving diversity and risk preferences.


## Conceptual Info

The shim chooses a subset of instruments that balances asset class representation and risk considerations, ensuring the portfolio reaches the desired number of distinct tradable securities.

## Docstring

### Summary
Selects a balanced subset of instruments from a given list, ensuring the returned set meets the target count and preserves diversity across asset classes while respecting the specified risk profile.

### Parameters

- **instruments** (List[dict]): A list of instrument dictionaries, each containing at least the keys 'name', 'asset_class', and 'risk'.
- **target_count** (int): The desired number of instruments to return.

### Returns

List[dict]: A list of dictionaries representing the selected instruments, matching the structure of the input instruments.

### Raises

- ValueError: Raised if the target_count is less than 1 or greater than the number of unique asset classes available.
- TypeError: Raised if instruments is not a list or if target_count is not an integer.

### Examples

```python
>>> instruments = [
...     {'name': 'StockA', 'asset_class': 'Equity', 'risk': 0.3},
...     {'name': 'BondB', 'asset_class': 'Fixed Income', 'risk': 0.1},
...     {'name': 'CommodityC', 'asset_class': 'Commodity', 'risk': 0.5},
...     {'name': 'StockD', 'asset_class': 'Equity', 'risk': 0.4},
...     {'name': 'BondE', 'asset_class': 'Fixed Income', 'risk': 0.2},
>>> ]
>>> result = select_balanced_instruments(instruments, target_count=3)
>>> print(result)
[{'name': 'StockA', 'asset_class': 'Equity', 'risk': 0.3}, {'name': 'BondB', 'asset_class': 'Fixed Income', 'risk': 0.1}, {'name': 'CommodityC', 'asset_class': 'Commodity', 'risk': 0.5}]
```

```python
>>> select_balanced_instruments([], target_count=5)
ValueError: target_count must be at least 1 and at most the number of unique asset classes available.
```
