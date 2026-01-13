# get_candidate_jurisdictions PRD

## Description
Returns a list of candidate jurisdictions for fund domicile based on unclear criteria.


## Conceptual Info

The get_candidate_jurisdictions shim function provides a list of potential jurisdictions for fund domicile. The exact criteria for selection are not specified and will be determined in the future.

## Docstring

### Summary
Returns a list of candidate jurisdictions for fund domicile.

### Returns

List[str]: List of candidate jurisdictions

### Raises

- ValueError: When the list of candidate jurisdictions cannot be generated.
- TypeError: When the output type is incorrect.

### Examples

```python
>>> get_candidate_jurisdictions()
['Cayman Islands', 'Luxembourg', 'Singapore']
```

```python
>>> get_candidate_jurisdictions()
['Ireland', 'Switzerland', 'Hong Kong']
```
