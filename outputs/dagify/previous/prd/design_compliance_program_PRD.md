# design_compliance_program PRD

## Description
Creates a regulatory control framework by mapping required compliance items across three key domains—investor accreditation, subscription verification, and anti-money laundering—alongside their planned implementation dates.


## Conceptual Info

The node synthesizes regulatory requirements identified earlier and investor profile constraints into a structured compliance program. It outputs three parallel lists of checklist items and their corresponding launch dates, ready for inclusion in a spreadsheet or project tracking tool.

## Docstring

### Summary
Generate compliance checklists for investor accreditation, subscription verification, and AML policies, each paired with an implementation date.

### Parameters

- **regulatory_requirements** (List[Dict[str, Any]]): Output from identify_regulatory_requirements. Each dict contains keys 'requirement', 'agency_citation', and 'implementation_notes'. These provide the regulatory basis for accreditation, subscription, and AML items.
- **investor_profile** (Dict[str, Any]): Output from define_investor_profile. Contains fields such as 'typical_investor_types', 'required_minimum_investment', 'liquidity_expectations', 'risk_tolerance_levels', and 'geographic_focus'. These inform the specificity of accreditation and subscription items.

### Returns

Dict[str, List[str]]: A dictionary with six keys—accreditation_items, accreditation_dates, subscription_items, subscription_dates, aml_items, aml_dates—each mapping to a list of strings.

### Raises

- ValueError: If either input list is empty or missing required keys.
- TypeError: If inputs are not of the expected types.

### Examples

```python
>>> # Example 1: Basic compliance program generation
>>> reg_req = [
...   {'requirement': 'SEC Form ADV', 'agency_citation': 'SEC', 'implementation_notes': ['File annually', 'Update bi‑annually']},
...   {'requirement': 'FINRA Membership', 'agency_citation': 'FINRA', 'implementation_notes': ['Apply within 30 days']}
>>> ]
>>> inv_prof = {
...   'typical_investor_types': ['Family Office', 'Pension Fund'],
...   'required_minimum_investment': 5000000,
...   'liquidity_expectations': 'Monthly',
...   'risk_tolerance_levels': ['Aggressive'],
...   'geographic_focus': 'US'"
                "}
>>> result = design_compliance_program(reg_req, inv_prof)
>>> print(result['accreditation_items'])
['SEC Form ADV', 'FINRA Membership']
```

```python
>>> # Example 2: Validation error when inputs missing
>>> try:
...   design_compliance_program([], inv_prof)
>>> except ValueError as e:
...   print(str(e))
Input regulatory_requirements list is empty.
```
