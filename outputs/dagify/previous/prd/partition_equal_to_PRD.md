# partition_equal_to PRD

## Description
Create list of elements == pivot


## Conceptual Info

Filters the original array to extract all elements strictly equal to the selected pivot value.

## Docstring

### Summary
Extracts elements from the array that are equal to the provided pivot value.

### Parameters

- **array** (List[int]): The original array to partition after base case check and pivot selection
- **pivot** (int): The pivot value selected by the select_first_element_pivot node

### Returns

List[int]: A list containing only the elements from the array equal to the pivot

### Examples

```python
>>> partition_equal_to([3,2,1,3,4], pivot=3)
[3, 3]
```

```python
>>> partition_equal_to([5,5,5], pivot=5)
[5, 5, 5]
```
