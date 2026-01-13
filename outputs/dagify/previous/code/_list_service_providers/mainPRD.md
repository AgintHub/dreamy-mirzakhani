# _list_service_providers - Complete PRD Documentation

## Overview
PRDs for nodes in the '_list_service_providers' module.

## Table of Contents

- [validate_entity_type](#validate_entity_type)

- [get_provider_mapping_for_entity](#get_provider_mapping_for_entity)

- [extract_ordered_provider_names](#extract_ordered_provider_names)

- [extract_provider_functions](#extract_provider_functions)

- [validate_provider_completeness](#validate_provider_completeness)



---

## validate_entity_type

### Description
Validates the given entity type to ensure it meets specific requirements.

### Conceptual Info

The validate_entity_type shim function plays a crucial role in ensuring that the provided entity type is valid and consistent with the system's requirements. It acts as a gatekeeper, preventing invalid or unsupported entity types from being processed further.

### Docstring

**Summary:** Validates the given entity type to ensure it meets specific requirements.

**Parameters:**

- entity_type (str): The entity type to be validated (e.g., LP, LLC, SICAV)
**Returns:** str - Validation result or an error message

**Raises:**

- ValueError: When the input entity type is invalid or unsupported
- TypeError: When the input entity type is not a string
**Examples:**

```python
>>> validate_entity_type(entity_type='LLC')
'LLC' is a valid entity type
```

```python
>>> validate_entity_type(entity_type='InvalidType')
'InvalidType' is not a supported entity type
```



---

## get_provider_mapping_for_entity

### Description
This shim function retrieves a dictionary mapping of service providers for a given legal entity type.

### Conceptual Info

The get_provider_mapping_for_entity shim function acts as an interface to retrieve service provider mappings for different legal entity types, playing a crucial role in the system's operational workflow.

### Docstring

**Summary:** This function takes a legal entity type as input and returns a dictionary mapping of service providers, including their core functions, specific to the given entity type.

**Parameters:**

- entity_type (str): The legal entity type for which the service provider mapping is required, e.g., 'LP', 'LLC', 'SICAV'.
**Returns:** dict - A dictionary containing service provider names as keys and their respective core functions as values, specific to the given legal entity type.

**Raises:**

- ValueError: If the input entity type is not recognized or supported.
- TypeError: If the input entity type is not a string.
**Examples:**

```python
>>> provider_mapping = get_provider_mapping_for_entity(entity_type='LP')
>>> print(provider_mapping)
{'Prime Broker': 'Custody and Trading', 'Custodian': 'Asset Safekeeping', 'Fund Administrator': 'Accounting and Compliance'}
```

```python
>>> provider_mapping = get_provider_mapping_for_entity(entity_type='LLC')
>>> print(provider_mapping)
{'Legal Counsel': 'Regulatory Compliance', 'Compliance Consultant': 'Risk Management', 'Fund Administrator': 'Accounting and Tax'}
```



---

## extract_ordered_provider_names

### Description
This shim extracts the ordered list of provider names from a given provider mapping.

### Conceptual Info

The extract_ordered_provider_names shim is responsible for extracting a list of provider names in a specific order from a provider mapping, which is crucial for the list_service_providers function.

### Docstring

**Summary:** Extracts the ordered list of provider names from a given provider mapping.

**Parameters:**

- mapping (dict): A dictionary containing the provider mapping.
**Returns:** List[str] - A list of provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.

**Raises:**

- ValueError: If the provider mapping is invalid or missing required providers.
- TypeError: If the input provider mapping is not a dictionary.
**Examples:**

```python
>>> provider_mapping = {'prime_broker': 'Provider A', 'custodian': 'Provider B', 'fund_administrator': 'Provider C', 'legal_counsel': 'Provider D', 'compliance_consultant': 'Provider E'}
>>> ordered_providers = extract_ordered_provider_names(provider_mapping)
['Provider A', 'Provider B', 'Provider C', 'Provider D', 'Provider E']
```

```python
>>> invalid_mapping = 'invalid provider mapping'
>>> try:
...     extract_ordered_provider_names(invalid_mapping)
>>> except TypeError as e:
...     print(e)
Input provider mapping must be a dictionary.
```



---

## extract_provider_functions

### Description
Returns a list of core function descriptions for a given ordered list of service provider names based on a provider mapping dictionary.

### Conceptual Info

The shim translates a mapping of provider names to their function descriptions into an ordered list of functions that match the ordering of provider names supplied by the caller. This facilitates validation of provider completeness and integration with downstream nodes that consume structured provider information.

### Docstring

**Summary:** Retrieve ordered provider functions from a mapping.

**Parameters:**

- mapping (str): A JSON-serialised dictionary where keys are provider names and values are strings describing their core functions.
- providers (str): A JSON-serialised list of provider names in the desired order. The function will return a list of corresponding function descriptions.
**Returns:** str - A JSON-serialised list of function descriptions corresponding to the input providers list.

**Raises:**

- ValueError: Raised if a provider name in `providers` is missing from `mapping`.
- TypeError: Raised if either `mapping` or `providers` is not a valid JSON string or does not represent a dictionary/list respectively.
**Examples:**

```python
>>> import json
>>> mapping = json.dumps({"prime broker": "Execute trades", "custodian": "Safeguard assets"})
>>> providers = json.dumps(["prime broker", "custodian"])
>>> result = extract_provider_functions(mapping, providers)
>>> print(json.loads(result))
["Execute trades", "Safeguard assets"]
```

```python
>>> mapping = json.dumps({"prime broker": "Execute trades"})
>>> providers = json.dumps(["prime broker", "custodian"])
>>> extract_provider_functions(mapping, providers)
ValueError: Provider 'custodian' not found in mapping.
```



---

## validate_provider_completeness

### Description
Validates that the list of provider names and their corresponding functions are complete and correctly ordered.

### Conceptual Info

Ensures that each mandatory external service provider required for a chosen legal entity type is present with a corresponding function, preserving the predefined order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.

### Docstring

**Summary:** Checks that the provider names and their functions fully cover the required service stack and are in the correct order.

**Parameters:**

- providers (str): Comma‑separated string of provider names in the expected order.
- functions (str): Comma‑separated string of provider function descriptions matching the order of `providers`.
**Returns:** str - A success message 'Provider completeness validated.' when all checks pass.

**Raises:**

- ValueError: Raised if the number of providers does not equal the number of functions, or if any required provider is missing.
- TypeError: Raised if `providers` or `functions` are not strings.
**Examples:**

```python
>>> validate_provider_completeness(
...     providers='prime broker,custodian,fund administrator,legal counsel,compliance consultant',
...     functions='Brokerage services,Custodial services,Administration services,Legal advice,Regulatory compliance'"
              ")
'Provider completeness validated.'
```

```python
>>> validate_provider_completeness(
...     providers='prime broker,custodian',
...     functions='Brokerage services,Custodial services'"
              ")
ValueError: Missing required providers or functions.
```

