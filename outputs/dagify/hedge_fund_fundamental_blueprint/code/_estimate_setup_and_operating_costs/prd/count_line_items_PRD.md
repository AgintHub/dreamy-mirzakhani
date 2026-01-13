# count_line_items PRD

## Description
Counts the number of unique service names provided.


## Conceptual Info

The shim determines how many distinct service names exist in a given list, which is essential for budget line item enumeration in the overall cost estimation workflow.

## Docstring

### Summary
Return the count of unique service names supplied.

### Parameters

- **service_names** (List[str]): A list of service names; may contain duplicates.

### Returns

int: The number of unique service names in the input list.

### Raises

- ValueError: Raised if service_names is empty.
- TypeError: Raised if service_names is not a list of strings.

### Examples

```python
>>> count_line_items(['PrimeBroker', 'Custodian', 'PrimeBroker', 'LegalCounsel'])
3
```

```python
>>> count_line_items([])
ValueError: service_names list cannot be empty
```
