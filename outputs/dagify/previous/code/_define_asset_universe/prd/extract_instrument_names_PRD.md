# extract_instrument_names PRD

## Description
Extracts the instrument names from a list of instrument dictionaries.


## Conceptual Info

In the asset universe definition workflow, this shim retrieves the names of the selected instruments to populate the output model.

## Docstring

### Summary
Return a list of instrument names extracted from a list of instrument dictionaries.

### Parameters

- **instruments** (list[dict]): A list of dictionaries, each representing an instrument with at least a 'name' key.

### Returns

list[str]: A list containing the value of the 'name' key from each instrument dictionary, preserving order.

### Raises

- TypeError: If `instruments` is not a list or if any element is not a dict.
- KeyError: If any instrument dictionary does not contain a 'name' key.

### Examples

```python
>>> instruments = [
...     {'name': 'AAPL', 'price': 150},
...     {'name': 'MSFT', 'price': 300},
...     {'name': 'GOOG', 'price': 2800}
>>> ]
>>> names = extract_instrument_names(instruments)
>>> print(names)
['AAPL', 'MSFT', 'GOOG']
```

```python
>>> instruments = [
...     {'id': 1, 'symbol': 'BTC'},
...     {'id': 2, 'symbol': 'ETH'}
>>> ]
>>> try:
...     extract_instrument_names(instruments)
>>> except KeyError as e:
...     print('KeyError:', e)
KeyError: 'name'
```
