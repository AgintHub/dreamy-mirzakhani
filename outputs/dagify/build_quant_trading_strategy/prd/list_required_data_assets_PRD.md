# list_required_data_assets PRD

## Description
Identify necessary data sources


## Conceptual Info

This node maps the chosen quantitative strategy type to a curated set of data assets that the strategy will depend on. It returns a concise list of required data types along with the data category for each type, enabling downstream nodes (e.g., data retrieval and cleaning) to fetch the appropriate datasets.

## Docstring

### Summary
Generate a list of required data types and their categories based on a selected strategy type.

### Parameters

- **strategy_type** (str): The primary strategy category selected in the `choose_strategy_type` node. Expected values are one of: "market neutral", "statistical arbitrage", "momentum", "mean reversion", or "trend following".

### Returns

Dict[str, List[str]]: A dictionary with two keys:

- `data_types`: a list of string identifiers for each data asset required by the strategy (4–8 items).
- `data_categories`: a list of string labels indicating the category of each asset (market data, orderflow, fundamentals, macro). The order of the two lists aligns element‑wise.


### Raises

- ValueError: Raised if `strategy_type` is not one of the supported strategy categories.
- TypeError: Raised if `strategy_type` is not a string.

### Examples

```python
>>> assets = list_required_data_assets('market neutral')
>>> print(assets['data_types'])
>>> print(assets['data_categories'])
['OHLC bars', 'Volume', 'Order book snapshots', 'Statistical spreads', 'Fundamental ratios']
['market data', 'market data', 'orderflow', 'market data', 'fundamentals']
```

```python
>>> assets = list_required_data_assets('statistical arbitrage')
>>> print(assets['data_types'])
>>> print(assets['data_categories'])
['Tick data', 'Volume', 'Implied volatility surface', 'Historical price series', 'Fundamental ratios']
['orderflow', 'market data', 'market data', 'market data', 'fundamentals']
```
