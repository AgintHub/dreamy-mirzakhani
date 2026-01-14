# validate_input_requirements PRD

## Description
Validates the input requirements for the define asset universe and list service providers outputs to ensure compatibility and correctness for drafting an operations workflow.


## Conceptual Info

This shim validates input requirements to ensure the define asset universe and list service providers outputs are compatible and correct, which is crucial for drafting a viable operations workflow.

## Docstring

### Summary
Validate the input requirements for define asset universe and list service providers outputs to ensure they are compatible and correct for drafting an operations workflow.

### Parameters

- **asset_universe** (DefineAssetUniverseOutput): The output from the define asset universe node, containing instrument names, rationales, and asset class count.
- **service_providers** (ListServiceProvidersOutput): The output from the list service providers node, containing provider names and functions.

### Returns

str: A string indicating whether the input requirements are valid ('valid') or not ('invalid').

### Raises

- ValueError: When the input validation fails due to incompatible or missing data.
- TypeError: When the input types are incorrect, expecting DefineAssetUniverseOutput and ListServiceProvidersOutput instances.

### Examples

```python
>>> validate_input_requirements(asset_universe=DefineAssetUniverseOutput(instrument_names=[' Instrument1'], instrument_rationales=['Rationale1'], asset_class_count=1),
...                               service_providers=ListServiceProvidersOutput(provider_names=['Provider1'], provider_functions=['Function1']))
'valid'
```

```python
>>> validate_input_requirements(asset_universe='Invalid input', service_providers='Invalid input')
ValueError: Input validation failed due to incompatible data.
```
