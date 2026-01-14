# construct_nyse_api_request PRD

## Description
Constructs the API request for fetching NYSE stock data.


## Conceptual Info

Constructs the API request for fetching NYSE stock data.

## Docstring

### Summary
Constructs the NYSE API request string.

### Parameters

- **api_endpoint** (str): The base URL of the NYSE API.
- **stock_symbols** (List[str]): The list of stock symbols to query.
- **date_range** (str): The date range for the data query.
- **data_frequency** (str): The data frequency, such as 1-minute or daily bars.
- **api_key_authentication** (str): The API key authentication token for the NYSE API.
- **user_agent_header** (str): The User-Agent header value for the API request.
- **tls_settings** (str): The TLS settings, including the protocol version and cipher suite, for the API request.
- **retry_policy** (str): The retry policy for the NYSE API request, including the number of retries and the backoff strategy.

### Returns

nyse_api_request_string: The constructed NYSE API request string.

### Raises

- ValueError: If any of the required inputs are missing or invalid.
- ConnectionError: If there is a connection issue with the NYSE API.

### Examples

```python
>>> stock_symbols = ['AAPL', 'GOOG', 'MSFT']
>>> date_range = '2020-01-01:2020-01-31'
>>> data_frequency = '1min'
>>> api_key_authentication = 'your_api_key'
>>> user_agent_header = 'Your-User-Agent'
>>> tls_settings = 'TLS 1.2, SHA-256'
>>> retry_policy = '3 retries with exponential backoff'
>>> construct_nyse_api_request(api_endpoint, stock_symbols, date_range, data_frequency, api_key_authentication, user_agent_header, tls_settings, retry_policy)
The constructed NYSE API request string.
```

```python
>>> stock_symbols = ['AAPL', 'GOOG', 'MSFT']
>>> date_range = '2020-01-01:2020-01-31'
>>> data_frequency = '1min'
>>> api_key_authentication = 'your_api_key'
>>> user_agent_header = 'Your-User-Agent'
>>> tls_settings = 'TLS 1.2, SHA-256'
>>> retry_policy = '3 retries with exponential backoff'
>>> construct_nyse_api_request(api_endpoint, stock_symbols, date_range, data_frequency, api_key_authentication, user_agent_header, tls_settings, retry_policy)
The constructed NYSE API request string.
```
