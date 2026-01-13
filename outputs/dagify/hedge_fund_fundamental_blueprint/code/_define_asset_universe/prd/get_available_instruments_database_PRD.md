# get_available_instruments_database PRD

## Description
Retrieves a complete list of tradable instruments available for portfolio construction


## Conceptual Info

This shim abstracts the data retrieval layer for tradable instruments, enabling higher‑level strategy nodes to filter and rank assets without hard‑coding the source or schema.

## Docstring

### Summary
Return the full instruments database as a list of dictionaries for downstream processing.

### Returns

list of dict: Each dict contains keys such as 'name', 'ticker', 'asset_class', 'risk_factor', and any other metadata required by the strategy engine.

### Raises

- RuntimeError: If the data source is unreachable or returns an unexpected format.
- ValueError: If the retrieved data cannot be validated against the expected schema.

### Examples

```python
>>> instruments = get_available_instruments_database()
>>> len(instruments)
>>> instruments[0]['name']
100
'Apple Inc.'
```

```python
>>> try:
...     get_available_instruments_database()
>>> except RuntimeError as e:
...     print(str(e))
Data source unavailable.
```
