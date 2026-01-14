# validate_jurisdiction PRD

## Description
Validates a jurisdiction string and returns a standardized jurisdiction code or raises an error if invalid


## Conceptual Info

The `validate_jurisdiction` shim ensures that the jurisdiction value supplied to downstream regulatory logic is recognized, correctly formatted, and mapped to a canonical code, preventing downstream errors and enabling consistent mapping to regulatory requirements.

## Docstring

### Summary
Validate a jurisdiction string and return a canonical jurisdiction code.

### Parameters

- **jurisdiction** (str): The jurisdiction to be validated, typically provided by user input or extracted from context. It may be an abbreviated code, full name, or mixed case.

### Returns

str: A normalized jurisdiction code (e.g., 'DE', 'GB', 'US') that is guaranteed to exist in the system’s jurisdiction registry.

### Raises

- ValueError: Raised when the jurisdiction string does not match any known jurisdiction in the registry.
- TypeError: Raised when the jurisdiction argument is not a string.

### Examples

```python
>>> validate_jurisdiction('United States')
'US'
```

```python
>>> validate_jurisdiction('de')
'DE'
```

```python
>>> validate_jurisdiction('UnknownCountry')
ValueError: Unknown jurisdiction: UnknownCountry
```
