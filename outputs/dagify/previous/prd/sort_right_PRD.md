# sort_right PRD

## Description
Recursively apply quicksort to the right (greater than pivot) partition.


## Conceptual Info

This node receives the 'greater' partition from `partition_list` and recursively sorts it using the quicksort algorithm, returning the sorted sub‑list.

## Docstring

### Summary
Recursively quicksort the sub‑list of elements greater than the pivot.

### Parameters

- **greater_sublist** (List[int]): List of integers that are greater than the current pivot, produced by the `partition_list` node.

### Returns

List[int]: The input sub‑list sorted in ascending order.

### Raises

- TypeError: If `greater_sublist` is not a list of integers.
- RecursionError: If the recursion depth exceeds Python's limit due to malformed input.

### Examples

```python
>>> sorted_right = sort_right([9, 7, 5, 8])
[5, 7, 8, 9]
```

```python
>>> sort_right([])
[]
```
