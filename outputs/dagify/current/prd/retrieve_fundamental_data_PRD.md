# retrieve_fundamental_data PRD

## Description
Collect non-price financial information


## Conceptual Info

The `retrieve_fundamental_data` node gathers essential non‑price financial data—quarterly earnings, balance sheet items, and dividend history—for a set of company tickers. It consolidates the information from Bloomberg and Yahoo Finance into a single raw data file, providing metadata such as the file path, format, retrieval status, and record counts for downstream cleaning and analysis.

## Docstring

### Summary
Collects quarterly earnings reports, balance sheet metrics, and dividend history for a list of company tickers from Bloomberg and Yahoo Finance APIs.

### Parameters

- **tickers** (List[str]): List of company ticker symbols to retrieve fundamental data for.
- **data_sources** (List[str]): Optional list of data source names to use. Defaults to ['Bloomberg', 'Yahoo Finance'].

### Returns

dict: A dictionary containing metadata about the retrieved fundamental data, including file path, format, tickers retrieved/failed, record counts, timestamps, and sources used.

### Raises

- ValueError: If the tickers list is empty.
- RuntimeError: If any API call fails or data cannot be retrieved for all requested tickers.
- TimeoutError: If an API request times out.
- ConnectionError: If network connection errors occur.

### Examples

```python
>>> result = retrieve_fundamental_data(tickers=['AAPL', 'MSFT'])
{"raw_data_file_path": "/tmp/fundamental_data.parquet", "file_format": "Parquet", "tickers_retrieved": ["AAPL", "MSFT"], "missing_tickers": [], "total_earnings_records": 8, "total_balance_sheet_records": 8, "total_dividend_records": 4, "retrieval_success": true, "retrieval_start_time": "2023-12-01T10:00:00Z", "retrieval_end_time": "2023-12-01T10:02:00Z", "data_sources_used": ["Bloomberg", "Yahoo Finance"]}
```

```python
>>> result = retrieve_fundamental_data(tickers=['AAPL', 'FAKE'])
{"raw_data_file_path": "/tmp/fundamental_data.parquet", "file_format": "Parquet", "tickers_retrieved": ["AAPL"], "missing_tickers": ["FAKE"], "total_earnings_records": 4, "total_balance_sheet_records": 4, "total_dividend_records": 2, "retrieval_success": false, "retrieval_start_time": "2023-12-01T10:00:00Z", "retrieval_end_time": "2023-12-01T10:02:00Z", "data_sources_used": ["Bloomberg", "Yahoo Finance"]}
```
