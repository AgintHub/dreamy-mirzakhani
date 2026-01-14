# define_operational_stages PRD

## Description
Defines the operational stages for a given asset context.


## Conceptual Info

The define_operational_stages shim function generates a list of operational stages based on the provided asset context.

## Docstring

### Summary
Defines the operational stages for a given asset context.

### Parameters

- **asset_context** (str): Input parameter describing the asset context, including instrument names, rationales, and asset class count.

### Returns

List[str]: A list of operational stages from idea generation to settlement.

### Raises

- ValueError: When the asset context is invalid or incomplete.
- TypeError: When the asset context is not a string.

### Examples

```python
>>> define_operational_stages(asset_context='{"instrument_names": ["stock1", "bond2"], "instrument_rationales": ["rationale1", "rationale2"], "asset_class_count": 2}')
['stage1', 'stage2', 'stage3']
```

```python
>>> define_operational_stages(asset_context='{"instrument_names": ["future1", "option2"], "instrument_rationales": ["rationale3", "rationale4"], "asset_class_count": 1}')
['stage4', 'stage5']
```
