# extract_responsibilities PRD

## Description
Extracts a list of responsibilities for a given responsibility level from a governance template.


## Conceptual Info

This shim parses a governance template dictionary to retrieve responsibilities assigned to each role at a specified hierarchical level, facilitating downstream generation of role-based governance documentation.

## Docstring

### Summary
Return a list of responsibilities for a specified level from a governance template.

### Parameters

- **template** (str): A JSON string representation of the governance template dictionary.
- **responsibility_level** (str): The responsibility level to extract (e.g., '1', '2', or '3').

### Returns

list: A list of strings, each representing a responsibility for the requested level.

### Raises

- ValueError: Raised if the responsibility_level is not one of the expected levels ('1', '2', '3').
- KeyError: Raised if the template does not contain the expected keys for responsibilities.
- TypeError: Raised if template is not a valid JSON string or if responsibility_level is not a string.

### Examples

```python
>>> template = '{"responsibilities": {"1": ["Define scope", "Allocate resources"], "2": ["Implement policy", "Monitor compliance"], "3": ["Audit results", "Report to board"]}}'
>>> extract_responsibilities(template=template, responsibility_level='2')
['Implement policy', 'Monitor compliance']
```

```python
>>> template = '{"responsibilities": {"1": ["Plan", "Budget"], "2": ["Execute", "Review"]}}'
>>> extract_responsibilities(template=template, responsibility_level='1')
['Plan', 'Budget']
```
