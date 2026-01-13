# generate_tertiary_responsibilities PRD

## Description
Generate tertiary responsibilities for roles in a given entity type.


## Conceptual Info

This shim function generates tertiary responsibilities for roles in a given entity type, which is used to outline the governance structure.

## Docstring

### Summary
Generate tertiary responsibilities for roles in a given entity type.

### Parameters

- **entity_type** (str): The entity type for which tertiary responsibilities are generated (e.g., LP, LLC, SICAV)
- **role_names** (str): The role names for which tertiary responsibilities are generated

### Returns

List[str]: List of tertiary responsibilities for each role

### Raises

- ValueError: When entity type or role names are invalid
- TypeError: When input types are incorrect

### Examples

```python
>>> generate_tertiary_responsibilities(entity_type='LLC', role_names='Manager,Employee')
['Manage finances', 'Develop business strategy', 'Oversee daily operations']
```

```python
>>> generate_tertiary_responsibilities(entity_type='LP', role_names='General Partner,Limited Partner')
['Manage fund investments', 'Oversee portfolio performance', 'Make investment decisions']
```
