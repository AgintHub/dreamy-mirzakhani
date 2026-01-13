# extract_key_advantages PRD

## Description
Returns a list of the top N key advantages of a given jurisdiction based on its data dictionary.


## Conceptual Info

This shim analyzes jurisdiction metadata to surface the most compelling advantages that support fund strategy decisions.

## Docstring

### Summary
Extracts a specified number of key advantages from a jurisdiction data dictionary.

### Parameters

- **jurisdiction_data** (dict): A dictionary containing jurisdiction attributes, expected to include an 'advantages' list or a free‑text 'description' field.
- **count** (int): The number of top advantages to return. Must be a positive integer.

### Returns

List[str]: A list of up to `count` advantage strings sorted by relevance.

### Raises

- TypeError: If `jurisdiction_data` is not a dictionary or `count` is not an integer.
- ValueError: If `count` is less than 1 or exceeds the available advantage entries.

### Examples

```python
>>> data = {
...     'name': 'Cyprus',
...     'advantages': ['Low tax rates', 'EU membership', 'English common law', 'Fast company registration']
>>> }
>>> print(extract_key_advantages(jurisdiction_data=data, count=2))
['Low tax rates', 'EU membership']
```

```python
>>> data = {
...     'name': 'Guernsey',
...     'description': 'Guernsey offers a stable regulatory environment, tax neutrality, and access to the UK market.'
>>> }
>>> print(extract_key_advantages(jurisdiction_data=data, count=3))
['Stable regulatory environment', 'Tax neutrality', 'Access to the UK market']
```
