# _identify_regulatory_requirements - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_regulatory_requirements' module.

## Table of Contents

- [extract_jurisdiction_from_kwargs](#extract_jurisdiction_from_kwargs)

- [validate_legal_entity_and_jurisdiction](#validate_legal_entity_and_jurisdiction)

- [fetch_regulatory_requirements](#fetch_regulatory_requirements)

- [select_primary_requirement](#select_primary_requirement)

- [format_implementation_notes](#format_implementation_notes)



---

## extract_jurisdiction_from_kwargs

### Description
Extracts the jurisdiction from the provided keyword arguments.

### Conceptual Info

This shim function is responsible for extracting the jurisdiction from a set of keyword arguments. It plays a crucial role in validating and processing legal entity information.

### Docstring

**Summary:** Extracts the jurisdiction from the provided keyword arguments.

**Parameters:**

- kwargs (dict): A dictionary of keyword arguments containing the jurisdiction information.
**Returns:** str - The extracted jurisdiction as a string.

**Raises:**

- ValueError: When the jurisdiction is not found in the keyword arguments.
- TypeError: When the input keyword arguments are not of type dict.
**Examples:**

```python
>>> extract_jurisdiction_from_kwargs(country='USA', state='California')
>>> extract_jurisdiction_from_kwargs(jurisdiction='New York')
'California, USA'
'New York'
```



---

## validate_legal_entity_and_jurisdiction

### Description
Validates a legal entity type against a jurisdiction and returns a dictionary of normalized entity information.

### Conceptual Info

This shim abstracts the validation logic for legal entity types across jurisdictions, ensuring downstream modules receive consistent, normalized data.

### Docstring

**Summary:** Validate a legal entity type against a jurisdiction and return normalized entity information.

**Parameters:**

- entity_type (str): The raw legal entity type provided by the user (e.g., 'lp', 'LLC', 'SICAV').
- jurisdiction (str): The jurisdiction code or name where the entity will operate (e.g., 'US', 'DE', 'FR').
**Returns:** str - A JSON-formatted string containing `legal_entity_type` and `jurisdiction` keys with normalized values.

**Raises:**

- ValueError: If the entity type is not supported in the specified jurisdiction.
- TypeError: If either `entity_type` or `jurisdiction` is not a string.
**Examples:**

```python
>>> result = validate_legal_entity_and_jurisdiction(entity_type='LLC', jurisdiction='US')
>>> print(result)
"{\"legal_entity_type\": \"LLC\", \"jurisdiction\": \"US\"}"
```

```python
>>> try:
...     validate_legal_entity_and_jurisdiction(entity_type='XYZ', jurisdiction='US')
>>> except ValueError as e:
...     print(e)
"Entity type 'XYZ' is not supported in jurisdiction 'US'."
```



---

## fetch_regulatory_requirements

### Description
Fetches a list of regulatory requirements for a given entity type and jurisdiction.

### Conceptual Info

This shim function is responsible for fetching a list of regulatory requirements for a given entity type and jurisdiction. It serves as a placeholder for the actual implementation, which will be defined in the future.

### Docstring

**Summary:** Fetches a list of regulatory requirements for a given entity type and jurisdiction.

**Parameters:**

- entity_type (str): The type of entity (e.g., LP, LLC, SICAV).
- jurisdiction (str): The jurisdiction for which to fetch regulatory requirements.
**Returns:** List[dict] - A list of dictionaries containing regulatory requirements. Each dictionary should have the following keys: 'requirement', 'agency_citation', 'implementation_notes'.

**Raises:**

- ValueError: When input validation fails (e.g., invalid entity type or jurisdiction).
- TypeError: When input types are incorrect (e.g., entity_type or jurisdiction is not a string).
**Examples:**

```python
>>> fetch_regulatory_requirements(entity_type='LP', jurisdiction='US')
>>> -> [{'requirement': 'File Form D', 'agency_citation': 'SEC', 'implementation_notes': ['Note 1', 'Note 2']}]
[{'requirement': 'File Form D', 'agency_citation': 'SEC', 'implementation_notes': ['Note 1', 'Note 2']}]
```

```python
>>> fetch_regulatory_requirements(entity_type='LLC', jurisdiction='CA')
>>> -> [{'requirement': 'File Statement of Information', 'agency_citation': 'California Secretary of State', 'implementation_notes': ['Note 3', 'Note 4']}]
[{'requirement': 'File Statement of Information', 'agency_citation': 'California Secretary of State', 'implementation_notes': ['Note 3', 'Note 4']}]
```



---

## select_primary_requirement

### Description
Selects the primary regulatory requirement from a list of requirements.

### Conceptual Info

The select_primary_requirement shim is used to identify the most critical regulatory requirement from a list of requirements. This is essential in determining the primary compliance obligation for a given legal entity and jurisdiction.

### Docstring

**Summary:** Selects the primary regulatory requirement from a list of requirements based on a set of predefined criteria.

**Parameters:**

- requirements_list (str): A list of regulatory requirements in JSON format.
**Returns:** str - The primary regulatory requirement in JSON format.

**Raises:**

- ValueError: When the input list is empty or invalid.
- TypeError: When the input is not a string or the output is not a string.
**Examples:**

```python
>>> import json
>>> requirements_list = '[{"requirement": "req1"}, {"requirement": "req2"}]'
>>> select_primary_requirement(requirements_list=json.loads(requirements_list))
{"requirement": "req1"}
```

```python
>>> import json
>>> requirements_list = '[{"requirement": "req3"}, {"requirement": "req4"}]'
>>> select_primary_requirement(requirements_list=json.loads(requirements_list))
{"requirement": "req3"}
```



---

## format_implementation_notes

### Description
This shim function formats the implementation notes for regulatory requirements into a standardized list of strings.

### Conceptual Info

The format_implementation_notes shim is responsible for taking raw implementation notes and converting them into a standardized format that can be easily consumed by the rest of the system.

### Docstring

**Summary:** Formats the implementation notes for regulatory requirements into a list of strings.

**Parameters:**

- raw_notes (str): The raw implementation notes to be formatted.
**Returns:** List[str] - A list of formatted implementation notes.

**Raises:**

- ValueError: If the input raw_notes is not a string.
- TypeError: If the input raw_notes is not a string or cannot be converted to a list of strings.
**Examples:**

```python
>>> formatted_notes = format_implementation_notes("Note 1, Note 2")
["Note 1", "Note 2"]
```

```python
>>> formatted_notes = format_implementation_notes("Single Note")
["Single Note"]
```

