# list_service_providers PRD

## Description
Compile third-party vendor requirements


## Conceptual Info

The node generates a concise, ordered checklist of essential third‑party service providers required to launch a hedge fund, based on the selected legal entity type. Each provider is accompanied by a single‑sentence core function that captures its primary role in the fund’s operational ecosystem.

## Docstring

### Summary
Generate an ordered list of mandatory external service providers and their core functions.

### Parameters

- **legal_entity_type** (str): The chosen legal entity type (e.g., LP, LLC, SICAV) obtained from the `choose_legal_entity_type` node.

### Returns

dict: A dictionary with two keys: `provider_names` (List[str]) and `provider_functions` (List[str]). Both lists are aligned so that index *i* in `provider_names` corresponds to index *i* in `provider_functions`.

### Raises

- ValueError: Raised if `legal_entity_type` is empty or not one of the supported entity types.
- KeyError: Raised if the internal mapping for the given entity type does not contain entries for all required providers.

### Examples

```python
>>> output = list_service_providers('LP')
>>> print(output['provider_names'])
>>> print(output['provider_functions'])
["Prime Broker", "Custodian", "Fund Administrator", "Legal Counsel", "Compliance Consultant"]\n["Facilitates trade execution and margin management.", "Safeguards assets and provides custody services.", "Handles NAV calculation, investor reporting, and fund accounting.", "Provides legal structuring and regulatory compliance advice.", "Assesses and implements AML and other compliance policies."]
```

```python
>>> output = list_service_providers('SICAV')
>>> print(output['provider_functions'][2])
"Handles NAV calculation, investor reporting, and fund accounting."
```
