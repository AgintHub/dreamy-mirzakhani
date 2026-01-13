# assign_responsibilities_to_stages PRD

## Description
Assigns responsibilities to operational stages based on the provided service providers.


## Conceptual Info

This shim function assigns responsibilities to operational stages based on the provided service providers, playing a crucial role in drafting the operations workflow.

## Docstring

### Summary
Assigns responsibilities to operational stages based on the provided service providers.

### Parameters

- **stages** (str): A string representing operational stages, expected to be a comma-separated list of stages.
- **service_providers** (str): A string representing service providers, expected to be a comma-separated list of provider names.

### Returns

List[str]: A list of responsible parties corresponding to each operational stage.

### Raises

- ValueError: When the number of service providers does not match the number of stages.
- TypeError: When input types are incorrect.

### Examples

```python
>>> assign_responsibilities_to_stages(stages='idea_generation,execution,settlement', service_providers='prime_broker,custodian,fund_administrator')
['prime_broker', 'custodian', 'fund_administrator']
```

```python
>>> assign_responsibilities_to_stages(stages='stage1,stage2,stage3', service_providers='provider1,provider2')
['provider1', 'provider2', 'In-house']
```
