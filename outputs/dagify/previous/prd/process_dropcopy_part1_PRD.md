# process_dropcopy_part1 PRD

## Description
Securely analyze the initial segment of the retrieved dropcopy data to extract, parse, and structure relevant transactional and market information using OAuth-authenticated access to ensure compliance and data integrity.


## Conceptual Info

This node securely processes the first segment of the retrieved dropcopy data by leveraging OAuth-authenticated access. It extracts and parses detailed trade information including transaction identifiers, instrument symbols, trade sides, volumes, prices, and timestamps. The node ensures data integrity and compliance by validating parsed results and calculating aggregate metrics such as total traded volume and average price, preparing structured data for further processing stages.

## Docstring

### Summary
Processes the initial segment of dropcopy data securely using OAuth authentication to extract structured trade and market details, validating and aggregating the information for downstream use.

### Parameters

- **raw_data_base64** (str): Base64-encoded raw dropcopy data for the first segment retrieved securely from the pico datacenter.
- **access_token** (str): OAuth 2.0 access token used to authenticate the data access and processing requests.

### Returns

dict: A dictionary containing parsed and validated trade data fields including part number, record count, lists of transaction IDs, instrument IDs, sides, volumes, prices, timestamps, a validity flag for extraction success, total volume, and average trade price for the processed segment.

### Raises

- ValueError: If the input raw_data_base64 is empty or improperly encoded.
- AuthenticationError: If OAuth access_token is invalid or expired, denying secure access.
- ParsingError: If extracted data cannot be parsed or validated correctly.

### Examples

```python
>>> result = process_dropcopy_part1(raw_data_base64='QmFzZTY0RW5jb2RlZERhdGE=', access_token='valid_oauth_token')
>>> print(result['part_number'], result['record_count'], result['total_volume'], result['average_price'])
1 10 1500 25.75
```

```python
>>> result = process_dropcopy_part1(raw_data_base64='VGhpcyBpcyBhIHRlc3Q=', access_token='valid_oauth_token')
>>> assert result['is_valid'] is True
>>> assert len(result['transaction_ids']) == result['record_count']
True
```
