# estimate_setup_and_operating_costs PRD

## Description
Quantify financial resources needed for the hedge fund set‑up by aggregating estimated annual costs for service providers, technology systems, and office/human infrastructure.


## Conceptual Info

This node calculates the annual capital and operating expenditure required to launch the hedge fund, based on the service providers and technology stack identified in prior steps.

## Docstring

### Summary
Estimate annual costs for service providers, technology systems, and office/human infrastructure.

### Parameters

- **service_provider_categories** (List[str]): List of mandatory service provider categories (e.g., prime broker, custodian, compliance consultant) supplied by the `list_service_providers` node.
- **step_names** (List[str]): Ordered list of operational steps produced by the `define_technology_stack` node.
- **tech_components** (List[str]): Ordered list of technology components corresponding to each operational step.

### Returns

Tuple[float, float, float]: A tuple containing the annual cost estimates for service providers, technology systems, and office/human infrastructure, respectively.

### Raises

- ValueError: If any input list is empty or if the lengths of `step_names` and `tech_components` differ.
- TypeError: If any input is not of the expected type.

### Examples

```python
>>> service_provider_categories = ["Prime Broker", "Custodian", "Compliance Consultant", "Legal Advisor", "Fund Administrator", "Auditor"]
>>> step_names = ["Idea Generation", "Order Entry", "Execution", "Post‑Trade Processing", "Reporting"]
>>> tech_components = ["Research Platform", "OMS", "Execution System", "Post‑Trade System", "Reporting Suite"]
>>> costs = estimate_setup_and_operating_costs(service_provider_categories, step_names, tech_components)
>>> print(costs)
(225000.0, 180000.0, 125000.0)
```

```python
>>> service_provider_categories = []
>>> step_names = []
>>> tech_components = []
>>> try:
...     estimate_setup_and_operating_costs(service_provider_categories, step_names, tech_components)
>>> except ValueError as e:
...     print(str(e))
Input lists must not be empty.
```
