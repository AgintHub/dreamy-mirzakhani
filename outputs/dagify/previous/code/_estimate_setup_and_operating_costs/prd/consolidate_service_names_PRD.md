# consolidate_service_names PRD

## Description
This shim function consolidates service provider names, technology names, and governance names into a single list of service names.


## Conceptual Info

The consolidate_service_names shim function plays a crucial role in integrating and standardizing service names across different domains, ensuring consistency and clarity in the overall system.

## Docstring

### Summary
Consolidates service provider names, technology names, and governance names into a single list of service names.

### Parameters

- **provider_names** (str): A string of service provider names separated by commas.
- **technology_names** (str): A string of technology names separated by commas.
- **governance_names** (str): A string of governance names separated by commas.

### Returns

List[str]: A list of consolidated service names.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> consolidate_service_names(provider_names='Prime Broker, Custodian, Fund Administrator', technology_names='Data Analytics Platform, Portfolio Management System', governance_names='Risk Management, Compliance')
['Prime Broker', 'Custodian', 'Fund Administrator', 'Data Analytics Platform', 'Portfolio Management System', 'Risk Management', 'Compliance']
```
