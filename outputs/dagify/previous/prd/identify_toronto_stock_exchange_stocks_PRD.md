# identify_toronto_stock_exchange_stocks PRD

## Description
Compiles a comprehensive, protocol-aware catalog of active Toronto Stock Exchange equities for automated data ingestion. The node specifies each ticker's sector, market-cap classification, optimal data-feed protocol with associated latency expectations, and the primary data-center location to enable latency-optimized routing and high-availability strategies.


## Conceptual Info

Identify and assemble a protocol-aware catalog of active TSE equities with latency and datacenter guidance to enable downstream ingestion routing and SLAs.

## Docstring

### Summary
Return a curated list of Toronto Stock Exchange equities with ticker, company_name, sector_industry, market_cap_tier, preferred_data_feed_protocol, expected_latency_ms, and datacenter.

### Returns

List[Dict[str, Any]]: A list where each element is a dict with keys: ticker, company_name, sector_industry, market_cap_tier, preferred_data_feed_protocol, expected_latency_ms, datacenter.

### Raises

- ValueError: If the resolved catalog contains missing mandatory fields or invalid value ranges.
- TypeError: If the resolved catalog elements are not dictionaries with the expected schema.

### Examples

```python
>>> identify_toronto_stock_exchange_stocks()
[{'ticker': 'BCE', 'company_name': 'BCE Inc.', 'sector_industry': 'Communication Services - Telecom', 'market_cap_tier': 'Large', 'preferred_data_feed_protocol': 'WebSocket', 'expected_latency_ms': 20, 'datacenter': 'Toronto (ON-1)'}, {'ticker': 'SHOP', 'company_name': 'Shopify Inc.', 'sector_industry': 'Technology - Internet Retail', 'market_cap_tier': 'Large', 'preferred_data_feed_protocol': 'REST', 'expected_latency_ms': 45, 'datacenter': 'Toronto (ON-1)'}]
```
