# draft_operations_workflow PRD

## Description
Creates a structured outline of the daily operational workflow for a hedge fund, mapping each stage of the trade lifecycle to responsible parties and indicating whether a vendor is involved.


## Conceptual Info

The node captures the day‑to‑day operational flow of a hedge fund, from idea inception through settlement, assigning each leg of the process to either in‑house teams or external vendors.

## Docstring

### Summary
Builds a step‑by‑step operational workflow for trade execution, mapping responsibilities and vendor involvement.

### Parameters

- **asset_universe** (dict): Output of the `define_asset_universe` node containing `instrument_names`, `instrument_rationales`, and `asset_class_count`. Used to contextualize which assets will be traded.
- **service_providers** (dict): Output of the `list_service_providers` node containing `provider_names` and `provider_functions`. Provides the names of key third‑party vendors.

### Returns

dict: Dictionary with keys `stages`, `responsible_parties`, `vendor_involved`, and `stage_descriptions`, each holding a list of strings or booleans.

### Raises

- ValueError: Raised if either input dict is missing required keys.

### Examples

```python
>>> # Mock inputs
>>> asset_universe = {
...     'instrument_names': ['S&P 500 Futures', 'Emerging Market Debt', 'Crude Oil Futures'],
...     'instrument_rationales': ['Liquidity', 'Yield potential', 'Diversification'],
...     'asset_class_count': 3
>>> }
>>> service_providers = {
...     'provider_names': ['Prime Broker', 'Custodian', 'Fund Administrator', 'Legal Counsel', 'Compliance Consultant'],
...     'provider_functions': ['Order routing', 'Safekeeping', 'NAV calculations', 'Contract review', 'AML monitoring']
>>> }
>>> output = draft_operations_workflow(asset_universe, service_providers)
>>> print(output['stages'])
['Idea Generation', 'Signal Generation', 'Order Entry', 'Execution Management', 'Position Monitoring', 'Reconciliation', 'Settlement']
```

```python
>>> print(output['vendor_involved'])
[False, False, False, True, False, True, True]
```
