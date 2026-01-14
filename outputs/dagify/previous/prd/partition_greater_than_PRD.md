# partition_greater_than PRD

## Description
Create list of elements > pivot


## Conceptual Info

This node is responsible for partitioning the input array into elements greater than the pivot.

## Docstring

### Summary
Partitions the input array into elements greater than the pivot.

### Parameters

- **array** (List[int]): The input array to be partitioned.
- **pivot** (int): The pivot element to partition around.

### Returns

List[int]: A list of elements greater than the pivot.

### Raises

- ValueError: If the input array is empty.

### Examples

```python
>>> array = [3, 6, 8, 10, 1, 4, 7]
>>> pivot = 6
>>> greater_than_partition = partition_greater(array, pivot)
[8, 10, 7]
```

```python
>>> array = [1, 2, 3, 4, 5]
>>> pivot = 3
>>> greater_than_partition = partition_greater(array, pivot)
[4, 5]
```
