# sort_right_partition PRD

## Description
Recursively sort greater-than partition


## Conceptual Info

This node takes the list of elements greater than the chosen pivot and recursively applies the quicksort algorithm to produce a fully sorted list of those elements.

## Docstring

### Summary
Recursively sorts the partition containing elements greater than the pivot using the quicksort algorithm.

### Parameters

- **greater_than_partition** (List[int]): List of integers that are strictly greater than the pivot element.

### Returns

List[int]: A new list containing the elements from `greater_than_partition` sorted in non‑decreasing order.

### Raises

- ValueError: If an element in `greater_than_partition` is not an integer.

### Examples

```python
>>> def sort_right(greater_than_partition):
...     if len(greater_than_partition) <= 1:
...         return greater_than_partition
...     pivot = greater_than_partition[0]
...     less = [x for x in greater_than_partition[1:] if x < pivot]
...     equal = [x for x in greater_than_partition[1:] if x == pivot]
...     greater = [x for x in greater_than_partition[1:] if x > pivot]
...     return sort_right(less) + [pivot] + equal + sort_right(greater)
[2, 3, 5, 8]
```

```python
>>> print(sort_right([9, 7, 10, 8]))
[7, 8, 9, 10]
```
