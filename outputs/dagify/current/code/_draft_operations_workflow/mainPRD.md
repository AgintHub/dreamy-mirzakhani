# _draft_operations_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the '_draft_operations_workflow' module.

## Table of Contents

- [validate_input_requirements](#validate_input_requirements)

- [define_operational_stages](#define_operational_stages)

- [assign_stage_responsibilities](#assign_stage_responsibilities)

- [determine_vendor_involvement](#determine_vendor_involvement)

- [generate_stage_descriptions](#generate_stage_descriptions)



---

## validate_input_requirements

### Description
Validates the input requirements for the define asset universe and list service providers outputs to ensure compatibility and correctness for drafting an operations workflow.

### Conceptual Info

This shim validates input requirements to ensure the define asset universe and list service providers outputs are compatible and correct, which is crucial for drafting a viable operations workflow.

### Docstring

**Summary:** Validate the input requirements for define asset universe and list service providers outputs to ensure they are compatible and correct for drafting an operations workflow.

**Parameters:**

- asset_universe (DefineAssetUniverseOutput): The output from the define asset universe node, containing instrument names, rationales, and asset class count.
- service_providers (ListServiceProvidersOutput): The output from the list service providers node, containing provider names and functions.
**Returns:** str - A string indicating whether the input requirements are valid ('valid') or not ('invalid').

**Raises:**

- ValueError: When the input validation fails due to incompatible or missing data.
- TypeError: When the input types are incorrect, expecting DefineAssetUniverseOutput and ListServiceProvidersOutput instances.
**Examples:**

```python
>>> validate_input_requirements(asset_universe=DefineAssetUniverseOutput(instrument_names=[' Instrument1'], instrument_rationales=['Rationale1'], asset_class_count=1),
...                               service_providers=ListServiceProvidersOutput(provider_names=['Provider1'], provider_functions=['Function1']))
'valid'
```

```python
>>> validate_input_requirements(asset_universe='Invalid input', service_providers='Invalid input')
ValueError: Input validation failed due to incompatible data.
```



---

## define_operational_stages

### Description
Defines the operational stages for a given asset context.

### Conceptual Info

The define_operational_stages shim function generates a list of operational stages based on the provided asset context.

### Docstring

**Summary:** Defines the operational stages for a given asset context.

**Parameters:**

- asset_context (str): Input parameter describing the asset context, including instrument names, rationales, and asset class count.
**Returns:** List[str] - A list of operational stages from idea generation to settlement.

**Raises:**

- ValueError: When the asset context is invalid or incomplete.
- TypeError: When the asset context is not a string.
**Examples:**

```python
>>> define_operational_stages(asset_context='{"instrument_names": ["stock1", "bond2"], "instrument_rationales": ["rationale1", "rationale2"], "asset_class_count": 2}')
['stage1', 'stage2', 'stage3']
```

```python
>>> define_operational_stages(asset_context='{"instrument_names": ["future1", "option2"], "instrument_rationales": ["rationale3", "rationale4"], "asset_class_count": 1}')
['stage4', 'stage5']
```



---

## assign_stage_responsibilities

### Description
Assigns responsible parties to each operational stage based on the provided list of stages and service provider names.

### Conceptual Info

This shim provides the core logic for determining which organization (in‑house or a specific vendor) is accountable for each stage in the investment lifecycle, enabling downstream nodes to flag vendor involvement and generate stage descriptions.

### Docstring

**Summary:** Map operational stages to responsible parties using the fixed provider order.

**Parameters:**

- stages (str): An ordered, comma‑separated string of operational stage names.
- providers (str): An ordered, comma‑separated string of mandatory external service provider names in the order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.
**Returns:** str - A comma‑separated string of responsible parties, one for each stage, matching the input order.

**Raises:**

- ValueError: Raised if the number of stages does not match the number of providers.
- TypeError: Raised if either input is not a string.
**Examples:**

```python
>>> stages = 'Idea Generation,Structuring,Compliance,Execution,Settlement'
>>> providers = 'Prime Broker,Custodian,Fund Administrator,Legal Counsel,Compliance Consultant'
>>> result = assign_stage_responsibilities(stages, providers)
>>> print(result)
'Prime Broker,Custodian,Fund Administrator,Legal Counsel,Compliance Consultant'
```

```python
>>> assign_stage_responsibilities('Idea Generation,Execution', 'Prime Broker')
ValueError: Number of stages (2) does not match number of providers (1).
```



---

## determine_vendor_involvement

### Description
Determines vendor involvement for each stage in the operations workflow based on responsible parties.

### Conceptual Info

This shim function determines vendor involvement for each stage in the operations workflow based on responsible parties.

### Docstring

**Summary:** Determines vendor involvement for each stage in the operations workflow based on responsible parties.

**Parameters:**

- responsible_parties (str): List of responsible parties for each stage in the operations workflow.
**Returns:** List[bool] - List of boolean flags indicating vendor involvement for each stage.

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
Generates brief descriptions of operational stages for a given asset universe.

### Conceptual Info

This shim function generates brief descriptions of operational stages for a given asset universe, which are used to draft an operations workflow.

### Docstring

**Summary:** Generates brief descriptions of operational stages for a given asset universe.

**Parameters:**

- stages (str): Ordered list of operational stages from idea generation to settlement.
- asset_universe (str): Typed node for define_asset_universe output.
**Returns:** List[str] - List of brief descriptions for each operational stage.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_stage_descriptions(stages=['idea_generation', 'trade_execution', 'settlement'], asset_universe='define_asset_universe_output')
['Brief description of idea generation stage.', 'Brief description of trade execution stage.', 'Brief description of settlement stage.']
```

