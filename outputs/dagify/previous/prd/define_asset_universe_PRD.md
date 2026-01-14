# define_asset_universe PRD

## Description
Specify tradable asset categories


## Conceptual Info

The node generates a concise list of tradable asset classes that form the hedge fund’s investable universe, aligning with the selected investment strategy.

## Docstring

### Summary
Generate a list of tradable asset classes for the hedge fund’s investable universe.

### Parameters

- **chosen_strategy** (str): The specific hedge fund strategy selected from the predefined categories (e.g., long/short equity, market neutral, global macro, event-driven, arbitrage).

### Returns

Dict[str, Union[List[str], int]]: A dictionary containing two keys:

- ``asset_classes``: a list of specific asset classes/instruments that will constitute the investable universe.
- ``number_of_assets``: an integer representing the count of asset classes listed.

### Raises

- ValueError: If ``chosen_strategy`` is empty or not one of the supported strategy categories.

### Examples

```python
>>> define_asset_universe(chosen_strategy='long/short equity')
{'asset_classes': ['US Equities', 'EU Equities', 'Emerging Market Equities', 'US Equity Options', 'EU Equity Options'], 'number_of_assets': 5}
```

```python
>>> define_asset_universe(chosen_strategy='global macro')
{'asset_classes': ['US Treasuries', 'Eurodollar Futures', 'Gold Futures', 'USD/JPY FX', 'Commodities Futures'], 'number_of_assets': 5}
```
