# create_hiring_plan PRD

## Description
Determines initial staffing requirements.


## Conceptual Info

Creates a list of essential roles required for launching the fund with detailed responsibilities.

## Docstring

### Summary
Determine initial staffing requirements based on drafted operations workflow.

### Parameters

- **tradelifecycle_steps** (List[str]): List of daily trade lifecycle steps from drafted operations workflow.

### Returns

dict: A dictionary containing 'roles_needed' and 'count_roles'.

### Raises

- ValueError: If 'tradelifecycle_steps' is empty.

### Examples

```python
>>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'])

role_needed = roles_needed
count_roles = count_roles
print(role_needed)
print(count_roles)
```

```python
>>> create_hiring_plan(tradelifecycle_steps=['Idea generation', 'Order creation', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation', 'Market Analysis'])

role_needed = roles_needed
count_roles = count_roles
print(role_needed)
print(count_roles)
```
