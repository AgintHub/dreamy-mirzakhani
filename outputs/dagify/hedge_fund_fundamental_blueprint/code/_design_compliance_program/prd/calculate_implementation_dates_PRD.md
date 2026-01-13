# calculate_implementation_dates PRD

## Description
Calculates implementation dates for a list of accreditation, subscription, or AML items.


## Conceptual Info

The calculate_implementation_dates shim function generates a list of implementation dates for a given list of items and a category.

## Docstring

### Summary
Calculates implementation dates for a list of items based on their category.

### Parameters

- **items** (List[str]): List of accreditation, subscription, or AML items
- **category** (str): Category of items (accreditation, subscription, or aml)

### Returns

List[str]: List of implementation dates in YYYY-MM-DD format

### Raises

- ValueError: When the category is not one of accreditation, subscription, or aml
- TypeError: When the input items are not a list of strings

### Examples

```python
>>> calculate_implementation_dates(items=['item1', 'item2'], category='accreditation')
>>> => ['2024-01-01', '2024-02-01']
['2024-01-01', '2024-02-01']
```

```python
>>> calculate_implementation_dates(items=['item3', 'item4'], category='subscription')
>>> => ['2024-03-01', '2024-04-01']
['2024-03-01', '2024-04-01']
```
