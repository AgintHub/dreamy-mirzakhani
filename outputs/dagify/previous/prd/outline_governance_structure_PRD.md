# outline_governance_structure PRD

## Description
Define the core management and oversight framework for the hedge fund by enumerating five key leadership positions and summarizing each role’s primary duty in a concise statement.


## Conceptual Info

This node establishes the governance skeleton of the hedge fund, mapping the legal entity type to a clear set of leadership roles and their responsibilities. The output feeds into both the pitch deck (to demonstrate institutional credibility) and the hiring plan (to identify staffing requirements).

## Docstring

### Summary
Generate a list of five leadership roles and a one‑sentence description of each duty for a hedge fund, based on the chosen legal entity type.

### Parameters

- **legal_entity_type** (str): The legal entity type selected in the choose_legal_entity_type node (e.g., LP, LLC, SICAV).

### Returns

Dict[str, List[str]]: A dictionary with two keys: 'roles', a list of role names, and 'duties', a list of one‑sentence duty statements in the same order.

### Raises

- ValueError: Raised if legal_entity_type is not one of the supported types (LP, LLC, SICAV).
- KeyError: Raised if the internal role mapping for the provided entity type is missing.

### Examples

```python
>>> output = outline_governance_structure('LP')
{
  "roles": ["General Partner (GP)", "Chief Investment Officer (CIO)", "Chief Financial Officer (CFO)", "Chief Operating Officer (COO)", "Chief Compliance Officer (CCO)"],
  "duties": ["Oversee overall fund strategy and execution.", "Set investment mandates and monitor performance.", "Manage capital structure, budgeting, and reporting.", "Coordinate day‑to‑day operations and technology.", "Ensure regulatory compliance and risk oversight."]
}
```

```python
>>> output = outline_governance_structure('SICAV')
{
  "roles": ["President", "Chief Investment Officer (CIO)", "Chief Financial Officer (CFO)", "Chief Operating Officer (COO)", "Chief Risk Officer (CRO)"],
  "duties": ["Represent the SICAV to regulators and investors.", "Define and monitor investment strategies.", "Oversee financial reporting and capital management.", "Lead operational efficiency and IT governance.", "Develop and enforce risk policies across the fund."]
}
```
