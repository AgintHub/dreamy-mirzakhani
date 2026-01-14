# assign_stage_responsibilities PRD

## Description
Assigns responsible parties to each operational stage based on the provided list of stages and service provider names.


## Conceptual Info

This shim provides the core logic for determining which organization (in‑house or a specific vendor) is accountable for each stage in the investment lifecycle, enabling downstream nodes to flag vendor involvement and generate stage descriptions.

## Docstring

### Summary
Map operational stages to responsible parties using the fixed provider order.

### Parameters

- **stages** (str): An ordered, comma‑separated string of operational stage names.
- **providers** (str): An ordered, comma‑separated string of mandatory external service provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.

### Returns

str: A comma‑separated string of responsible parties, one for each stage, matching the input order.

### Raises

- ValueError: Raised if the number of stages does not match the number of providers.
- TypeError: Raised if either input is not a string.

### Examples

```python
>>> stages = 'Idea Generation,Structuring,Compliance,Execution,Settlement'
>>> providers = 'Prime Broker,Custodian,Fund Administrator,Legal Counsel,Compliance Consultant'
>>> result = assign_stage_responsibilities(stages, providers)
>>> print(result)
'Prime Broker,Custodian,Fund Administrator,Legal Counsel,Compliance Consultant'
```

```python
>>> assign_stage_responsibilities('Idea Generation,Execution', 'Prime Broker')
ValueError: Number of stages (2) does not match number of providers (1).
```
