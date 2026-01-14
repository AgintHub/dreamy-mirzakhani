# sort_right_partition PRD

## Description
Recursively sort greater-than partition


## Conceptual Info

Recursively sort the elements greater than the chosen pivot using quicksort.

## Docstring

### Summary
Recursively applies quicksort to the list of elements greater than the chosen pivot and returns the sorted list.

### Parameters

- **greater_than_partition** (List[int]): The list of elements greater than the pivot that need to be sorted.

### Returns

List[int]: A sorted list of the elements that were greater than the pivot.

### Raises

- ValueError: If 'greater_than_partition' is not a list or contains non-integer elements.

### Examples

```python
>>> sorted_list = sort_right([3, 1, 4])
[1, 3, 4]
```

```python
>>> sorted_list = sort_right([])
[]
```
