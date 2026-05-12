# list_service_providers PRD

## Description
Identifies required external service providers for establishing and operating a hedge fund, focusing on key categories necessary for compliance and functionality.


## Conceptual Info

This node generates a list of essential external service provider categories required to operate a hedge fund, based on jurisdictional and operational needs.

## Docstring

### Summary
Creates a list of mandatory third-party service provider categories for hedge fund setup and operation.

### Parameters

- **jurisdiction** (str): The legal jurisdiction selected for the fund, influencing the service provider landscape.

### Returns

dict: A dictionary containing provider categories and their counts.

### Raises

- ValueError: If jurisdiction input is invalid or not provided.

### Examples

```python
>>> list_service_providers('Cayman')
{
```
