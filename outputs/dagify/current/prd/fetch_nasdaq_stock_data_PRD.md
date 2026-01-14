# fetch_nasdaq_stock_data PRD

## Description
Retrieves the stock data from the NASDAQ exchange through a technically sophisticated API request.


## Conceptual Info

Fetch NASDAQ stock data over HTTPS

## Docstring

### Summary
Constructs a secure, protocol-compliant HTTP(S) request to the NASDAQ API and fetches the stock data over HTTPS.

### Parameters

- **api_request** (str): API request string
- **timeout** (int): Timeout in seconds
- **retry_policy** (str): Retry policy for handling 500-level server errors

### Returns

dict: Returns a dictionary containing the stock data in JSON format, API endpoint URI, query parameters, HTTP headers, latency, and data feed availability.

### Raises

- Exception: Raises an exception if the API request fails or the timeout is exceeded

### Examples

```python
>>> fetch_nasdaq_stock_data(api_request='https://api.nasdaq.com/qsvc/v1/stocks', timeout=5, retry_policy='2')
{"nasdaq_stock_data": ["{"symbol": "AAPL", "price": 150.0}"]}
```
