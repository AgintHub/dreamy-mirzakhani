# fetch_lse_stock_data PRD

## Description
Initiates a secured, HTTPS-based data fetch operation from the London Stock Exchange (LSE) via a meticulously constructed API request, incorporating detailed parameters for stock symbols, data frequency, and time range, while ensuring robust error handling and exception management to guarantee data integrity and consistency, across multiple datacenters in London, New York, and Singapore with latency averaging 50ms, 100ms, and 120ms respectively.


## Conceptual Info

Fetches stock data from the London Stock Exchange (LSE) using a meticulously constructed API request.

## Docstring

### Summary
Fetches stock data from the London Stock Exchange (LSE).

### Parameters

- **lse_api_request** (str): The LSE API request.

### Returns

tuple[str, bool, float, str]: A tuple containing the raw JSON data, a boolean indicating whether any errors occurred, the average latency, and the datacenter used to fetch the data.

### Raises

- Exception: If an unexpected error occurs during the data fetch operation.

### Examples

```python
>>> lse_api_request = construct_lse_api_request().lse_api_url
(raw_json_data, False, latency, datacenter)
```
