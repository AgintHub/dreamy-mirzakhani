# extract_target_values PRD

## Description
Extracts target values from a dictionary of targets.


## Conceptual Info

The extract_target_values shim function is used to extract target values from a dictionary of targets. It plays a crucial role in the set_performance_and_risk_targets function by providing the target values for performance and risk metrics.

## Docstring

### Summary
Extracts target values from a dictionary of targets.

### Parameters

- **targets** (dict): A dictionary containing target values

### Returns

List[float]: A list of target values

### Raises

- ValueError: When the input dictionary is empty or does not contain the expected keys.
- TypeError: When the input is not a dictionary.

### Examples

```python
>>> targets = {'metric1': 0.1, 'metric2': 0.2}
>>> extract_target_values(targets=targets)
[0.1, 0.2]
```

```python
>>> targets = {}
>>> extract_target_values(targets=targets)
[]
```
