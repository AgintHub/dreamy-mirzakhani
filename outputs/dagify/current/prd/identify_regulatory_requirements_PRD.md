# identify_regulatory_requirements PRD

## Description
Lists mandatory compliance obligations for a hedge fund based on the chosen legal entity and jurisdiction.


## Conceptual Info

This node gathers the regulatory filing requirements that must be met by the hedge fund once its legal structure is chosen. The output is a concise, jurisdiction‑specific checklist that downstream compliance and governance modules can map to internal controls.

## Docstring

### Summary
Generate a list of mandatory regulatory filings for the selected legal entity and jurisdiction.

### Parameters

- **legal_entity_type** (str): The legal entity type chosen for the hedge fund (e.g., LP, LLC, SICAV).

### Returns

Dict[str, Any]: A dictionary containing the legal entity type and a list of required regulatory filings.

### Raises

- ValueError: Raised if the input legal_entity_type is not one of the supported types (LP, LLC, SICAV).
- LookupError: Raised when the jurisdiction‑specific filing data for the given entity type cannot be retrieved.

### Examples

```python
>>> output = identify_regulatory_requirements('LLC')
>>> print(output['legal_entity_type'])
>>> print(output['regulatory_filings'])
"LLC\n[\n  'SEC Form 13D',\n  'SEC Form 13G',\n  'EFIS Filing',\n  'AIFM Registration',\n  'FCA FCA 21',\n  'HMRC Fund Registration',\n  'EU UCITS Directive',\n  'FINRA 24-13'\n]"
```

```python
>>> output = identify_regulatory_requirements('SICAV')
>>> print(output['regulatory_filings'])
"[\n  'Luxembourg AIFMD Registration',\n  'Luxembourg Fund Law Filing',\n  'EU UCITS Directive',\n  'FCA FCA 21',\n  'SEC Form N-1A',\n  'SEC Form 13D',\n  'EFIS Filing',\n  'HMRC Fund Registration'\n]"
```
