# sort_left_partition PRD

## Description
Recursively sort the elements that are less than the pivot.


## Conceptual Info

Recursively sorts a list of elements less than a pivot using the quicksort algorithm, as part of a functional decomposition.

## Docstring

### Summary
Applies a recursive quicksort to the output of the 'partition_less_than' node, returning a sorted list.

### Parameters

- **less_than_elements** (List[int]): List of integers less than the pivot from the 'partition_less_than' node output

### Returns

List[int]: A sorted list of integers produced by recursively applying the quicksort algorithm

### Examples

```python
>>> sort_left([3, 1, 2])
[1, 2, 3]
```

```python
>>> sort_left([5, 4, 3])
[3, 4, 5]
```
