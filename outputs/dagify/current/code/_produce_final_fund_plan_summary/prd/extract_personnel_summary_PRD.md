# extract_personnel_summary PRD

## Description
Extracts a concise summary of key personnel and their roles from a team description.


## Conceptual Info

The extract_personnel_summary shim function is used to extract a concise summary of key personnel and their roles from a team description. This summary is then used to populate the personnel section of a fund plan summary.

## Docstring

### Summary
Extracts a concise summary of key personnel and their roles from a team description.

### Parameters

- **team_description** (str): A string describing the team, including key personnel and their roles.

### Returns

str: A concise summary of key personnel and their roles.

### Raises

- ValueError: When the input team description is empty or missing.
- TypeError: When the input team description is not a string.

### Examples

```python
>>> extract_personnel_summary(team_description='The team consists of John Doe, CEO; Jane Smith, CTO; and Bob Johnson, CFO.')
'The team consists of John Doe (CEO), Jane Smith (CTO), and Bob Johnson (CFO).'
```

```python
>>> extract_personnel_summary(team_description='')
''
```
