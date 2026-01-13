# generate_stage_descriptions PRD

## Description
Generates brief descriptions of activities performed in each operational stage.


## Conceptual Info

This shim function generates brief descriptions of activities performed in each operational stage, given the stages, asset context, and provider functions.

## Docstring

### Summary
Generates brief descriptions of activities performed in each operational stage.

### Parameters

- **stages** (str): Ordered list of operational stages from idea generation to settlement.
- **asset_context** (str): List of selected tradable instruments (asset universe).
- **provider_functions** (str): Core function descriptions for each external service provider.

### Returns

List[str]: List of brief descriptions for each operational stage.

### Raises

- ValueError: When input validation fails (e.g., stages, asset_context, or provider_functions are empty).
- TypeError: When input types are incorrect (e.g., stages is not a list of strings).

### Examples

```python
>>> generate_stage_descriptions(stages=['idea_generation', 'settlement'], asset_context=['stock', 'bond'], provider_functions=['prime_broker', 'custodian'])
['Brief description of idea generation stage', 'Brief description of settlement stage']
```
