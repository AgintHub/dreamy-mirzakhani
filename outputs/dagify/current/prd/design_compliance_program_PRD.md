# design_compliance_program PRD

## Description
Create regulatory compliance framework


## Conceptual Info

The node assembles a compliance matrix that maps every regulatory requirement to a specific internal policy. It consumes the outputs from the risk‑management framework (to understand controls) and the regulatory‑requirements list (to know what must be met). The resulting matrices are used by the pitch deck and final summary.

## Docstring

### Summary
Generate a compliance checklist that maps each regulatory requirement to its internal policy reference.

### Parameters

- **control_name** (List[str]): Names of the risk control measures from the risk‑management framework.
- **target_metric** (List[str]): Performance or risk metric each control is designed to limit.
- **limit_value** (List[float]): Numeric threshold for each control.
- **requirements** (List[str]): Primary regulatory filings or registrations required for the chosen legal entity.
- **governing_bodies** (List[str]): Governing bodies responsible for each regulatory requirement.

### Returns

Tuple[List[str], List[str]]: A tuple containing two lists: the first list is the ordered regulatory requirements, the second list is the corresponding internal policy references that satisfy each requirement.

### Raises

- ValueError: If any input list is empty or if the lengths of the regulatory lists do not match.

### Examples

```python
>>> requirement_list, policy_reference_list = design_compliance_program(

...     control_name=["Position Limit", "VaR Limit"],

...     target_metric=["Daily Position Size", "Annual VaR"],

...     limit_value=[1.0, 0.02],

...     requirements=["Securities Act Registration", "AML Registration"],

...     governing_bodies=["SEC", "FINCEN"]

>>> )
{'requirement_list': ['Securities Act Registration', 'AML Registration'],
 'policy_reference_list': ['Policy_P100', 'Policy_P200']}
```

```python
>>> # Minimal example with one requirement

>>> design_compliance_program(

...     control_name=['Stop‑Loss Rule'],

...     target_metric=['Max Daily Loss'],

...     limit_value=[0.05],

...     requirements=['Regulation K'],

...     governing_bodies=['SEC']

>>> )
{'requirement_list': ['Regulation K'],
 'policy_reference_list': ['Policy_P300']}
```
