# partition_greater_than PRD

## Description
Create list of elements > pivot


## Conceptual Info

Filters elements from the input array that are strictly greater than the selected pivot, used for partitioning in the quicksort workflow.

## Docstring

### Summary
Returns a list of elements from the input array that are strictly greater than the given pivot.

### Parameters

- **array** (List[int]): The unmodified input array from which to filter elements (does not exclude the pivot itself).
- **pivot** (int): The pivot value selected by 'select_first_element_pivot', used as the comparison threshold.

### Returns

List[int]: A new list containing only elements from the input array with values > pivot, preserving original order.

### Raises

- ValueError: If the input array is empty (though unlikely due to upstream 'base_case_check').

### Examples

```python
>>> partition_greater_than([5, 3, 8, 1, 6], 5)
[8, 6]
```

```python
>>> partition_greater_than([5, 5, 5], 5)
[]
```
