# outline_governance_structure PRD

## Description
Define internal governance framework


## Conceptual Info

The node generates a concise governance chart that outlines the key internal roles and their primary responsibilities for a hedge fund. It supports the pitch deck and overall fund structure by providing a clear, easily digestible representation of governance.

## Docstring

### Summary
Generate a five-role governance chart with one-line duties for each role.

### Parameters

- **legal_entity_type** (str): The chosen legal entity type (e.g., LP, LLC, SICAV). This value is used to contextualize role titles but not directly in the output.

### Returns

dict: Dictionary containing the role names and their corresponding duties.

### Raises

- ValueError: Raised if any input parameter is missing or empty.

### Examples

```python
>>> output = outline_governance_structure(legal_entity_type='LP')
>>> print(output['role1_name'])
>>> print(output['role1_duty'])
"General Partner\nResponsible for investment decisions and fund oversight"
```

```python
>>> output = outline_governance_structure(legal_entity_type='LLC')
>>> print(output['role5_name'])
>>> print(output['role5_duty'])
"Compliance Officer\nEnsures regulatory adherence and internal policy enforcement"
```
