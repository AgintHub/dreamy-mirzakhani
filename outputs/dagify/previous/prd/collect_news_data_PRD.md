# collect_news_data PRD

## Description
Collect news data related to the identified assets for trading


## Conceptual Info

This node gathers relevant news data for the assets to be tracked by the quantitative trading strategy.

## Docstring

### Summary
Collect news data related to the identified assets for trading.

### Parameters

- **asset_instruments** (List[str]): List of asset symbols to collect news data for
- **time_period** (int): Number of years to collect news data for

### Returns

Dict[str, List[str]]: Dictionary with asset IDs as keys and lists of news headlines and article bodies as values

### Raises

- ValueError: If the asset_instruments parameter is empty or not a list of strings

### Examples

```python
>>> # Import required libraries
>>> import requests
>>> import json
>>> # Define the asset instruments to collect news data for
>>> asset_instruments = ['AAPL', 'GOOG', 'AMZN']
>>> # Collect news data for the past year
>>> response = collect_news_data(asset_instruments, 1)
{'AAPL': ['News Headline 1', 'News Headline 2'], 'GOOG': ['News Headline 3', 'News Headline 4'], 'AMZN': ['News Headline 5', 'News Headline 6']}
```
