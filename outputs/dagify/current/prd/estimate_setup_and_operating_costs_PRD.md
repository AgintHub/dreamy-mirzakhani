# estimate_setup_and_operating_costs PRD

## Description
Produces a high-level cost model for launch and ongoing operations.


## Conceptual Info

Estimate and summarize costs required for hedge fund operations.

## Docstring

### Summary
Estimate and summarize costs required for hedge fund operations based on listed service providers and internal overhead categories.

### Parameters

- **provider_categories_list** (str): Output list from 'list_service_providers' node or other relevant data source.
- **internal_overhead_categories** (str): User-provided list of internal overhead categories.

### Returns

Dict[str, Union[List[float], float]]: Cost estimates for each service provider category and internal overhead category.

### Raises

- ValueError: If 'provider_categories_list' or 'internal_overhead_categories' is invalid or empty.

### Examples

```python
>>> provider_categories_list = ['prime broker', 'fund administrator', 'auditor']
>>> internal_overhead_categories = ['office', 'technology', 'staffing']
>>> estimate_setup_and_operating_costs(provider_categories_list, internal_overhead_categories)
{"
              "  'service_provider_costs': [100000, 50000, 20000],"
              "  'internal_overhead_costs': [30000, 20000, 40000]"
              
```
