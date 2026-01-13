# outliner_governance_structure PRD

## Description
Define internal authority framework


## Conceptual Info

Generates a structured governance chart that specifies key internal roles, their core duties, and the decision‑making authority each holds within the hedge fund.

## Docstring

### Summary
Creates a governance framework for a hedge fund based on the selected legal entity type.

### Parameters

- **legal_entity_type** (str): The legal entity type chosen for the fund (e.g., LP, LLC, SICAV).

### Returns

dict: Dictionary containing five lists: role_names, role_responsibility_1, role_responsibility_2, role_responsibility_3, and role_authority_scope.

### Raises

- ValueError: If `legal_entity_type` is an empty string or not among the supported entity types.

### Examples

```python
>>> outliner_governance_structure('LP')
{
  'role_names': ['GP', 'Investment Manager', 'Compliance Officer', 'Chief Operating Officer', 'Investor Relations Officer'],
  'role_responsibility_1': ['Oversee overall fund strategy', 'Develop trade ideas', 'Ensure regulatory compliance', 'Manage day‑to‑day operations', 'Maintain investor communications'],
  'role_responsibility_2': ['Allocate capital', 'Approve trade execution', 'Monitor AML/KYC', 'Coordinate vendor relationships', 'Distribute performance reports'],
  'role_responsibility_3': ['Set performance targets', 'Conduct risk reviews', 'Draft compliance policies', 'Report to board', 'Handle investor inquiries'],
  'role_authority_scope': ['Strategic decisions', 'Trade approval up to $10M', 'Compliance approvals', 'Operational budgets', 'Investor disclosures']
}
```

```python
>>> outliner_governance_structure('LLC')
{
  'role_names': ['GP', 'Investment Manager', 'Compliance Officer', 'Chief Financial Officer', 'Investor Relations Officer'],
  'role_responsibility_1': ['Set investment mandate', 'Identify market opportunities', 'Maintain regulatory filings', 'Oversee financial reporting', 'Engage investors'],
  'role_responsibility_2': ['Allocate capital within limits', 'Approve execution plans', 'Implement AML controls', 'Manage budgets', 'Provide performance updates'],
  'role_responsibility_3': ['Define risk appetite', 'Conduct compliance audits', 'Prepare annual reports', 'Ensure tax compliance', 'Coordinate investor meetings'],
  'role_authority_scope': ['Strategic direction', 'Trade approvals up to $8M', 'Compliance approvals', 'Financial oversight', 'Investor disclosure']
}
```
