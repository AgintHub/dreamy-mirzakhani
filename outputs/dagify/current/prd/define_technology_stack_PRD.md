# define_technology_stack PRD

## Description
Specify system infrastructure requirements


## Conceptual Info

The `define_technology_stack` node translates the operational workflow defined in `draft_operations_workflow` into a concrete technology roadmap. It aligns each lifecycle stage with a suitable platform or service and flags whether the capability will be built internally or sourced from a third‑party vendor. The output feeds cost estimation and vendor selection nodes downstream.

## Docstring

### Summary
Generate a technology stack mapping for the hedge fund’s operational workflow.

### Parameters

- **workflow_stages** (List[str]): Ordered list of workflow stages as produced by `draft_operations_workflow`.
- **stage_descriptions** (List[str]): Brief description of activities performed in each stage (used for contextual mapping).

### Returns

Dict[str, List[Any]]: A dictionary containing three keys:
- `workflow_stages` (List[str])
- `technology_solutions` (List[str])
- `vendor_in_house_flags` (List[bool])

### Raises

- ValueError: If the length of `workflow_stages` and `stage_descriptions` do not match.
- KeyError: If a known workflow stage is not present in the internal mapping.

### Examples

```python
>>> workflow_stages = ["Idea Generation", "Signal Generation", "Order Entry", "Execution Management", "Position Monitoring", "Reconciliation", "Settlement"],
>>> stage_descriptions = [
...     "Generate investment ideas via research and data analysis.",
...     "Generate buy/sell signals from quantitative models.",
...     "Create order records in the OMS.",
...     "Route orders to market via FIX gateway.",
...     "Track open positions and P&L.",
...     "Automated P&L and trade reconciliation.",
...     "Confirm settlements with custodians and counterparties."]
>>> result = define_technology_stack(workflow_stages, stage_descriptions)
>>> print(result)
{
  "workflow_stages": ["Idea Generation", "Signal Generation", "Order Entry", "Execution Management", "Position Monitoring", "Reconciliation", "Settlement"],
  "technology_solutions": ["Data Analytics Platform", "Quant Model Engine", "Order Management System", "FIX Gateway", "Risk Engine", "Reconciliation Tool", "Settlement Service"],
  "vendor_in_house_flags": [true, true, false, false, true, false, false]
}
```

```python
>>> # Using a shortened workflow
workflow_stages = ["Signal Generation", "Order Entry", "Execution Management"],
>>> stage_descriptions = [
...     "Generate buy/sell signals.",
...     "Create orders.",
...     "Route to market."]
>>> print(define_technology_stack(workflow_stages, stage_descriptions))
{
  "workflow_stages": ["Signal Generation", "Order Entry", "Execution Management"],
  "technology_solutions": ["Quant Model Engine", "Order Management System", "FIX Gateway"],
  "vendor_in_house_flags": [true, false, false]
}
```
