# preprocess_data PRD

## Description
Clean and align market data for analysis


## Conceptual Info

Transforms raw market feeds into a structured, feature‑rich 4‑D NumPy array suitable for quantitative modeling.

## Docstring

### Summary
Preprocesses raw market data by normalizing prices, computing volatility, and aligning OHLCV into a 4‑D NumPy array.

### Parameters

- **raw_data** (dict): Dictionary mapping asset tickers to raw OHLCV time series. Each series is a list of dictionaries with keys ['timestamp', 'open', 'high', 'low', 'close', 'volume'].
- **config** (dict): Configuration dict containing preprocessing options: 
- `normalization_method` (str): 'minmax' or 'zscore';
- `volatility_window` (int): Number of periods for rolling volatility;
- `alignment_frequency` (str): Desired resampling frequency (e.g., '1h', '1d');
- `features` (List[str]): Features to compute (e.g., ['price', 'volatility', 'returns']);
- `channels` (List[str]): Optional channels such as ['price', 'volume'].

### Returns

dict: Dictionary containing the processed data and metadata:
- `data`: 4‑D NumPy array of shape [assets, features, time_steps, channels];
- `metadata`: Dict with keys 'array_shape', 'num_assets', 'num_time_steps', 'price_normalized', 'volatility_calculated', 'data_integrity'.

### Raises

- ValueError: If any asset has fewer than 2 valid time steps after alignment.
- KeyError: If required OHLCV keys are missing in raw data.
- RuntimeError: If data integrity checks fail (e.g., NaNs remain after imputation).

### Examples

```python
>>> raw_data = {
...     'AAPL': [
...         {'timestamp': '2023-01-01T09:30:00', 'open': 150.0, 'high': 152.0, 'low': 149.5, 'close': 151.0, 'volume': 1000000},
...         {'timestamp': '2023-01-01T10:30:00', 'open': 151.0, 'high': 153.0, 'low': 150.0, 'close': 152.5, 'volume': 1200000}
...     ],
...     'MSFT': [
...         {'timestamp': '2023-01-01T09:30:00', 'open': 250.0, 'high': 251.0, 'low': 249.0, 'close': 250.5, 'volume': 800000},
...         {'timestamp': '2023-01-01T10:30:00', 'open': 250.5, 'high': 252.0, 'low': 250.0, 'close': 251.0, 'volume': 900000}
...     ]
>>> }
{
  'data': <4‑D array shape [2, 3, 2, 1]>,
  'metadata': {
    'array_shape': [2, 3, 2, 1],
    'num_assets': 2,
    'num_time_steps': 2,
    'price_normalized': true,
    'volatility_calculated': true,
    'data_integrity': true
  }
}
```

```python
>>> config = {
...   'normalization_method': 'minmax',
...   'volatility_window': 10,
...   'alignment_frequency': '1h',
...   'features': ['price', 'volatility'],
...   'channels': ['price']
>>> }
{
  'data': <4‑D array shape [5, 2, 240, 1]>,
  'metadata': {
    'array_shape': [5, 2, 240, 1],
    'num_assets': 5,
    'num_time_steps': 240,
    'price_normalized': true,
    'volatility_calculated': true,
    'data_integrity': true
  }
}
```
