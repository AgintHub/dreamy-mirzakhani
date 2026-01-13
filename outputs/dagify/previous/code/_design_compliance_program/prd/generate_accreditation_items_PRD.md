# generate_accreditation_items PRD

## Description
Generate a list of accreditation items required for compliance based on regulatory requirements and investor profile.


## Conceptual Info

The generate_accreditation_items shim function generates a list of accreditation items required for compliance based on the provided regulatory requirements and investor profile.

## Docstring

### Summary
Generate a list of accreditation items required for compliance based on regulatory requirements and investor profile.

### Parameters

- **regulatory_requirements** (str): A string representing the regulatory requirements, e.g., output from the identify_regulatory_requirements node.
- **investor_profile** (str): A string representing the investor profile, e.g., output from the define_investor_profile node.

### Returns

List[str]: A list of accreditation items required for compliance.

### Raises

- ValueError: When input validation fails, e.g., invalid or missing regulatory requirements or investor profile.
- TypeError: When input types are incorrect, e.g., regulatory requirements or investor profile is not a string.

### Examples

```python
>>> regulatory_requirements = {'requirement': 'Regulatory filing', 'agency_citation': 'Agency citation', 'implementation_notes': ['Note 1', 'Note 2']}
>>> investor_profile = {'typical_investor_types': ['Family offices', 'Pensions'], 'required_minimum_investment': 100000, 'liquidity_expectations': 'Short-term', 'risk_tolerance_levels': ['Aggressive', 'Conservative'], 'geographic_focus': 'Global'}
>>> generate_accreditation_items(regulatory_requirements=regulatory_requirements, investor_profile=investor_profile)
['Accreditation item 1', 'Accreditation item 2']
```
