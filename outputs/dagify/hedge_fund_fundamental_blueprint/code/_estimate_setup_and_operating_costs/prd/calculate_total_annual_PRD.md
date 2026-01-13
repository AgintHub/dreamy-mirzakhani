# calculate_total_annual PRD

## Description
Sums a list of annual costs to produce the total annual budget.


## Conceptual Info

This shim aggregates individual annual cost items into a single total, enabling downstream budgeting calculations.

## Docstring

### Summary
Return the total of a list of annual cost amounts.

### Parameters

- **annual_costs** (List[float]): A list of annual cost values (USD) for each service provider or cost category.

### Returns

float: The sum of all numbers in `annual_costs`. If the list is empty, returns 0.0.

### Raises

- ValueError: Raised when any element in `annual_costs` is negative, indicating an invalid cost value.
- TypeError: Raised when `annual_costs` is not a list or contains non-numeric elements.

### Examples

```python
>>> calculate_total_annual(annual_costs=[12000.0, 24000.5, 18000.25])
54000.75
```

```python
>>> calculate_total_annual(annual_costs=[])
0.0
```
