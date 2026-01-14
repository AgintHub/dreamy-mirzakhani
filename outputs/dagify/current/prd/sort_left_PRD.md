# sort_left PRD

## Description
Recursively apply quicksort to the left (less than pivot) partition.


## Conceptual Info

The `sort_left` node receives the `less` partition from `partition_list`, recursively sorts it using the same quicksort workflow, and outputs the sorted left sublist. It is a core recursive step that ensures all elements smaller than the current pivot end up in order before final concatenation.

## Docstring

### Summary
Recursively sorts the 'less' partition of a list using the quicksort algorithm.

### Parameters

- **less** (List[int]): List of integers that are smaller than the current pivot, obtained from the `partition_list` node.

### Returns

List[int]: A new list containing the elements of `less` sorted in ascending order.

### Raises

- TypeError: If `less` is not a list of integers.
- RecursionError: If the recursion depth exceeds Python's limit, indicating a possible non‑terminating input.

### Examples

```python
>>> sorted_less = sort_left([3, 1, 4, 2])
[1, 2, 3, 4]
```

```python
>>> sorted_less = sort_left([])
[]
```
