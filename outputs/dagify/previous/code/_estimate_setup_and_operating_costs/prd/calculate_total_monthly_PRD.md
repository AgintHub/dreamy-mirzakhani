# calculate_total_monthly PRD

## Description
Calculates the total monthly cost from a list of monthly costs.


## Conceptual Info

The calculate_total_monthly shim function takes a string of monthly costs and returns the total monthly cost as a float.

## Docstring

### Summary
Calculates the total monthly cost from a string of monthly costs.

### Parameters

- **monthly_costs** (str): A string representation of the monthly costs.

### Returns

float: The total monthly cost.

### Raises

- ValueError: When the input string is not a valid representation of monthly costs.
- TypeError: When the input is not a string.

### Examples

```python
>>> calculate_total_monthly('100,200,300')
600.0
```

```python
>>> calculate_total_monthly('500')
500.0
```
