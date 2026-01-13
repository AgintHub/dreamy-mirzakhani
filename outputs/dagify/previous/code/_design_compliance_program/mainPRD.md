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
Validates the inputs for the design compliance program.

### Conceptual Info

The validate_inputs shim function validates the regulatory requirements and investor profile inputs for the design compliance program.

### Docstring

**Summary:** Validates the inputs for the design compliance program.

**Parameters:**

- regulatory_requirements (str): The regulatory requirements output from the identify_regulatory_requirements node.
- investor_profile (str): The investor profile output from the define_investor_profile node.
**Returns:** str - An output of type Any.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> validate_inputs(regulatory_requirements='requirement1', investor_profile='profile1')
'output1'
```

```python
>>> validate_inputs(regulatory_requirements='requirement2', investor_profile='profile2')
'output2'
```



---

## generate_accreditation_items

### Description
Generate a list of accreditation items required for compliance based on regulatory requirements and investor profile.

### Conceptual Info

The generate_accreditation_items shim function generates a list of accreditation items required for compliance based on the provided regulatory requirements and investor profile.

### Docstring

**Summary:** Generate a list of accreditation items required for compliance based on regulatory requirements and investor profile.

**Parameters:**

- regulatory_requirements (str): A string representing the regulatory requirements, e.g., output from the identify_regulatory_requirements node.
- investor_profile (str): A string representing the investor profile, e.g., output from the define_investor_profile node.
**Returns:** List[str] - A list of accreditation items required for compliance.

**Raises:**

- ValueError: When input validation fails, e.g., invalid or missing regulatory requirements or investor profile.
- TypeError: When input types are incorrect, e.g., regulatory requirements or investor profile is not a string.
**Examples:**

```python
>>> regulatory_requirements = {'requirement': 'Regulatory filing', 'agency_citation': 'Agency citation', 'implementation_notes': ['Note 1', 'Note 2']}
>>> investor_profile = {'typical_investor_types': ['Family offices', 'Pensions'], 'required_minimum_investment': 100000, 'liquidity_expectations': 'Short-term', 'risk_tolerance_levels': ['Aggressive', 'Conservative'], 'geographic_focus': 'Global'}
>>> generate_accreditation_items(regulatory_requirements=regulatory_requirements, investor_profile=investor_profile)
['Accreditation item 1', 'Accreditation item 2']
```



---

## calculate_implementation_dates

### Description
Calculates implementation dates for a list of accreditation, subscription, or AML items.

### Conceptual Info

The calculate_implementation_dates shim function generates a list of implementation dates for a given list of items and a category.

### Docstring

**Summary:** Calculates implementation dates for a list of items based on their category.

**Parameters:**

- items (List[str]): List of accreditation, subscription, or AML items
- category (str): Category of items (accreditation, subscription, or aml)
**Returns:** List[str] - List of implementation dates in YYYY-MM-DD format

**Raises:**

- ValueError: When the category is not one of accreditation, subscription, or aml
- TypeError: When the input items are not a list of strings
**Examples:**

```python
>>> calculate_implementation_dates(items=['item1', 'item2'], category='accreditation')
>>> => ['2024-01-01', '2024-02-01']
['2024-01-01', '2024-02-01']
```

```python
>>> calculate_implementation_dates(items=['item3', 'item4'], category='subscription')
>>> => ['2024-03-01', '2024-04-01']
['2024-03-01', '2024-04-01']
```



---

## generate_subscription_items

### Description
Generate a list of subscription verification procedures based on regulatory requirements and investor profile.

### Conceptual Info

The generate_subscription_items shim function generates a list of subscription verification procedures based on regulatory requirements and investor profile. This function is used in the design_compliance_program function to create a comprehensive compliance program.

### Docstring

**Summary:** Generate a list of subscription verification procedures based on regulatory requirements and investor profile.

**Parameters:**

- regulatory_requirements (str): A string representing the regulatory requirements, which may include specific regulatory filing or registration required, agency citation or form number associated with the requirement, and implementation notes describing how to implement or comply with the requirement.
- investor_profile (str): A string representing the investor profile, which may include typical investor types, required minimum investment, liquidity expectations, risk tolerance levels, and geographic focus.
**Returns:** List[str] - A list of subscription verification procedures to be followed.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_subscription_items(regulatory_requirements='requirement1', investor_profile='profile1')
['subscription_item1', 'subscription_item2']
```

```python
>>> generate_subscription_items(regulatory_requirements='requirement2', investor_profile='profile2')
['subscription_item3', 'subscription_item4']
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

- regulatory_requirements (str): A string representing the regulatory requirements, including specific filing or registration required, agency citation or form number, and implementation notes.
- investor_profile (str): A string representing the investor profile, including typical investor types, required minimum investment, liquidity expectations, risk tolerance levels, and geographic focus.
**Returns:** List[str] - A list of anti-money laundering policy items to implement.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_aml_items(regulatory_requirements='requirement1', investor_profile='profile1')
['AML policy item 1', 'AML policy item 2']
```

```python
>>> generate_aml_items(regulatory_requirements='requirement2', investor_profile='profile2')
['AML policy item 3', 'AML policy item 4']
```

