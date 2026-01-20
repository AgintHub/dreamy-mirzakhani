# define_technology_stack PRD

## Description
Identify system requirements


## Conceptual Info

This node maps the daily trade lifecycle to the necessary software and infrastructure, ensuring each operational step has a clear technology owner.

## Docstring

### Summary
Map each trade lifecycle step to its required technology component(s).

### Parameters

- **trade_lifecycle_steps** (List[str]): Ordered list of daily trade lifecycle steps as produced by draft_operations_workflow.

### Returns

Dict[str, List[str]]: A dictionary containing two keys: 'ops_steps' and 'tech_components', each a list of strings aligned by index.

### Raises

- ValueError: If trade_lifecycle_steps is empty or contains non-string items.

### Examples

```python
>>> trade_lifecycle_steps = [
...     'Idea Generation',
...     'Order Entry',
...     'Execution',
...     'Confirmation',
...     'Settlement',
...     'Reconciliation']
>>> ops_steps, tech_components = define_technology_stack(trade_lifecycle_steps)
>>> print(ops_steps)
>>> print(tech_components)
[
    'Idea Generation',
    'Order Entry',
    'Execution',
    'Confirmation',
    'Settlement',
    'Reconciliation'
]
[
    'Ideation Platform (e.g., Slack, IdeaBoard)',
    'Order Management System (OMS)',
    'Execution Platform (e.g., FIX gateway, Algo engine)',
    'Confirmation System (e.g., Trade Capture)',
    'Clearing & Custody System',
    'Reconciliation Suite (e.g., Calypso, BlackLine)'
]
```

```python
>>> trade_lifecycle_steps = ['Order Entry', 'Execution', 'Settlement']
>>> ops_steps, tech_components = define_technology_stack(trade_lifecycle_steps)
>>> print(tech_components[-1])
'Clearing & Custody System'
```
