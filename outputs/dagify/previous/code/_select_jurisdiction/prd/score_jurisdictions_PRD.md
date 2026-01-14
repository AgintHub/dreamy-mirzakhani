# score_jurisdictions PRD

## Description
Scores jurisdictions based on their suitability for a fund with given requirements.


## Conceptual Info

The score_jurisdictions shim function evaluates a list of candidate jurisdictions against a set of fund requirements and returns a scored list of jurisdictions.

## Docstring

### Summary
Scores jurisdictions based on their suitability for a fund with given requirements.

### Parameters

- **candidates** (str): A string representing candidate jurisdictions.
- **requirements** (str): A string representing fund requirements.

### Returns

List[dict]: A list of dictionaries containing scored jurisdictions.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> score_jurisdictions(candidates='{"jurisdiction1": "desc1"}, {"jurisdiction2": "desc2"}', requirements='{"req1": "desc1"}, {"req2": "desc2"}')
[{"jurisdiction": "jurisdiction1", "score": 0.8}, {"jurisdiction": "jurisdiction2", "score": 0.6}]
```
