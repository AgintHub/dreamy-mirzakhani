# draft_operations_workflow PRD

## Description
Maps core trade and post-trade operational steps, outlining each stage in the trade lifecycle and assigning responsibility to internal teams or external service providers.


## Conceptual Info

This node details the sequence of core operational steps involved in executing a trade on a daily basis, including responsible parties at each stage.

## Docstring

### Summary
Maps and outlines the end-to-end daily trading and post-trade workflow, specifying operational steps and responsible entities.

### Parameters

- **define_asset_universe** (list of str): Predefined list of tradable assets and instruments used to inform operational procedures.
- **list_service_providers** (list of str): Identifies external service providers involved in trade lifecycle steps.
- **design_risk_management_framework** (list of str): Framework outlining risk controls influencing operational workflows.

### Returns

dict: Dictionary with 'tradelifecycle_steps' (list of trade steps) and 'responsible_parties' (respective responsible entities).

### Raises

- ValueError: If required dependencies are missing or contain invalid data.

### Examples

```python
>>> draft_operations_workflow()
{tradelifecycle_steps: [Idea Generation, Order Creation, Execution, Confirmation, Settlement, Reconciliation], responsible_parties: [Internal Research Team, Trading Desk, Broker Provider, Clearinghouse, Internal Operations, Compliance and Risk Team]}
```
