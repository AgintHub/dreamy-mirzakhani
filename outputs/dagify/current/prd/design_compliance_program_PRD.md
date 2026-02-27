# design_compliance_program PRD

## Description
Creates the quantitative and qualitative risk control architecture.


## Conceptual Info

Generates the risk control architecture aligned with regulations and risk targets.

## Docstring

### Summary
Creates the risk control architecture by implementing core risk controls and systems.

### Returns

{risk_control_1: str, risk_control_2: str, risk_control_3: str, risk_control_4: str, risk_control_5: str, risk_control_6: str}: The implemented risk control architecture as a dictionary with keys: risk_control_1, risk_control_2, risk_control_3, risk_control_4, risk_control_5, risk_control_6, corresponding to the implemented risk controls.

### Raises

- RuntimeError: If any required risk control or system is not implemented.

### Examples

```python
>>> risk_controls = design_risk_management_framework(set_performance_and_risk_targets()).values
>>> print(risk_controls)
{'risk_control_1': 'position limits', 'risk_control_2': 'VaR caps', 'risk_control_3': 'stop-loss levels', 'risk_control_4': 'liquidity thresholds'}
```
