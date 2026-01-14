# generate_budget_overview PRD

## Description
Creates a concise textual summary of the overall budget, highlighting major cost drivers and key service categories.


## Conceptual Info

The shim generates a human‑readable budget overview that condenses numeric totals and service names into a single paragraph suitable for executive reporting.

## Docstring

### Summary
Generate a budget overview string summarizing annual cost totals per service category.

### Parameters

- **total_annual** (str): Total annual budget as a formatted string (e.g., "$12,345,678").
- **service_names** (str): Comma‑separated list of service names corresponding to the annual costs.
- **annual_costs** (str): Comma‑separated list of annual costs per service, matching the order of service_names.

### Returns

str: A single paragraph string summarizing the budget, including the total annual amount and the top three cost drivers.

### Raises

- ValueError: Raised if the numbers of service names and costs do not match.
- TypeError: Raised if any argument is not a string.

### Examples

```python
>>> result = generate_budget_overview(
...     total_annual='$12,345,678',
...     service_names='Prime Broker,Custodian,Legal Counsel',
...     annual_costs='5,000,000;2,500,000;1,000,000')
>>> print(result)
"Total annual budget is $12,345,678. The largest cost drivers are Prime Broker ($5,000,000), Custodian ($2,500,000), and Legal Counsel ($1,000,000)."
```

```python
>>> generate_budget_overview('','$','')
"Total annual budget is $0. No cost drivers to report."
```
