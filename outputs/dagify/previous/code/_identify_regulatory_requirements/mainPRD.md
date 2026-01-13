# _identify_regulatory_requirements - Complete PRD Documentation

## Overview
PRDs for nodes in the '_identify_regulatory_requirements' module.

## Table of Contents

- [validate_legal_entity_type](#validate_legal_entity_type)

- [extract_jurisdiction_from_kwargs](#extract_jurisdiction_from_kwargs)

- [validate_jurisdiction](#validate_jurisdiction)

- [get_regulatory_requirements_mapping](#get_regulatory_requirements_mapping)

- [extract_primary_requirement](#extract_primary_requirement)

- [extract_agency_citation](#extract_agency_citation)

- [generate_implementation_notes](#generate_implementation_notes)



---

## validate_legal_entity_type

### Description
Validates a given legal entity type to ensure it meets specific criteria.

### Conceptual Info

The validate_legal_entity_type shim function plays a crucial role in ensuring that the provided legal entity type is valid and recognized within the system. This function is essential for maintaining data consistency and accuracy.

### Docstring

**Summary:** Validates a given legal entity type to ensure it meets specific criteria.

**Parameters:**

- entity_type (str): The legal entity type to be validated (e.g., LP, LLC, SICAV).
**Returns:** str - The validated legal entity type.

**Raises:**

- ValueError: When the input entity type is not recognized or does not meet the required criteria.
- TypeError: When the input entity type is not a string.
**Examples:**

```python
>>> validate_legal_entity_type(entity_type='LLC')
'LLC'
```

```python
>>> validate_legal_entity_type(entity_type='Invalid Entity Type')
raises ValueError
```



---

## extract_jurisdiction_from_kwargs

### Description
Extracts the jurisdiction value from keyword arguments passed to regulatory requirement functions.

### Conceptual Info

In the regulatory requirement workflow, the jurisdiction is supplied via keyword arguments; this shim standardizes retrieval of that value and validates its presence before further processing.

### Docstring

**Summary:** Retrieve the jurisdiction string from a set of keyword arguments used in regulatory requirement functions.

**Parameters:**

- kwargs (dict): A mapping of keyword arguments that should include a key named 'jurisdiction' holding a string value.
**Returns:** str - The jurisdiction name extracted from `kwargs`.

**Raises:**

- ValueError: Raised when the 'jurisdiction' key is missing from `kwargs` or its value is empty.
- TypeError: Raised when the value associated with the 'jurisdiction' key is not a string.
**Examples:**

```python
>>> result = extract_jurisdiction_from_kwargs(jurisdiction="France")
>>> print(result)
"France"
```

```python
>>> try:
...     extract_jurisdiction_from_kwargs(country="Italy")
>>> except ValueError as e:
...     print(e)
"Missing 'jurisdiction' key in keyword arguments."
```



---

## validate_jurisdiction

### Description
Validates a jurisdiction string and returns a standardized jurisdiction code or raises an error if invalid

### Conceptual Info

The `validate_jurisdiction` shim ensures that the jurisdiction value supplied to downstream regulatory logic is recognized, correctly formatted, and mapped to a canonical code, preventing downstream errors and enabling consistent mapping to regulatory requirements.

### Docstring

**Summary:** Validate a jurisdiction string and return a canonical jurisdiction code.

**Parameters:**

- jurisdiction (str): The jurisdiction to be validated, typically provided by user input or extracted from context. It may be an abbreviated code, full name, or mixed case.
**Returns:** str - A normalized jurisdiction code (e.g., 'DE', 'GB', 'US') that is guaranteed to exist in the system’s jurisdiction registry.

**Raises:**

- ValueError: Raised when the jurisdiction string does not match any known jurisdiction in the registry.
- TypeError: Raised when the jurisdiction argument is not a string.
**Examples:**

```python
>>> validate_jurisdiction('United States')
'US'
```

```python
>>> validate_jurisdiction('de')
'DE'
```

```python
>>> validate_jurisdiction('UnknownCountry')
ValueError: Unknown jurisdiction: UnknownCountry
```



---

## get_regulatory_requirements_mapping

### Description
Retrieves a dictionary mapping of regulatory requirements for a given legal entity type and jurisdiction.

### Conceptual Info

This shim encapsulates the logic needed to fetch the regulatory requirement mapping for a specified legal entity type and jurisdiction, acting as a bridge between higher‑level business logic and the underlying data source.

### Docstring

**Summary:** Return a mapping of regulatory requirements for a given entity type and jurisdiction.

**Parameters:**

- entity_type (str): Canonical name of the legal entity type (e.g., 'LLC', 'SICAV', 'LP').
- jurisdiction (str): Two‑letter ISO country code or jurisdiction identifier (e.g., 'US', 'DE').
**Returns:** str - A JSON string representation of a dictionary where keys are requirement identifiers and values are dictionaries containing 'requirement', 'agency_citation', and optional 'implementation_notes'.

**Raises:**

- ValueError: Raised if the entity_type or jurisdiction is unsupported or missing.
- TypeError: Raised if entity_type or jurisdiction is not a string.
**Examples:**

```python
>>> mapping = get_regulatory_requirements_mapping(entity_type='LLC', jurisdiction='US')
>>> print(mapping)
{\n  "SEC_Registration": {\n    "requirement": "SEC Form 10-K filing",\n    "agency_citation": "SEC 10-K",\n    "implementation_notes": ["Prepare annual financial statements", "Submit via EDGAR"]\n  }\n}
```

```python
>>> try:
...     get_regulatory_requirements_mapping(entity_type='INVALID', jurisdiction='US')
>>> except ValueError as e:
...     print(e)
"Unsupported entity type: INVALID"
```



---

## extract_primary_requirement

### Description
Extracts the primary regulatory requirement from a given regulatory mapping.

### Conceptual Info

The extract_primary_requirement shim function plays a crucial role in identifying the primary regulatory requirement from a given regulatory mapping. This function is essential in determining the specific regulatory filing or registration required.

### Docstring

**Summary:** Extracts the primary regulatory requirement from a given regulatory mapping.

**Parameters:**

- mapping (str): The regulatory mapping from which to extract the primary requirement.
**Returns:** str - The primary regulatory requirement.

**Raises:**

- ValueError: When the input mapping is invalid or empty.
- TypeError: When the input mapping is not a string.
**Examples:**

```python
>>> regulatory_mapping = {'primary_requirement': 'File Form 10-K with the SEC', 'agency_citation': 'SEC'}
>>> extract_primary_requirement(mapping=regulatory_mapping)
'File Form 10-K with the SEC'
```

```python
>>> regulatory_mapping = {}
>>> extract_primary_requirement(mapping=regulatory_mapping)
''
```



---

## extract_agency_citation

### Description
Extracts the agency citation from a given regulatory mapping.

### Conceptual Info

The extract_agency_citation shim function is responsible for extracting the agency citation from a given regulatory mapping. This function plays a crucial role in identifying regulatory requirements and providing the necessary citation for compliance.

### Docstring

**Summary:** Extracts the agency citation from a given regulatory mapping.

**Parameters:**

- mapping (str): The input regulatory mapping.
**Returns:** str - The extracted agency citation.

**Raises:**

- ValueError: When the input mapping is invalid or empty.
- TypeError: When the input mapping is not a string.
**Examples:**

```python
>>> extract_agency_citation(mapping={'agency_citation': 'Example Citation'})
'Example Citation'
```

```python
>>> extract_agency_citation(mapping={})
''
```



---

## generate_implementation_notes

### Description
Generates concise implementation or compliance notes for a specified legal entity type, jurisdiction, and regulatory requirement.

### Conceptual Info

This shim creates user-friendly, actionable guidance for compliance officers, translating regulatory requirements into clear steps that can be followed within the specified entity and jurisdiction context.

### Docstring

**Summary:** Generate one or two short notes that explain how to implement or comply with a given regulatory requirement for a specified legal entity type and jurisdiction.

**Parameters:**

- entity_type (str): The legal entity type (e.g., 'LLC', 'LP', 'SICAV').
- jurisdiction (str): The regulatory jurisdiction or country where the entity operates.
- requirement (str): The specific regulatory filing, registration, or compliance action required.
**Returns:** List[str] - A list containing one or two brief textual notes that describe actionable steps to implement or comply with the requirement.

**Raises:**

- ValueError: Raised if any of the input strings are empty or None.
- TypeError: Raised if any input is not of type `str`.
**Examples:**

```python
>>> notes = generate_implementation_notes(
...     entity_type='LLC',
...     jurisdiction='United States',
...     requirement='File annual report with the Secretary of State')
>>> print(notes)
['Submit the annual report by the deadline indicated on the Secretary of State website.', 'Ensure all shareholders’ information is current before filing.']
```

```python
>>> notes = generate_implementation_notes(
...     entity_type='SICAV',
...     jurisdiction='Switzerland',
...     requirement='Register with FINMA under Article 3.1')
>>> print(notes)
['Complete the FINMA registration form and submit required financial statements.', 'Maintain the register of beneficial owners as per Article 3.1.']
```

