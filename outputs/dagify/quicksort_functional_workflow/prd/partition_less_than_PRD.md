# partition_less_than PRD

## Description
Create list of elements < pivot


## Conceptual Info

Filters the input array to produce a new list containing only elements strictly less than the selected pivot value. This is a core partitioning step in the quicksort algorithm.

## Docstring

### Summary
Returns a list of all elements in the input array that are strictly less than the specified pivot value.

### Parameters

- **array** (List[int]): The input list of integers to filter.
- **pivot** (int): The pivot value for comparison, selected via the parent node.

### Returns

List[int]: A list containing all elements from 'array' that are less than 'pivot'.

### Raises

- ValueError: If input array is empty (validated by parent nodes).

### Examples

```python
>>> partition_less_than([3,1,2], 3)
{'less_than_elements': [1, 2]}
```

```python
>>> partition_less_than([5,4,5,6], 5)
{'less_than_elements': [4]}
```
