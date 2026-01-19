# estimate_setup_and_operating_costs PRD

## Description
Produce an initial budget estimate for the hedge fund, aggregating annual fees from mandatory service providers and general operational overhead.


## Conceptual Info

This node generates a concise, annual cost estimate table that aggregates provider fees and overhead, enabling early budget planning and financial modeling for the hedge fund launch.

## Docstring

### Summary
Estimates annual operating costs for each mandatory service provider and general overhead based on the selected providers.

### Parameters

- **prime_broker** (str): Name of the selected prime broker.
- **fund_administrator** (str): Name of the chosen fund administrator.
- **auditor** (str): Name of the external auditor.
- **legal_counsel** (str): Name of the legal counsel firm.
- **compliance_consultant** (str): Name of the compliance consulting firm.
- **custodian** (str): Name of the custodial service provider.

### Returns

Tuple[List[str], List[float]]: A two‑tuple where the first element is a list of cost item names and the second is the corresponding annual USD amounts.

### Raises

- ValueError: Raised if any provider name is an empty string.
- TypeError: Raised if any input is not of type `str`.

### Examples

```python
>>> cost_items, costs = estimate_setup_and_operating_costs(
...     prime_broker='PrimeB',
...     fund_administrator='AdminCo',
...     auditor='AuditInc',
...     legal_counsel='LawFirm',
...     compliance_consultant='ComplianceGrp',
...     custodian='CustodianLLC')
[['Prime Broker Fees', 'Fund Administrator Fees', 'Auditor Fees', 'Legal Counsel Fees', 'Compliance Consultant Fees', 'Custodian Fees', 'General Overhead'],
 [120000.0, 85000.0, 40000.0, 30000.0, 25000.0, 50000.0, 75000.0]]
```

```python
>>> cost_items, costs = estimate_setup_and_operating_costs(
...     prime_broker='PrimeB',
...     fund_administrator='AdminCo',
...     auditor='AuditInc',
...     legal_counsel='LawFirm',
...     compliance_consultant='ComplianceGrp',
...     custodian='CustodianLLC')
>>> print(dict(zip(cost_items, costs)))
{'Prime Broker Fees': 120000.0, 'Fund Administrator Fees': 85000.0, 'Auditor Fees': 40000.0, 'Legal Counsel Fees': 30000.0, 'Compliance Consultant Fees': 25000.0, 'Custodian Fees': 50000.0, 'General Overhead': 75000.0}
```
