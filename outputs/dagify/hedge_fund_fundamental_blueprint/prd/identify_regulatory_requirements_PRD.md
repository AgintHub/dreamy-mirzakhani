# identify_regulatory_requirements PRD

## Description
Maps the regulatory obligations that a newly formed hedge fund must satisfy based on its legal entity type and domicile.


## Conceptual Info

This node gathers the list of mandatory regulatory filings, registrations, and other compliance checkpoints that a hedge fund must complete in its chosen jurisdiction and entity form. It transforms the legal‑entity output from its parent node into a structured compliance checklist ready for downstream use in the compliance program design.

## Docstring

### Summary
Generate a list of all regulatory filings, registrations, and associated implementation notes required for the hedge fund’s chosen legal entity and jurisdiction.

### Parameters

- **legal_entity_info** (dict): Dictionary containing the legal entity type and jurisdiction as returned by the parent node `choose_legal_entity_type`.

### Returns

List[dict]: A list of dictionaries, each containing a `requirement`, `agency_citation`, and `implementation_notes` field.

### Raises

- KeyError: If `legal_entity_info` does not contain expected keys such as `legal_entity_type` or `jurisdiction`.
- ValueError: If the legal entity type or jurisdiction is unsupported or unknown.

### Examples

```python
>>> legal_entity_info = {
...     'legal_entity_type': 'LLC',
...     'jurisdiction': 'Delaware'
>>> }
[
  {
    "requirement": "Register with SEC as an investment adviser",
    "agency_citation": "SEC, Form ADV",
    "implementation_notes": [
      "File Form ADV Part 2A and 2B with the SEC",
      "Maintain annual updates and filing deadlines"
```
