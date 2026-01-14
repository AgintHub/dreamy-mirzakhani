# prioritize_by_risk_profile PRD

## Description
Sorts a list of instrument dictionaries by their compatibility with a specified risk profile, returning the reordered list.


## Conceptual Info

The prioritize_by_risk_profile shim is responsible for ordering a collection of investment instruments so that those best aligned with a given risk appetite appear first. This ordering is used downstream to select a balanced set of assets.

## Docstring

### Summary
Return an instrument list sorted by how well each instrument matches the requested risk profile.

### Parameters

- **instruments** (str): A JSON string representing a list of instrument dictionaries, each containing at least a 'risk_score' key and an 'identifier'.
- **risk_profile** (str): Desired risk level ('low', 'medium', 'high') that will guide the sorting heuristic.

### Returns

str: A JSON string of the input instruments sorted in descending order of suitability for the specified risk profile.

### Raises

- ValueError: Raised if 'risk_profile' is not one of the supported values or if any instrument dictionary lacks required keys.
- TypeError: Raised if 'instruments' is not a valid JSON string or if parsed content is not a list of dictionaries.

### Examples

```python
>>> instruments = '[{"identifier": "ABC", "risk_score": 0.2}, {"identifier": "XYZ", "risk_score": 0.8}]'
>>> risk_profile = "high"
>>> result = prioritize_by_risk_profile(instruments, risk_profile)
>>> print(result)
"[{'identifier': 'XYZ', 'risk_score': 0.8}, {'identifier': 'ABC', 'risk_score': 0.2}]"
```

```python
>>> instruments = '[{"identifier": "DEF", "risk_score": 0.5}]'
>>> risk_profile = "low"
>>> print(prioritize_by_risk_profile(instruments, risk_profile))
"[{'identifier': 'DEF', 'risk_score': 0.5}]"
```
