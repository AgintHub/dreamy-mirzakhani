# select_first_element_pivot PRD

## Description
Select first element as pivot


## Conceptual Info

Selects the first element of a non-empty array as the pivot for quicksort. This provides a deterministic pivot choice and tracks its original index for partitioning.

## Docstring

### Summary
Returns the first element of a non-empty array as the pivot value and its index.

### Parameters

- **arr** (List[int]): Non-empty array from base_case_check validation. Assumed to contain only integers.

### Returns

Tuple[int, int]: Tuple where first element is the pivot value (int) and second is the pivot index (int, always 0).

### Raises

- ValueError: If input array is empty. Note: This should never occur as base_case_check already validates non-emptiness.

### Examples

```python
>>> select_pivot([7, 2, 5, 1])
(7, 0)
```

```python
>>> select_pivot([42])
(42, 0)
```
