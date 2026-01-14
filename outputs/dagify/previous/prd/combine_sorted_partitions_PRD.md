# combine_sorted_partitions PRD

## Description
Concatenate sorted left + equal + sorted right


## Conceptual Info

This node combines three sorted partitions into a single sorted list.

## Docstring

### Summary
Concatenates sorted left, equal, and sorted right partitions into a single sorted list.

### Parameters

- **sorted_left** (List[int]): Sorted list of elements less than the pivot.
- **equal_elements** (List[int]): List of elements equal to the pivot.
- **sorted_right** (List[int]): Sorted list of elements greater than the pivot.

### Returns

List[int]: The fully concatenated sorted list.

### Examples

```python
>>> combine_sorted_partitions([1, 3], [2, 2], [4, 5])
[1, 3, 2, 2, 4, 5]
```

```python
>>> combine_sorted_partitions([], [1], [2, 3])
[1, 2, 3]
```
