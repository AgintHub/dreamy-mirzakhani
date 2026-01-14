# select_first_element_pivot PRD

## Description
Select first element as pivot


## Conceptual Info

This node selects the first element of a non-empty array as the pivot for further processing.

## Docstring

### Summary
Selects the first element of a non-empty array as the pivot.

### Parameters

- **array** (List[int]): A non-empty array of integers

### Returns

Tuple[int, int]: A tuple containing the pivot element and its index in the original array

### Raises

- ValueError: If the input array is empty

### Examples

```python
>>> array = [5, 2, 8, 3]
>>> pivot, pivot_index = select_pivot(array)
(5, 0)
```

```python
>>> array = [10, 7, 4, 1]
>>> pivot, pivot_index = select_pivot(array)
(10, 0)
```
