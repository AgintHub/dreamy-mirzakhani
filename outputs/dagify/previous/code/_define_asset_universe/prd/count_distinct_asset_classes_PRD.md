# count_distinct_asset_classes PRD

## Description
Counts the number of unique asset classes among a list of instrument dictionaries.


## Conceptual Info

This shim function aggregates the asset class field from each instrument in the input list and returns the count of unique asset classes, enabling downstream components to assess portfolio diversification.

## Docstring

### Summary
Return the count of unique asset classes in a list of instrument dictionaries.

### Parameters

- **instruments** (List[dict]): A list of dictionaries, each representing an instrument with an 'asset_class' key.

### Returns

int: The number of distinct asset classes present in the input list.

### Raises

- ValueError: Raised when the input list is empty or contains no valid 'asset_class' entries.
- TypeError: Raised when the input is not a list or when any element is not a dictionary.

### Examples

```python
>>> instruments = [
...     {'symbol': 'AAPL', 'asset_class': 'Equity'},
...     {'symbol': 'MSFT', 'asset_class': 'Equity'},
...     {'symbol': 'TLT', 'asset_class': 'Bond'}
>>> ]
>>> count_distinct_asset_classes(instruments)
2
```

```python
>>> instruments = [
...     {'symbol': 'GLD', 'asset_class': 'Commodity'},
...     {'symbol': 'SLV', 'asset_class': 'Commodity'},
...     {'symbol': 'VNQ', 'asset_class': 'Real Estate'}
>>> ]
>>> count_distinct_asset_classes(instruments)
3
```
