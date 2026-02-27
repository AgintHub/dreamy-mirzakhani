# define_asset_universe PRD

## Description
Enumerates the tradable assets and instruments.


## Conceptual Info

This node takes the chosen investment strategy as input and outputs the list of asset classes or instruments the strategy will trade.

## Docstring

### Summary
Enumerate asset classes or instruments for the chosen investment strategy.

### Parameters

- **chosen_investment_strategy** (str): The chosen high-level investment strategy

### Returns

LIST_STR: A list of specific asset classes or instruments that the strategy will trade, with a maximum of ten entries.

### Examples

```python
>>> chosen_investment_strategy = 'Long-Short Equity'
>>> asset_classes_instruments = define_asset_universe(chosen_investment_strategy)
['US large-cap equities', 'Euro-dollar futures', 'credit default swaps']
```
