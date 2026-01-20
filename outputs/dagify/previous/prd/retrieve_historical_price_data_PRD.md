# retrieve_historical_price_data PRD

## Description
Acquire historical price data from specified sources for a set of liquid equity instruments across multiple exchanges.


## Conceptual Info

This node retrieves granular price data for a selected set of liquid equity instruments from multiple exchanges over a defined period and granularity, storing the results locally for downstream analysis.

## Docstring

### Summary
Retrieves historical price data for a list of instruments from multiple exchanges within a specified date range and granularity. Stores the data locally and returns metadata about the retrieval.

### Parameters

- **instrument_ids** (List[str]): Identifiers of the instruments to fetch price data for (e.g., ['AAPL', 'MSFT']).
- **exchange_ids** (List[str]): Identifiers of the exchanges to pull data from (e.g., ['NYSE', 'NASDAQ', 'BATS']).
- **start_date** (str): Start date of the data retrieval in ISO format 'YYYY-MM-DD'.
- **end_date** (str): End date of the data retrieval in ISO format 'YYYY-MM-DD'.
- **timeframe** (str): Granularity of the bars requested (e.g., '1m', '1d', '1w').

### Returns

dict: Dictionary containing metadata and file path for the retrieved price data.

### Raises

- ValueError: Raised when start_date is later than end_date or when required parameters are missing.
- TimeoutError: Raised if the data source does not respond within the allotted time.
- ConnectionError: Raised when network connectivity or API credentials are invalid.
- RuntimeError: Raised for any non-recoverable data retrieval failures.

### Examples

```python
>>> prices = retrieve_historical_price_data(
...     instrument_ids=['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'],
...     exchange_ids=['NYSE', 'NASDAQ'],
...     start_date='2010-01-01', end_date='2024-01-01', timeframe='1d')
{'data_file_path': '/data/prices_2010_2024_1d.csv', 'instrument_ids': ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'AMZN'], 'exchange_ids': ['NYSE', 'NASDAQ'], 'start_date': '2010-01-01', 'end_date': '2024-01-01', 'timeframe': '1d', 'total_records': 1234567, 'data_retrieved': True, 'retrieval_timestamp': '2024-01-01T12:00:00Z'}
```

```python
>>> prices = retrieve_historical_price_data(
...     instrument_ids=['AAPL'],
...     exchange_ids=['NASDAQ'],
...     start_date='2019-01-01', end_date='2019-12-31', timeframe='1m')
{'data_file_path': '/data/prices_2019_1m.csv', 'instrument_ids': ['AAPL'], 'exchange_ids': ['NASDAQ'], 'start_date': '2019-01-01', 'end_date': '2019-12-31', 'timeframe': '1m', 'total_records': 123456, 'data_retrieved': True, 'retrieval_timestamp': '2019-12-31T23:59:59Z'}
```
