# generate_stage_descriptions PRD

## Description
Generates brief descriptions of operational stages for a given asset universe.


## Conceptual Info

This shim function generates brief descriptions of operational stages for a given asset universe, which are used to draft an operations workflow.

## Docstring

### Summary
Generates brief descriptions of operational stages for a given asset universe.

### Parameters

- **stages** (str): Ordered list of operational stages from idea generation to settlement.
- **asset_universe** (str): Typed node for define_asset_universe output.

### Returns

List[str]: List of brief descriptions for each operational stage.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> generate_stage_descriptions(stages=['idea_generation', 'trade_execution', 'settlement'], asset_universe='define_asset_universe_output')
['Brief description of idea generation stage.', 'Brief description of trade execution stage.', 'Brief description of settlement stage.']
```
