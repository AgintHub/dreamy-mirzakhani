# generate_primary_responsibilities PRD

## Description
Generate primary responsibilities for roles based on the entity type.


## Conceptual Info

The generate_primary_responsibilities shim function generates primary responsibilities for roles based on the entity type. It takes an entity type and a list of role names as input and returns a list of primary responsibilities for each role.

## Docstring

### Summary
Generate primary responsibilities for roles based on the entity type.

### Parameters

- **entity_type** (str): The type of entity (e.g., LP, LLC, SICAV)
- **role_names** (str): Comma-separated list of role names

### Returns

List[str]: List of primary responsibilities for each role

### Raises

- ValueError: When the entity type is not supported
- TypeError: When the input types are incorrect

### Examples

```python
>>> generate_primary_responsibilities(entity_type='LLC', role_names='CEO,CTO,CFO')
>>> => ['Manage company operations', 'Oversee technology strategy', 'Manage financials']
['Manage company operations', 'Oversee technology strategy', 'Manage financials']
```

```python
>>> generate_primary_responsibilities(entity_type='LP', role_names='General Partner, Limited Partner')
>>> => ['Manage fund operations', 'Invest in fund']
['Manage fund operations', 'Invest in fund']
```
