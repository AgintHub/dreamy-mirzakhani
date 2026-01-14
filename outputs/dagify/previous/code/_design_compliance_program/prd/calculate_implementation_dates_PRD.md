# calculate_implementation_dates PRD

## Description
Generates a list of implementation dates for a set of compliance items, one per item, based on the given category.


## Conceptual Info

The shim calculates realistic implementation dates for compliance tasks, ensuring that each item in a category receives a unique, sequential date that respects typical regulatory deadlines.

## Docstring

### Summary
Compute implementation dates for compliance items based on their category.

### Parameters

- **items** (List[str]): A list of compliance items that require implementation.
- **category** (str): The category of the items (e.g., "accreditation", "subscription", "aml").

### Returns

List[str]: A list of dates in ISO format (YYYY-MM-DD) corresponding one‑to‑one with the input items.

### Raises

- ValueError: Raised if the items list is empty or if the category is not one of the supported categories.
- TypeError: Raised if items is not a list of strings or if category is not a string.

### Examples

```python
>>> calculate_implementation_dates(["KYC", "AML Review"], "accreditation")
['2024-09-01', '2024-09-15']
```

```python
>>> calculate_implementation_dates(["Form D Filing", "Subscription Agreement"], "subscription")
['2024-10-05', '2024-10-20']
```
