# draft_operations_workflow PRD

## Description
Generate an ordered list of daily trade lifecycle steps and the party responsible for each step.


## Conceptual Info

This node captures the day‑to‑day flow of a trade, mapping each activity to the entity or role that executes it. It provides a concise, step‑by‑step blueprint that feeds downstream staffing (create_hiring_plan) and technology requirements (define_technology_stack).

## Docstring

### Summary
Creates an ordered list of daily trade lifecycle steps and the responsible party for each step.

### Parameters

- **asset_classes** (List[str]): List of asset classes the fund trades (from define_asset_universe). Used to infer any asset‑specific steps or responsibilities.
- **instrument_types** (List[str]): List of specific instruments traded (from define_asset_universe). Helps determine instrument‑specific responsibilities.
- **prime_broker** (str): Name of the selected prime broker (from list_service_providers). Often handles execution and confirmation.
- **fund_administrator** (str): Name of the fund administrator (from list_service_providers). Typically responsible for settlement and reconciliation.
- **auditor** (str): Name of the external auditor (from list_service_providers). May validate reconciliation.
- **legal_counsel** (str): Name of the legal counsel firm (from list_service_providers). Handles regulatory compliance of trade lifecycle.
- **compliance_consultant** (str): Name of the compliance consulting firm (from list_service_providers). Oversees policy adherence during each step.
- **custodian** (str): Name of the custodial service provider (from list_service_providers). Holds settled positions.

### Returns

Tuple[List[str], List[str]]: A tuple containing an ordered list of trade lifecycle steps and a matching list of responsible parties.

### Raises

- ValueError: Raised if any required provider name is missing or empty.
- TypeError: Raised if input lists are not of type List[str] or provider arguments are not str.

### Examples

```python
>>> steps, parties = draft_operations_workflow(
...     asset_classes=['Equities', 'Futures'],
...     instrument_types=['S&P 500 ETF', 'Crude Oil Futures'],
...     prime_broker='PrimeCo',
...     fund_administrator='AdminInc',
...     auditor='AuditCo',
...     legal_counsel='LegalCo',
...     compliance_consultant='ComplianceCo',
...     custodian='CustodyCo' )
(
    ['Idea Generation', 'Order Entry', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'],
    ['In‑house Trading Desk', 'Compliance Team', 'PrimeCo', 'PrimeCo', 'AdminInc', 'AdminInc']
)
```

```python
>>> steps, parties = draft_operations_workflow(
...     asset_classes=['Equities'],
...     instrument_types=['SPY'],
...     prime_broker='PrimeCo',
...     fund_administrator='AdminInc',
...     auditor='AuditCo',
...     legal_counsel='LegalCo',
...     compliance_consultant='ComplianceCo',
...     custodian='CustodyCo' )
(
    ['Idea Generation', 'Order Entry', 'Execution', 'Confirmation', 'Settlement', 'Reconciliation'],
    ['In‑house Trading Desk', 'Compliance Team', 'PrimeCo', 'PrimeCo', 'AdminInc', 'AdminInc']
)
```
