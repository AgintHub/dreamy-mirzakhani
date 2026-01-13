# _list_service_providers - Complete PRD Documentation

## Overview
PRDs for nodes in the '_list_service_providers' module.

## Table of Contents

- [validate_legal_entity_type](#validate_legal_entity_type)

- [get_provider_mapping_for_entity](#get_provider_mapping_for_entity)

- [extract_ordered_provider_names](#extract_ordered_provider_names)

- [extract_provider_functions](#extract_provider_functions)

- [validate_provider_completeness](#validate_provider_completeness)



---

## validate_legal_entity_type

### Description
Validates a given legal entity type and returns a standardized string representation.

### Conceptual Info

The validate_legal_entity_type shim function plays a crucial role in standardizing and validating legal entity types, ensuring consistency across the system.

### Docstring

**Summary:** Validates a given legal entity type and returns a standardized string representation.

**Parameters:**

- entity_type (str): The input legal entity type to be validated (e.g., LP, LLC, SICAV)
**Returns:** str - The validated legal entity type

**Raises:**

- ValueError: When the input entity type is not recognized or is invalid
- TypeError: When the input entity type is not a string
**Examples:**

```python
>>> validate_legal_entity_type(entity_type='LLC')
'LLC'
```

```python
>>> validate_legal_entity_type(entity_type=' invalid_type')
raises ValueError
```



---

## get_provider_mapping_for_entity

### Description
Retrieves a JSON string mapping mandatory service provider roles to specific provider names and their core functions for a validated legal entity type.

### Conceptual Info

This shim supplies the mapping between required service provider roles (prime broker, custodian, fund administrator, legal counsel, compliance consultant) and concrete provider identifiers along with their core functions for a specified legal entity type.

### Docstring

**Summary:** Returns a JSON-formatted mapping of provider roles to provider details for the given entity type.

**Parameters:**

- entity_type (str): The validated legal entity type (e.g., 'LLC', 'LP', 'SICAV').
**Returns:** str - A JSON string where keys are provider roles and values are dictionaries containing provider names and their core functions.

**Raises:**

- ValueError: If the provided entity_type is not supported or recognized.
- TypeError: If entity_type is not a string.
**Examples:**

```python
>>> output = get_provider_mapping_for_entity('LLC')
>>> print(output)
"{\n  \"prime_broker\": {\"name\": \"PrimeBrokerInc\", \"function\": \"Execution and clearing\"},\n  \"custodian\": {\"name\": \"CustodianLtd\", \"function\": \"Safekeeping and settlement\"},\n  \"fund_administrator\": {\"name\": \"AdminCorp\", \"function\": \"Reporting and NAV calculation\"},\n  \"legal_counsel\": {\"name\": \"LawPartners\", \"function\": \"Legal and regulatory advice\"},\n  \"compliance_consultant\": {\"name\": \"ComplianceCo\", \"function\": \"Risk and compliance management\"}\n}"
```

```python
>>> output = get_provider_mapping_for_entity('SICAV')
>>> print(output)
"{\n  \"prime_broker\": {\"name\": \"SicavPrime\", \"function\": \"Execution and clearing\"},\n  \"custodian\": {\"name\": \"SicavCustodian\", \"function\": \"Safekeeping and settlement\"},\n  \"fund_administrator\": {\"name\": \"SicavAdmin\", \"function\": \"Reporting and NAV calculation\"},\n  \"legal_counsel\": {\"name\": \"SicavLegal\", \"function\": \"Legal and regulatory advice\"},\n  \"compliance_consultant\": {\"name\": \"SicavCompliance\", \"function\": \"Risk and compliance management\"}\n}"
```



---

## extract_ordered_provider_names

### Description
Return a list of mandatory external service provider names in the required order based on an entity‑specific provider mapping.

### Conceptual Info

The shim transforms a provider mapping dictionary into a deterministic, ordered list of provider names required for downstream validation and processing.

### Docstring

**Summary:** Extracts the ordered list of mandatory external service provider names from a provider mapping dictionary.

**Parameters:**

- mapping (dict): A dictionary where keys are provider identifiers and values are provider details. The dictionary must contain entries for each of the five mandatory providers: 'prime_broker', 'custodian', 'fund_administrator', 'legal_counsel', and 'compliance_consultant'.
**Returns:** List[str] - A list of provider names in the exact order: ['prime broker', 'custodian', 'fund administrator', 'legal counsel', 'compliance consultant'].

**Raises:**

- ValueError: If any of the required provider keys are missing from the mapping.
- TypeError: If the input mapping is not a dictionary or contains non‑string values.
**Examples:**

```python
>>> sample_mapping = {
...     'prime_broker': {'name': 'PrimeX'},
...     'custodian': {'name': 'CustodialY'},
...     'fund_administrator': {'name': 'AdminZ'},
...     'legal_counsel': {'name': 'LegalA'},
...     'compliance_consultant': {'name': 'ComplianceB'}
>>> }
[\n    'prime broker',\n    'custodian',\n    'fund administrator',\n    'legal counsel',\n    'compliance consultant'\n]
```

```python
>>> incomplete_mapping = {
...     'prime_broker': {'name': 'PrimeX'},
...     'custodian': {'name': 'CustodialY'}
>>> }
ValueError: Missing required provider keys: fund_administrator, legal_counsel, compliance_consultant
```



---

## extract_provider_functions

### Description
Retrieves a list of provider function descriptions matching the order of provider names from a mapping dictionary.

### Conceptual Info

The shim fetches the functional descriptions of external service providers from a mapping, ensuring the order aligns with the provider list to support downstream validation and reporting.

### Docstring

**Summary:** Return a list of provider function descriptions that correspond to the supplied provider names, preserving order.

**Parameters:**

- mapping (dict): Dictionary mapping provider names to their function descriptions. Keys are provider names; values are strings describing the provider’s core functions.
- provider_names (list[str]): Ordered list of provider names for which function descriptions are required.
**Returns:** list[str] - A list of function description strings, each matching the provider name at the same index in provider_names.

**Raises:**

- KeyError: If a provider name in provider_names is not present in the mapping dictionary.
- ValueError: If the mapping values are not strings or if provider_names is empty.
**Examples:**

```python
>>> mapping = {
...     'prime broker': 'Execute trades and manage securities',
...     'custodian': 'Safeguard assets and provide custody services',
...     'fund administrator': 'Handle accounting and investor reporting',
...     'legal counsel': 'Provide legal advice and compliance oversight',
...     'compliance consultant': 'Ensure regulatory compliance and risk management'}
>>> provider_names = ['prime broker', 'custodian', 'fund administrator', 'legal counsel', 'compliance consultant']
>>> functions = extract_provider_functions(mapping, provider_names)
['Execute trades and manage securities', 'Safeguard assets and provide custody services', 'Handle accounting and investor reporting', 'Provide legal advice and compliance oversight', 'Ensure regulatory compliance and risk management']
```

```python
>>> mapping = {'prime broker': 'Execute trades'}
>>> extract_provider_functions(mapping, ['custodian'])
KeyError: 'custodian'
```



---

## validate_provider_completeness

### Description
Validates the completeness of provider information.

### Conceptual Info

The shim function validate_provider_completeness checks if the provided provider information is complete and valid.

### Docstring

**Summary:** Validates the completeness of provider information.

**Parameters:**

- provider_names (str): List of provider names
- provider_functions (str): List of core function descriptions for each provider
**Returns:** str - Output of the validation process

**Raises:**

- ValueError: When provider information is incomplete or invalid
- TypeError: When input types are incorrect
**Examples:**

```python
>>> validate_provider_completeness(provider_names=['prime broker', 'custodian'], provider_functions=['function 1', 'function 2'])
'Validation successful'
```

```python
>>> validate_provider_completeness(provider_names=['prime broker'], provider_functions=['function 1', 'function 2'])
'Validation failed: incomplete provider information'
```

