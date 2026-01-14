# list_service_providers PRD

## Description
Identify required third‑party vendors


## Conceptual Info

Collects a concise list of external vendor categories indispensable for a hedge fund’s operation, ensuring subsequent nodes receive a standardized taxonomy for cost estimation and workflow mapping.

## Docstring

### Summary
Generate a fixed list of service provider categories needed to launch a hedge fund.

### Parameters

- **legal_entity_type** (str): The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).

### Returns

dict: Dictionary containing a single key `service_provider_categories` mapped to a list of strings.

### Raises

- ValueError: If `legal_entity_type` is empty or not one of the supported types (LP, LLC, SICAV).

### Examples

```python
>>> list_service_providers('LP')
{'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit Firm', 'IT Service Provider']}
```

```python
>>> list_service_providers('LLC')
{'service_provider_categories': ['Prime Broker', 'Custodian', 'Compliance Consultant', 'Transfer Agent', 'Fund Administrator', 'Legal Counsel', 'Audit Firm', 'IT Service Provider']}
```
