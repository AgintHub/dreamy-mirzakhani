# extract_role_names PRD

## Description
Extracts role names from a given governance template.


## Conceptual Info

The extract_role_names shim function is responsible for parsing a governance template and extracting the role names defined within it.

## Docstring

### Summary
Extracts role names from a given governance template.

### Parameters

- **template** (str): The governance template to extract role names from. This should be a string representation of a data structure containing role information.

### Returns

List[str]: A list of role names extracted from the template.

### Raises

- ValueError: When the input template is invalid or cannot be parsed.
- TypeError: When the input template is not a string.

### Examples

```python
>>> import json
>>> template = json.dumps({'roles': ['CEO', 'CTO', 'CFO']})
>>> extract_role_names(template=template)
['CEO', 'CTO', 'CFO']
```

```python
>>> template = '{'roles': ['Manager', 'Developer', 'QA']}'
>>> extract_role_names(template=template)
['Manager', 'Developer', 'QA']
```
