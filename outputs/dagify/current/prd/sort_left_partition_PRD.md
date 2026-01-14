# sort_left_partition PRD

## Description
Recursively sort the elements that are less than the pivot.


## Conceptual Info

The `sort_left` function implements the left‑partition recursion of the functional quicksort algorithm. It takes the list of elements that are smaller than the chosen pivot (produced by `partition_less_than`) and returns that sub‑list sorted in ascending order.

## Docstring

### Summary
Recursively sort the sub‑list of elements less than the pivot using quicksort.

### Parameters

- **less_than_elements** (List[int]): A list of integers that are strictly smaller than the pivot selected by `select_first_element_pivot`.

### Returns

List[int]: A new list containing the same integers as `less_than_elements`, but sorted in non‑decreasing order.

### Raises

- ValueError: If an element in `less_than_elements` is not an integer.

### Examples

```python
>>> sorted_left = sort_left([5, 2, 3])
>>> print(sorted_left)
[2, 3, 5]
```

```python
>>> sorted_left = sort_left([])
>>> print(sorted_left)
[]
```
