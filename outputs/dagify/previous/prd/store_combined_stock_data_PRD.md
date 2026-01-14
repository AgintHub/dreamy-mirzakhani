# store_combined_stock_data PRD

## Description
Persist the aggregated, cleaned, and normalized stock data from LSE, NYSE, NASDAQ, and TSX into a fault-tolerant, geo-distributed data lake with strict schema validation, versioning, and low-latency ingestion via HTTPS/REST.


## Conceptual Info

This function stores the combined stock data in a geo-distributed data lake with strict schema validation, versioning, and low-latency ingestion.

## Docstring

### Summary
Store the combined stock data in a geo-distributed data lake with strict schema validation, versioning, and low-latency ingestion.

### Parameters

- **lse_data** (List[str]): LSE stock data from `parse_lse_stock_data` node.
- **nasdaq_data** (List[str]): NASDAQ stock data from `parse_nasdaq_stock_data` node.
- **nyse_data** (List[str]): NYSE stock data from `parse_nyse_stock_data` node.
- **tsx_data** (List[str]): TSX stock data from `parse_toronto_stock_exchange_stock_data` node.

### Returns

Dict[str, str]: Dictionary containing boolean indicating schema validation, current versioning status, ingestion latency, data lake region, and current data lake size.

### Raises

- ValueError: If input data is not in the correct format.

### Examples

```python
>>> lse_data = parse_lse_stock_data(fetch_lse_stock_data())
>>> nasdaq_data = parse_nasdaq_stock_data(fetch_nasdaq_stock_data())
>>> nyse_data = parse_nyse_stock_data(fetch_nyse_stock_data())
>>> tsx_data = parse_toronto_stock_exchange_stock_data(fetch_toronto_stock_exchange_stock_data())
>>> store_combined_stock_data(lse_data, nasdaq_data, nyse_data, tsx_data)
{schema_validated: True, versioning_status: Version 1.0, ingestion_latency_ms: 100, data_lake_region: US East, data_lake_size_gb: 100.0}
```
