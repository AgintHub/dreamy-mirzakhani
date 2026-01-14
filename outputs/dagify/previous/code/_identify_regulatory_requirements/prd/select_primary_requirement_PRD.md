# select_primary_requirement PRD

## Description
Selects the primary regulatory requirement from a list of requirements.


## Conceptual Info

The select_primary_requirement shim is used to identify the most critical regulatory requirement from a list of requirements. This is essential in determining the primary compliance obligation for a given legal entity and jurisdiction.

## Docstring

### Summary
Selects the primary regulatory requirement from a list of requirements based on a set of predefined criteria.

### Parameters

- **requirements_list** (str): A list of regulatory requirements in JSON format.

### Returns

str: The primary regulatory requirement in JSON format.

### Raises

- ValueError: When the input list is empty or invalid.
- TypeError: When the input is not a string or the output is not a string.

### Examples

```python
>>> import json
>>> requirements_list = '[{"requirement": "req1"}, {"requirement": "req2"}]'
>>> select_primary_requirement(requirements_list=json.loads(requirements_list))
{"requirement": "req1"}
```

```python
>>> import json
>>> requirements_list = '[{"requirement": "req3"}, {"requirement": "req4"}]'
>>> select_primary_requirement(requirements_list=json.loads(requirements_list))
{"requirement": "req3"}
```
