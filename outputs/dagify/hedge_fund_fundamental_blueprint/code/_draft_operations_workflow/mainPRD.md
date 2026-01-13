# _draft_operations_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the '_draft_operations_workflow' module.

## Table of Contents

- [define_operational_stages](#define_operational_stages)

- [assign_responsibilities_to_stages](#assign_responsibilities_to_stages)

- [determine_vendor_involvement](#determine_vendor_involvement)

- [generate_stage_descriptions](#generate_stage_descriptions)



---

## define_operational_stages

### Description
Defines a list of operational stages from idea generation to settlement.

### Conceptual Info

The define_operational_stages shim function generates a list of operational stages that are commonly involved in the process of managing an asset from idea generation to settlement.

### Docstring

**Summary:** Defines a list of operational stages from idea generation to settlement.

**Returns:** List[str] - Ordered list of operational stages from idea generation to settlement.

**Raises:**

- ValueError: When the operational stages cannot be defined.
- TypeError: When the output type is incorrect.
**Examples:**

```python
>>> define_operational_stages()
['Idea Generation', 'Feasibility Study', 'Proposal Development', 'Investment Decision', 'Trade Execution', 'Settlement']
```

```python
>>> define_operational_stages()
['Research and Planning', 'Strategy Development', 'Risk Assessment', 'Trade Execution', 'Post-Trade Analysis']
```



---

## assign_responsibilities_to_stages

### Description
Assigns responsibilities to operational stages based on the provided service providers.

### Conceptual Info

This shim function assigns responsibilities to operational stages based on the provided service providers, playing a crucial role in drafting the operations workflow.

### Docstring

**Summary:** Assigns responsibilities to operational stages based on the provided service providers.

**Parameters:**

- stages (str): A string representing operational stages, expected to be a comma-separated list of stages.
- service_providers (str): A string representing service providers, expected to be a comma-separated list of provider names.
**Returns:** List[str] - A list of responsible parties corresponding to each operational stage.

**Raises:**

- ValueError: When the number of service providers does not match the number of stages.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> assign_responsibilities_to_stages(stages='idea_generation,execution,settlement', service_providers='prime_broker,custodian,fund_administrator')
['prime_broker', 'custodian', 'fund_administrator']
```

```python
>>> assign_responsibilities_to_stages(stages='stage1,stage2,stage3', service_providers='provider1,provider2')
['provider1', 'provider2', 'In-house']
```



---

## determine_vendor_involvement

### Description
Determines vendor involvement for each stage in the operations workflow based on responsible parties.

### Conceptual Info

This shim function determines vendor involvement for each stage in the operations workflow based on the responsible parties.

### Docstring

**Summary:** Determines vendor involvement for each stage in the operations workflow based on responsible parties.

**Parameters:**

- responsible_parties (str): List of responsible parties for each stage in the operations workflow
**Returns:** List[bool] - List of boolean flags indicating vendor involvement for each stage

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> determine_vendor_involvement(responsible_parties=['In-house', 'Prime Broker', 'In-house'])
[False, True, False]
```

```python
>>> determine_vendor_involvement(responsible_parties=['Vendor', 'Vendor', 'In-house'])
[True, True, False]
```



---

## generate_stage_descriptions

### Description
Generates brief descriptions of activities performed in each operational stage.

### Conceptual Info

This shim function generates brief descriptions of activities performed in each operational stage, given the stages, asset context, and provider functions.

### Docstring

**Summary:** Generates brief descriptions of activities performed in each operational stage.

**Parameters:**

- stages (str): Ordered list of operational stages from idea generation to settlement.
- asset_context (str): List of selected tradable instruments (asset universe).
- provider_functions (str): Core function descriptions for each external service provider.
**Returns:** List[str] - List of brief descriptions for each operational stage.

**Raises:**

- ValueError: When input validation fails (e.g., stages, asset_context, or provider_functions are empty).
- TypeError: When input types are incorrect (e.g., stages is not a list of strings).
**Examples:**

```python
>>> generate_stage_descriptions(stages=['idea_generation', 'settlement'], asset_context=['stock', 'bond'], provider_functions=['prime_broker', 'custodian'])
['Brief description of idea generation stage', 'Brief description of settlement stage']
```

