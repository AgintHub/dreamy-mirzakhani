# generate_subscription_items PRD

## Description
Generates a list of subscription verification procedures required for a private placement, based on regulatory requirements and investor profile.


## Conceptual Info

This shim acts as the core logic for determining subscription procedures in a compliance program. It interprets regulatory mandates (e.g., SEC, FCA) and investor characteristics to enumerate concrete steps such as KYC checks, investment eligibility confirmations, and documentation collection.

## Docstring

### Summary
Generate a list of subscription verification procedures required to comply with regulatory filings and investor profile constraints.

### Parameters

- **regulatory_requirements** (str): A JSON string or identifier representing regulatory filing details (e.g., 'SEC Rule 506(b)', 'FCA Reg 2').
- **investor_profile** (str): A JSON string or identifier describing investor types, minimum investment, risk tolerance, and geographic focus.

### Returns

LIST_STR: A list of human‑readable subscription verification procedures, e.g., ['Verify accredited investor status', 'Collect signed subscription agreement', 'Check AML screening results'].

### Raises

- ValueError: If regulatory_requirements or investor_profile are empty or do not contain required fields.
- TypeError: If either input is not a string.

### Examples

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
