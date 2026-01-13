# _design_compliance_program - Complete PRD Documentation

## Overview
PRDs for nodes in the '_design_compliance_program' module.

## Table of Contents

- [validate_inputs](#validate_inputs)

- [generate_accreditation_items](#generate_accreditation_items)

- [calculate_implementation_dates](#calculate_implementation_dates)

- [generate_subscription_items](#generate_subscription_items)

- [generate_aml_items](#generate_aml_items)



---

## validate_inputs

### Description
Validates that the regulatory requirements and investor profile inputs are non-empty strings and conform to expected formats, returning a success message or raising errors.

### Conceptual Info

This shim serves as a pre‑processing gate in the compliance design workflow, ensuring that downstream functions receive well‑formed regulatory and investor data.

### Docstring

**Summary:** Validate the regulatory requirements and investor profile inputs before proceeding with compliance program design.

**Parameters:**

- regulatory_requirements (str): The output of the identify_regulatory_requirements node, expected to be a JSON string or a formatted summary of regulatory needs.
- investor_profile (str): The output of the define_investor_profile node, expected to be a JSON string or a formatted summary of investor characteristics.
**Returns:** str - A message such as "Validation successful" when inputs pass all checks.

**Raises:**

- TypeError: Raised if either input is not a string.
- ValueError: Raised if either input is an empty string or does not contain required keys when parsed.
**Examples:**

```python
>>> validate_inputs(regulatory_requirements='{"requirement":"Form D"}', investor_profile='{"typical_investor_types":["family office"]}')
"Validation successful"
```

```python
>>> validate_inputs(regulatory_requirements='', investor_profile='{"typical_investor_types":["family office"]}')
"ValueError: regulatory_requirements cannot be empty"
```



---

## generate_accreditation_items

### Description
Generate a list of accreditation items based on regulatory requirements and investor profile.

### Conceptual Info

The generate_accreditation_items shim function generates a list of accreditation items required for compliance based on the provided regulatory requirements and investor profile.

### Docstring

**Summary:** Generate a list of accreditation items required for compliance based on regulatory requirements and investor profile.

**Parameters:**

- regulatory_requirements (str): A string containing regulatory requirements, e.g., 'requirement: str, agency_citation: str, implementation_notes: List[str]'.
- investor_profile (str): A string containing investor profile, e.g., 'typical_investor_types: List[str], required_minimum_investment: int, liquidity_expectations: str'.
**Returns:** List[str] - A list of accreditation items required for compliance.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_accreditation_items(regulatory_requirements='requirement1, agency_citation1, implementation_notes1', investor_profile='typical_investor_types1, required_minimum_investment1, liquidity_expectations1')
['accreditation_item1', 'accreditation_item2']
```

```python
>>> generate_accreditation_items(regulatory_requirements='requirement2, agency_citation2, implementation_notes2', investor_profile='typical_investor_types2, required_minimum_investment2, liquidity_expectations2')
['accreditation_item3', 'accreditation_item4']
```



---

## calculate_implementation_dates

### Description
Generates a list of implementation dates for a set of compliance items, one per item, based on the given category.

### Conceptual Info

The shim calculates realistic implementation dates for compliance tasks, ensuring that each item in a category receives a unique, sequential date that respects typical regulatory deadlines.

### Docstring

**Summary:** Compute implementation dates for compliance items based on their category.

**Parameters:**

- items (List[str]): A list of compliance items that require implementation.
- category (str): The category of the items (e.g., "accreditation", "subscription", "aml").
**Returns:** List[str] - A list of dates in ISO format (YYYY-MM-DD) corresponding one‑to‑one with the input items.

**Raises:**

- ValueError: Raised if the items list is empty or if the category is not one of the supported categories.
- TypeError: Raised if items is not a list of strings or if category is not a string.
**Examples:**

```python
>>> calculate_implementation_dates(["KYC", "AML Review"], "accreditation")
['2024-09-01', '2024-09-15']
```

```python
>>> calculate_implementation_dates(["Form D Filing", "Subscription Agreement"], "subscription")
['2024-10-05', '2024-10-20']
```



---

## generate_subscription_items

### Description
Generates a list of subscription verification procedures required for a private placement, based on regulatory requirements and investor profile.

### Conceptual Info

This shim acts as the core logic for determining subscription procedures in a compliance program. It interprets regulatory mandates (e.g., SEC, FCA) and investor characteristics to enumerate concrete steps such as KYC checks, investment eligibility confirmations, and documentation collection.

### Docstring

**Summary:** Generate a list of subscription verification procedures required to comply with regulatory filings and investor profile constraints.

**Parameters:**

- regulatory_requirements (str): A JSON string or identifier representing regulatory filing details (e.g., 'SEC Rule 506(b)', 'FCA Reg 2').
- investor_profile (str): A JSON string or identifier describing investor types, minimum investment, risk tolerance, and geographic focus.
**Returns:** LIST_STR - A list of human‑readable subscription verification procedures, e.g., ['Verify accredited investor status', 'Collect signed subscription agreement', 'Check AML screening results'].

**Raises:**

- ValueError: If regulatory_requirements or investor_profile are empty or do not contain required fields.
- TypeError: If either input is not a string.
**Examples:**

```python
>>> reg_req = "{'agency': 'SEC', 'form': 'D', 'requirement': 'KYC and AML compliance'}"
>>> inv_prof = "{'typical_investor_types': ['family office', 'high net worth'], 'required_minimum_investment': 500000}"
>>> steps = generate_subscription_items(regulatory_requirements=reg_req, investor_profile=inv_prof)
>>> print(steps)
["Collect signed subscription agreement", "Verify accredited investor status", "Perform AML screening"]
```

```python
>>> reg_req = "{'agency': 'FCA', 'form': 'P5', 'requirement': 'Proof of funds'}"
>>> inv_prof = "{'typical_investor_types': ['institutional'], 'required_minimum_investment': 1000000}"
>>> steps = generate_subscription_items(regulatory_requirements=reg_req, investor_profile=inv_prof)
>>> print(steps)
["Request bank statements", "Confirm source of funds", "Sign subscription agreement"]
```



---

## generate_aml_items

### Description
Generate a list of anti-money laundering policy items to implement based on regulatory requirements and investor profile.

### Conceptual Info

The generate_aml_items shim function generates a list of anti-money laundering policy items to implement based on the provided regulatory requirements and investor profile.

### Docstring

**Summary:** Generate a list of anti-money laundering policy items to implement based on regulatory requirements and investor profile.

**Parameters:**

- regulatory_requirements (str): Input parameter containing regulatory requirements
- investor_profile (str): Input parameter containing investor profile
**Returns:** List[str] - List of anti-money laundering policy items to implement

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_aml_items(regulatory_requirements='example req', investor_profile='example profile')
>>> ['Implement AML policy item 1', 'Implement AML policy item 2']
['Implement AML policy item 1', 'Implement AML policy item 2']
```

```python
>>> generate_aml_items(regulatory_requirements='another req', investor_profile='another profile')
>>> ['Implement AML policy item 3', 'Implement AML policy item 4']
['Implement AML policy item 3', 'Implement AML policy item 4']
```

