# extract_instrument_names PRD

## Description
Extracts the names of instruments from a list of instrument dictionaries.


## Conceptual Info

The shim encapsulates the logic to pull instrument identifiers from a collection of instrument data structures, enabling downstream processes to work with a clean list of names.

## Docstring

### Summary
Return a list of instrument names extracted from the provided list of instrument dictionaries.

### Parameters

- **instruments** (list): A list of dictionaries, each representing an instrument. Each dictionary must contain a key `'symbol'` whose value is the instrument name.

### Returns

list[str]: A list of strings containing the instrument names in the same order as the input list.

### Raises

- ValueError: If any dictionary in the input list does not contain the key `'symbol'`.
- TypeError: If the input is not a list or contains non-dictionary elements.

### Examples

```python
>>> instruments = [
...     {'symbol': 'AAPL', 'price': 150},
...     {'symbol': 'MSFT', 'price': 300},
>>> ]
>>> print(extract_instrument_names(instruments))
['AAPL', 'MSFT']
```

```python
>>> instruments = [
...     {'symbol': 'TSLA', 'price': 700},
...     {'price': 1000},
>>> ]
>>> extract_instrument_names(instruments)
ValueError: Missing 'symbol' key in one or more instrument dictionaries.
```
