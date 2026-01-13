# estimate_technology_costs PRD

## Description
Estimates technology costs based on workflow stages, technology solutions, and vendor flags.


## Conceptual Info

The estimate_technology_costs shim function provides a placeholder for estimating technology costs based on workflow stages, technology solutions, and vendor flags. Its purpose is to facilitate the calculation of technology costs in the larger system.

## Docstring

### Summary
Estimates technology costs based on workflow stages, technology solutions, and vendor flags.

### Parameters

- **workflow_stages** (str): Ordered list of workflow stages (e.g., Idea Generation, Signal Generation, Order Entry, Execution Management, Position Monitoring, Reconciliation, Settlement).
- **technology_solutions** (str): Corresponding technology solution for each stage (e.g., Data Analytics Platform, Portfolio Management System, OMS, FIX Gateway, Risk Engine, Reconciliation Tool).
- **vendor_flags** (str): Boolean flag for each stage indicating whether the solution is implemented in-house (true) or outsourced to a vendor (false).

### Returns

List[float]: List of estimated technology costs.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> estimate_technology_costs(workflow_stages=['Idea Generation', 'Signal Generation'], technology_solutions=['Data Analytics Platform', 'Portfolio Management System'], vendor_flags=['in-house', 'outsourced'])
[1000.0, 2000.0]
```

```python
>>> estimate_technology_costs(workflow_stages=['Order Entry', 'Execution Management'], technology_solutions=['OMS', 'FIX Gateway'], vendor_flags=['outsourced', 'in-house'])
[1500.0, 2500.0]
```
