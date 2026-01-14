# validate_inputs PRD

## Description
Validates that the regulatory requirements and investor profile inputs are non-empty strings and conform to expected formats, returning a success message or raising errors.


## Conceptual Info

This shim serves as a pre‑processing gate in the compliance design workflow, ensuring that downstream functions receive well‑formed regulatory and investor data.

## Docstring

### Summary
Validate the regulatory requirements and investor profile inputs before proceeding with compliance program design.

### Parameters

- **regulatory_requirements** (str): The output of the identify_regulatory_requirements node, expected to be a JSON string or a formatted summary of regulatory needs.
- **investor_profile** (str): The output of the define_investor_profile node, expected to be a JSON string or a formatted summary of investor characteristics.

### Returns

str: A message such as "Validation successful" when inputs pass all checks.

### Raises

- TypeError: Raised if either input is not a string.
- ValueError: Raised if either input is an empty string or does not contain required keys when parsed.

### Examples

```python
>>> validate_inputs(regulatory_requirements='{"requirement":"Form D"}', investor_profile='{"typical_investor_types":["family office"]}')
"Validation successful"
```

```python
>>> validate_inputs(regulatory_requirements='', investor_profile='{"typical_investor_types":["family office"]}')
"ValueError: regulatory_requirements cannot be empty"
```
