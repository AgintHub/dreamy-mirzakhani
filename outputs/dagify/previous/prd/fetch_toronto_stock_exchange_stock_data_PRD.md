# fetch_toronto_stock_exchange_stock_data PRD

## Description
Retrieves real-time stock price and volume data for the identified Toronto Stock Exchange securities. The node performs a secure HTTPS request to the TSE API, handling authentication, failover between primary and secondary data centers, and ensuring low-latency delivery. It validates the response schema, logs errors, and emits a clean JSON payload for downstream analytics.


## Conceptual Info

Retrieves real-time stock price and volume data for the identified Toronto Stock Exchange securities.

## Docstring

### Summary
Perform HTTPS GET request to the Toronto Stock Exchange data service with specified query parameters and authentication headers.

### Parameters

- **api_request** (str): Fully constructed API request

### Returns

dict[str, any]: Parsed JSON response from the TSE API

### Raises

- requests.RequestException: If there is a problem with the HTTPS request
- json.JSONDecodeError: If the response is not valid JSON

### Examples

```python
>>> response = fetch_toronto_stock_exchange_stock_data('api_request')
{'timestamp': '2023-03-01 10:00:00', 'exchange': 'NYSE', 'symbol': 'AAPL', 'price': 100.0, 'volume': 1000, 'metadata': {'latency_ms': 80, 'datacenter': 'Toronoto', 'source_url': 'https://api.tse.ca/v1/quotes'}
```
