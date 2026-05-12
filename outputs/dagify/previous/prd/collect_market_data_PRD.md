# collect_market_data PRD

## Description
Retrieve raw market price data for the selected assets.


## Conceptual Info

This node collects raw market price data for the selected assets by downloading historical price and volume data at the desired frequency from a reliable source.

## Docstring

### Summary
Collects raw market price data for the selected assets.

### Parameters

- **asset_instruments** (List[str]): List of selected asset instruments
- **markets** (List[str]): List of selected market names
- **instrument_count** (INT): Total number of selected instruments

### Returns

Tuple[List[str], str]: The list of asset symbols retrieved and the path to the output CSV file

### Raises

- ValueError: If the input assets are not valid or the market data cannot be retrieved

### Examples

```python
>>> asset_instruments = ['AAPL', 'GOOG', 'AMZN']
>>> markets = ['NYSE', 'NASDAQ', 'FX']
>>> instrument_count = 3
>>> collect_market_data(asset_instruments, markets, instrument_count)
(['AAPL', 'GOOG', 'AMZN'], 'data_AAPL_NYSE.csv')
```

```python
>>> asset_instruments = ['MSFT', 'FB', 'TSLA']
>>> markets = ['NASDAQ', 'NYSE', 'FX']
>>> instrument_count = 3
>>> collect_market_data(asset_instruments, markets, instrument_count)
(['MSFT', 'FB', 'TSLA'], 'data_MSFT_NYSE.csv')
```
