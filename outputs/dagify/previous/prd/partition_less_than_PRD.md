# partition_less_than PRD

## Description
Create list of elements < pivot


## Conceptual Info

Partitions the input array into elements less than the given pivot.

## Docstring

### Summary
Partitions the input array into elements less than the given pivot.

### Parameters

- **array** (List[int]): The input array to be partitioned.
- **pivot** (int): The pivot element used for partitioning.

### Returns

List[int]: A list of elements less than the pivot.

### Examples

```python
>>> partition_less_than([3, 1, 4, 1, 5, 9, 2], 5)
[3, 1, 4, 1, 2]
```

```python
>>> partition_less_than([5, 5, 5], 5)
[]
```
