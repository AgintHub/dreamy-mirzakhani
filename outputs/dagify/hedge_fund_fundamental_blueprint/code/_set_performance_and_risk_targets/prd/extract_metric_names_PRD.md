# extract_metric_names PRD

## Description
Extracts metric names from a given set of targets.


## Conceptual Info

The extract_metric_names shim function takes in a set of targets and returns a list of corresponding metric names.

## Docstring

### Summary
Extracts metric names from a given set of targets.

### Parameters

- **targets** (str): A string representation of the targets, expected to be a dictionary or a JSON string representing a dictionary.

### Returns

List[str]: A list of extracted metric names.

### Raises

- ValueError: When the input targets are invalid or cannot be parsed.
- TypeError: When the input type is incorrect.

### Examples

```python
>>> import json
>>> targets = json.dumps({'Gross Return': 0.15, 'Volatility': 0.10})
>>> extract_metric_names(targets=targets)
['Gross Return', 'Volatility']
```

```python
>>> targets = '{'Gross Return': 0.15, 'Volatility': 0.10}'
>>> extract_metric_names(targets=targets)
['Gross Return', 'Volatility']
```
