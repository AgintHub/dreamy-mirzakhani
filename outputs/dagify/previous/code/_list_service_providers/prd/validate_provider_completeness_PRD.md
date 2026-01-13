# validate_provider_completeness PRD

## Description
Validates that the list of provider names and their corresponding functions are complete and correctly ordered.


## Conceptual Info

Ensures that each mandatory external service provider required for a chosen legal entity type is present with a corresponding function, preserving the predefined order: prime broker, custodian, fund administrator, legal counsel, compliance consultant.

## Docstring

### Summary
Checks that the provider names and their functions fully cover the required service stack and are in the correct order.

### Parameters

- **providers** (str): Comma‑separated string of provider names in the expected order.
- **functions** (str): Comma‑separated string of provider function descriptions matching the order of `providers`.

### Returns

str: A success message 'Provider completeness validated.' when all checks pass.

### Raises

- ValueError: Raised if the number of providers does not equal the number of functions, or if any required provider is missing.
- TypeError: Raised if `providers` or `functions` are not strings.

### Examples

```python
>>> validate_provider_completeness(
...     providers='prime broker,custodian,fund administrator,legal counsel,compliance consultant',
...     functions='Brokerage services,Custodial services,Administration services,Legal advice,Regulatory compliance'"
              ")
'Provider completeness validated.'
```

```python
>>> validate_provider_completeness(
...     providers='prime broker,custodian',
...     functions='Brokerage services,Custodial services'"
              ")
ValueError: Missing required providers or functions.
```
