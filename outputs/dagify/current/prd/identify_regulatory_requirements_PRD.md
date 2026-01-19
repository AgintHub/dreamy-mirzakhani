# identify_regulatory_requirements PRD

## Description
Generates a list of the key regulatory filings or registrations that the chosen legal entity must complete, along with the governing bodies responsible for each.


## Conceptual Info

This node takes the legal entity type chosen earlier in the workflow and returns a concise mapping of the most important regulatory filings along with the authorities that oversee those filings. The output feeds directly into the compliance checklist generation.

## Docstring

### Summary
Determine the regulatory filings required for a selected legal entity and identify the corresponding governing bodies.

### Parameters

- **legal_entity_type** (str): The legal structure selected for the hedge fund (e.g., 'LP', 'LLC', 'SICAV').

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists:

1. `requirements`: the names of the primary filings or registrations.
2. `governing_bodies`: the names of the authorities that mandate each filing.

### Raises

- ValueError: If `legal_entity_type` is empty or not among the supported entity types.
- KeyError: If the internal mapping for the provided `legal_entity_type` cannot be found.

### Examples

```python
>>> requirements, governing_bodies = identify_regulatory_requirements('LLC')
(['DBS Filing', 'SEC Form D'], ['FINRA', 'SEC'])
```

```python
>>> requirements, governing_bodies = identify_regulatory_requirements('SICAV')
(['FCA Registration', 'Securities and Investment Fund Management Authority Filing'], ['FCA', 'SIFMA'])
```
