# select_asset_universe PRD

## Description
Identify the set of assets that will be traded.


## Conceptual Info

This node identifies the set of assets that will be traded by the strategy. It is responsible for selecting the tradable instruments and markets that the strategy will target.

## Docstring

### Summary
This function takes the output of the `define_strategy_goals` node as input and returns a list of selected asset instruments, market names, and the total number of selected instruments.

### Returns

Tuple[List[str], List[str], int]: A tuple containing a list of selected asset instruments, a list of selected market names, and the total number of selected instruments.

### Examples

```python
>>> selected_instruments, selected_markets, instrument_count = select_asset_universe(define_strategy_goals())
('AAPL', 'MSFT', 15)
```
