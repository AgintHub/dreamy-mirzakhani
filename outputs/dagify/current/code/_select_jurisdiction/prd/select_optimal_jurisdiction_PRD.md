# select_optimal_jurisdiction PRD

## Description
Selects the optimal jurisdiction from a list of scored options based on fund objectives and strategy.


## Conceptual Info

The select_optimal_jurisdiction shim function is responsible for selecting the most suitable jurisdiction for a fund based on its objectives and strategy. It takes a list of scored jurisdiction options as input and returns the optimal jurisdiction.

## Docstring

### Summary
Selects the optimal jurisdiction from a list of scored options.

### Parameters

- **scored_options** (str): A list of dictionaries containing jurisdiction data and scores.

### Returns

str: The optimal jurisdiction

### Raises

- ValueError: When the input list is empty.
- TypeError: When the input is not a list of dictionaries.

### Examples

```python
>>> select_optimal_jurisdiction(scored_options=[{'name': 'Jurisdiction A', 'score': 90}, {'name': 'Jurisdiction B', 'score': 80}])
{'name': 'Jurisdiction A', 'score': 90}
```

```python
>>> select_optimal_jurisdiction(scored_options=[{'name': 'Jurisdiction C', 'score': 70}, {'name': 'Jurisdiction D', 'score': 60}])
{'name': 'Jurisdiction C', 'score': 70}
```
