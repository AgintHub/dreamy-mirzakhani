# list_service_providers PRD

## Description
Identify mandatory external providers required to launch a hedge fund based on the selected legal entity type.


## Conceptual Info

Creates a mandatory service‑provider checklist that feeds into operational planning and budgeting.

## Docstring

### Summary
Generate a checklist of mandatory external service providers for a hedge fund, given the legal entity type selected earlier.

### Parameters

- **legal_entity_type** (str): The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).  Used only to contextualize the provider selection but not directly influencing the output values.

### Returns

dict: Dictionary with six string fields: prime_broker, fund_administrator, auditor, legal_counsel, compliance_consultant, custodian.

### Raises

- ValueError: If legal_entity_type is empty or not a recognized string.
- RuntimeError: If provider selection logic fails due to missing internal data.

### Examples

```python
>>> # Example 1: Simple LP structure
{
    "prime_broker": "Goldman Sachs",
    "fund_administrator": "KPMG",
    "auditor": "Deloitte",
    "legal_counsel": "Latham & Watkins",
    "compliance_consultant": "FATCA Compliance Partners",
    "custodian": "J.P. Morgan"
}
```
