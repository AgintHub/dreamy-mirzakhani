# define_asset_universe PRD

## Description
Enumerate tradable assets/instruments for the selected hedge fund strategy.


## Conceptual Info

This node captures the market scope of the hedge fund by translating the chosen strategy into concrete asset classes and instruments, ensuring alignment with operational and risk frameworks downstream.

## Docstring

### Summary
Generate a mapping of asset classes to specific instruments for a hedge fund strategy.

### Parameters

- **strategy_category** (str): The primary hedge fund strategy selected by `choose_investment_strategy` (e.g., "Long/Short Equity", "Global Macro").

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists: (asset_classes, instrument_types). Both lists contain at most eight string elements and are aligned by index.

### Raises

- ValueError: If `strategy_category` is not one of the supported strategy types.
- RuntimeError: If the derived lists exceed the maximum allowed length or are mismatched.

### Examples

```python
>>> asset_classes, instrument_types = define_asset_universe("Long/Short Equity")
(['Equities', 'Options', 'Fixed Income', 'Commodities'], ['S&P 500 ETF', 'Equity Options', 'US Treasury Bonds', 'Gold Futures'])
```

```python
>>> asset_classes, instrument_types = define_asset_universe("Global Macro")
(['Currencies', 'Futures', 'Equities', 'Fixed Income'], ['EUR/USD', 'Euro Stoxx 50 Futures', 'NASDAQ Composite', 'Euro Government Bonds'])
```
