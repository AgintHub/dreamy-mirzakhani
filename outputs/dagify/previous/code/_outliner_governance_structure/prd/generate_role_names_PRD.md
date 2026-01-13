# generate_role_names PRD

## Description
Generates a list of role names appropriate for the specified legal entity type.


## Conceptual Info

This shim provides the foundational role nomenclature used by governance structure generation, ensuring consistent and relevant role titles across different legal entity types.

## Docstring

### Summary
Generate role names based on the provided legal entity type.

### Parameters

- **entity_type** (str): The legal entity type (e.g., 'LP', 'LLC', 'SICAV') for which role names are to be generated.

### Returns

List[str]: A list of role name strings relevant to the specified entity type.

### Raises

- ValueError: If the provided entity_type is not supported or recognized.
- TypeError: If entity_type is not a string.

### Examples

```python
>>> role_names = generate_role_names(entity_type='LLC')
['Member', 'Manager', 'Secretary']
```

```python
>>> role_names = generate_role_names(entity_type='SICAV')
['Manager', 'Director', 'Auditor']
```
