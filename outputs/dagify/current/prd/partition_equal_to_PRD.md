# partition_equal_to PRD

## Description
Create list of elements == pivot


## Conceptual Info

This node creates a list of elements that are equal to the pivot element, which is obtained from the 'select_pivot' function.

## Docstring

### Summary
Creates a list of elements from the input array that are equal to the pivot element.

### Parameters

- **array** (List[int]): The input array to process.
- **pivot** (int): The pivot element to compare with.

### Returns

List[int]: A list of elements equal to the pivot.

### Raises

- ValueError: If the input array is empty.

### Examples

```python
>>> array = [1, 2, 3, 2, 4, 2, 5]
>>> pivot = 2
>>> result = partition_equal(array, pivot)
[2, 2, 2]
```

```python
>>> array = [10, 20, 30, 40, 50]
>>> pivot = 30
>>> result = partition_equal(array, pivot)
[30]
```
