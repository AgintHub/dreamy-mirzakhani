# define_operational_stages PRD

## Description
Defines a list of operational stages from idea generation to settlement.


## Conceptual Info

The define_operational_stages shim function generates a list of operational stages that are commonly involved in the process of managing an asset from idea generation to settlement.

## Docstring

### Summary
Defines a list of operational stages from idea generation to settlement.

### Returns

List[str]: Ordered list of operational stages from idea generation to settlement.

### Raises

- ValueError: When the operational stages cannot be defined.
- TypeError: When the output type is incorrect.

### Examples

```python
>>> define_operational_stages()
['Idea Generation', 'Feasibility Study', 'Proposal Development', 'Investment Decision', 'Trade Execution', 'Settlement']
```

```python
>>> define_operational_stages()
['Research and Planning', 'Strategy Development', 'Risk Assessment', 'Trade Execution', 'Post-Trade Analysis']
```
