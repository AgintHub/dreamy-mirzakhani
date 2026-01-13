# extract_authority_scopes PRD

## Description
The extract_authority_scopes shim extracts authority scopes from a given governance template.


## Conceptual Info

The extract_authority_scopes shim is responsible for extracting authority scopes from a governance template, which is crucial for defining roles and responsibilities within an organization.

## Docstring

### Summary
Extracts authority scopes from a given governance template.

### Parameters

- **template** (str): The governance template as a string from which authority scopes will be extracted.

### Returns

List[str]: A list of authority scopes extracted from the governance template.

### Raises

- ValueError: If the input template is invalid or does not contain authority scopes.
- TypeError: If the input template is not a string.

### Examples

```python
>>> authority_scopes = extract_authority_scopes(template='{"roles": [{"name": "CEO", "authority": "Financial"}, {"name": "CTO", "authority": "Technical"}]}')
["Financial", "Technical"]
```

```python
>>> authority_scopes = extract_authority_scopes(template='Invalid template')
ValueError: Invalid template
```
