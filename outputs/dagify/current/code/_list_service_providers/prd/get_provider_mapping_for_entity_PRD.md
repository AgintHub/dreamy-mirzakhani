# get_provider_mapping_for_entity PRD

## Description
Retrieves a JSON string mapping mandatory service provider roles to specific provider names and their core functions for a validated legal entity type.


## Conceptual Info

This shim supplies the mapping between required service provider roles (prime broker, custodian, fund administrator, legal counsel, compliance consultant) and concrete provider identifiers along with their core functions for a specified legal entity type.

## Docstring

### Summary
Returns a JSON-formatted mapping of provider roles to provider details for the given entity type.

### Parameters

- **entity_type** (str): The validated legal entity type (e.g., 'LLC', 'LP', 'SICAV').

### Returns

str: A JSON string where keys are provider roles and values are dictionaries containing provider names and their core functions.

### Raises

- ValueError: If the provided entity_type is not supported or recognized.
- TypeError: If entity_type is not a string.

### Examples

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
