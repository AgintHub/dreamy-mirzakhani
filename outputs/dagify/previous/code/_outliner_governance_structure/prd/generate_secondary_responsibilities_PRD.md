# generate_secondary_responsibilities PRD

## Description
This shim generates secondary responsibilities for given role names based on a specified legal entity type.


## Conceptual Info

The generate_secondary_responsibilities shim is designed to produce secondary responsibilities associated with specific roles within a legal entity, playing a crucial role in outlining governance structures.

## Docstring

### Summary
Generates a list of secondary responsibilities for each role based on the provided legal entity type and role names.

### Parameters

- **entity_type** (str): The type of legal entity (e.g., LP, LLC, SICAV).
- **role_names** (str): A string containing names of roles separated by commas or any other delimiter.
