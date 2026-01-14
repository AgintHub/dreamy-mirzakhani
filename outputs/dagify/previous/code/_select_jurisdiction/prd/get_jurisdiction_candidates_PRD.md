# get_jurisdiction_candidates PRD

## Description
Retrieves a list of potential jurisdictions, each represented as a dictionary containing jurisdiction details required for later scoring and selection.


## Conceptual Info

This shim serves as the data source for the jurisdiction selection pipeline, providing raw candidate information that is later enriched, scored, and filtered.

## Docstring

### Summary
Return a list of jurisdiction candidate dictionaries for scoring and selection.

### Returns

LIST_STR: A list of jurisdiction dictionaries, e.g., [{'name': 'Cayman Islands', 'tax_rate': 0, 'regulatory_flexibility': 9}, ...].

### Raises

- RuntimeError: If the underlying data source is unreachable or returns malformed data.

### Examples

```python
>>> >>> candidates = get_jurisdiction_candidates()
>>> >>> print(candidates[0]['name'])
Cayman Islands
```

```python
>>> >>> for j in get_jurisdiction_candidates()[:2]:
>>> ...     print(j['name'], j['tax_rate'])
Cayman Islands 0\nBritish Virgin Islands 0
```
