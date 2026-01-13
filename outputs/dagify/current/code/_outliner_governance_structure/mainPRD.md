# _outliner_governance_structure - Complete PRD Documentation

## Overview
PRDs for nodes in the '_outliner_governance_structure' module.

## Table of Contents

- [validate_legal_entity_type](#validate_legal_entity_type)

- [get_governance_template_for_entity](#get_governance_template_for_entity)

- [extract_role_names](#extract_role_names)

- [extract_responsibilities](#extract_responsibilities)

- [extract_authority_scopes](#extract_authority_scopes)



---

## validate_legal_entity_type

### Description
Validates that the provided legal entity type is supported and returns a confirmation string.

### Conceptual Info

This shim ensures that downstream nodes receive a verified legal entity type, preventing propagation of invalid values through the governance structure pipeline.

### Docstring

**Summary:** Validate the supplied legal entity type against an internal list of supported types and return a confirmation string.

**Parameters:**

- entity_type (str): The legal entity type to validate (e.g., 'LP', 'LLC', 'SICAV').
**Returns:** str - A confirmation string such as "Entity type 'LLC' validated."

**Raises:**

- ValueError: If the entity_type is not in the list of supported legal entity types.
- TypeError: If entity_type is not a string.
**Examples:**

```python
>>> validate_legal_entity_type('LLC')
"Entity type 'LLC' validated."
```

```python
>>> validate_legal_entity_type('Unknown')
ValueError: Unsupported entity type 'Unknown'.
```



---

## get_governance_template_for_entity

### Description
Returns a JSON‐serialisable governance template dictionary for a given legal entity type.

### Conceptual Info

This shim supplies the governance template that outlines the structure and authority of roles for a specified legal entity. It is used by the outliner_governance_structure node to extract role names, responsibilities, and authority scopes.

### Docstring

**Summary:** Retrieve a governance template for the specified legal entity type.

**Parameters:**

- entity_type (str): The legal entity type for which the governance template is requested (e.g., 'LLC', 'LP', 'SICAV').
**Returns:** str - A JSON string that can be deserialised into a dict with keys: 'role_names', 'responsibilities_level_1', 'responsibilities_level_2', 'responsibilities_level_3', and 'authority_scopes'.

**Raises:**

- ValueError: If the requested entity_type is not supported.
- TypeError: If entity_type is not a string.
**Examples:**

```python
>>> template_json = get_governance_template_for_entity(entity_type='LLC')
>>> print(template_json)
{\n  \"role_names\": [\"Director\", \"Secretary\"],\n  \"responsibilities_level_1\": [\"Strategic Oversight\", \"Compliance\"],\n  \"responsibilities_level_2\": [\"Financial Reporting\", \"Risk Management\"],\n  \"responsibilities_level_3\": [\"Operational Decision-Making\", \"Policy Development\"],\n  \"authority_scopes\": [\"Full\", \"Limited\"]\n}
```

```python
>>> try:
...     get_governance_template_for_entity(entity_type='UnknownEntity')
>>> except ValueError as e:
...     print(e)
"Unsupported entity type: UnknownEntity"
```



---

## extract_role_names

### Description
Extracts role names from a given governance template.

### Conceptual Info

The extract_role_names shim function is responsible for parsing a governance template and extracting the role names defined within it.

### Docstring

**Summary:** Extracts role names from a given governance template.

**Parameters:**

- template (str): The governance template to extract role names from. This should be a string representation of a data structure containing role information.
**Returns:** List[str] - A list of role names extracted from the template.

**Raises:**

- ValueError: When the input template is invalid or cannot be parsed.
- TypeError: When the input template is not a string.
**Examples:**

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



---

## extract_responsibilities

### Description
Extracts a list of responsibilities for a given responsibility level from a governance template.

### Conceptual Info

This shim parses a governance template dictionary to retrieve responsibilities assigned to each role at a specified hierarchical level, facilitating downstream generation of role-based governance documentation.

### Docstring

**Summary:** Return a list of responsibilities for a specified level from a governance template.

**Parameters:**

- template (str): A JSON string representation of the governance template dictionary.
- responsibility_level (str): The responsibility level to extract (e.g., '1', '2', or '3').
**Returns:** list - A list of strings, each representing a responsibility for the requested level.

**Raises:**

- ValueError: Raised if the responsibility_level is not one of the expected levels ('1', '2', '3').
- KeyError: Raised if the template does not contain the expected keys for responsibilities.
- TypeError: Raised if template is not a valid JSON string or if responsibility_level is not a string.
**Examples:**

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



---

## extract_authority_scopes

### Description
The extract_authority_scopes shim extracts authority scopes from a given governance template.

### Conceptual Info

The extract_authority_scopes shim is responsible for extracting authority scopes from a governance template, which is crucial for defining roles and responsibilities within an organization.

### Docstring

**Summary:** Extracts authority scopes from a given governance template.

**Parameters:**

- template (str): The governance template as a string from which authority scopes will be extracted.
**Returns:** List[str] - A list of authority scopes extracted from the governance template.

**Raises:**

- ValueError: If the input template is invalid or does not contain authority scopes.
- TypeError: If the input template is not a string.
**Examples:**

```python
>>> authority_scopes = extract_authority_scopes(template='{"roles": [{"name": "CEO", "authority": "Financial"}, {"name": "CTO", "authority": "Technical"}]}')
["Financial", "Technical"]
```

```python
>>> authority_scopes = extract_authority_scopes(template='Invalid template')
ValueError: Invalid template
```

