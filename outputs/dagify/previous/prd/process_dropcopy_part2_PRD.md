# process_dropcopy_part2 PRD

## Description
Securely process the second segment of the retrieved dropcopy using OAuth-authenticated access to ensure authorized extraction of critical trade and market information with precision and data integrity.


## Conceptual Info

This node securely processes the second segment of dropcopy trading data retrieved from the pico datacenter using validated OAuth authentication. It ensures that data extraction from the raw segment is authorized and accurate, transforming base64-encoded, authenticated raw data into structured, validated trade records including trade identifiers, prices, volumes, symbols, timestamps, and trade sides. The node enforces data integrity and access compliance, producing a well-defined, authenticated, and complete subset of trade information for downstream analysis, storage, and merging.

## Docstring

### Summary
Process the second segment of dropcopy data retrieved via OAuth authentication to extract and structure trade information with integrity and security guarantees.

### Parameters

- **raw_data_base64** (str): Base64-encoded raw dropcopy data for the second segment, obtained from a secure OAuth-authenticated source.
- **access_token** (str): OAuth 2.0 access token authorizing access to the dropcopy data.

### Returns

dict[str, list]: Dictionary containing lists of trade-related data fields extracted from the second dropcopy segment: 'trade_ids', 'prices', 'volumes', 'symbols', 'timestamps', and 'sides'. Each list corresponds to records parsed from the segment with data integrity and compliance assured.

### Raises

- ValueError: If the input data is malformed or fails validation checks.
- AuthenticationError: If the provided OAuth token is invalid, expired, or unauthorized for accessing this data.
- ParseError: If extraction or parsing of trade data from the dropcopy segment fails due to unexpected format or corruption.

### Examples

```python
>>> result = process_dropcopy_part2(raw_data_base64, access_token)
>>> print(result['trade_ids'])
>>> print(result['prices'])
['T12345', 'T12346']
[102.5, 103.0]
```

```python
>>> segment_data = '...'  # Base64-encoded dropcopy part 2 segment
>>> token = 'valid_oauth_token_value'
>>> trades = process_dropcopy_part2(segment_data, token)
>>> assert all(isinstance(tid, str) for tid in trades['trade_ids'])
>>> assert all(isinstance(price, float) for price in trades['prices'])
No exceptions raised; data correctly parsed and typed.
```
