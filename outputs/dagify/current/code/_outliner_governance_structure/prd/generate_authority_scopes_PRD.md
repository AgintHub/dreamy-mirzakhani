# generate_authority_scopes PRD

## Description
Generates a list of authority scopes for given entity type and role names.


## Conceptual Info

The generate_authority_scopes shim function generates a list of authority scopes for a given entity type and role names. This function is used to define the authority scopes for different roles within an organization.

## Docstring

### Summary
Generates a list of authority scopes for given entity type and role names.

### Parameters

- **entity_type** (str): The entity type for which authority scopes are generated (e.g., LP, LLC, SICAV)
- **role_names** (str): The role names for which authority scopes are generated (comma-separated)

### Returns

List[str]: List of authority scopes corresponding to the input role names

### Raises

- ValueError: When input validation fails (e.g., invalid entity type or role names)
- TypeError: When input types are incorrect (e.g., entity type or role names are not strings)

### Examples

```python
>>> generate_authority_scopes(entity_type='LP', role_names='role1,role2,role3')
['authority_scope_1', 'authority_scope_2', 'authority_scope_3']
```

```python
>>> generate_authority_scopes(entity_type='LLC', role_names='CEO,CFO,CTO')
['authority_scope_ceo', 'authority_scope_cfo', 'authority_scope_cto']
```
