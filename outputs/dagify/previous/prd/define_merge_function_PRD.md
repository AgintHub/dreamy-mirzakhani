# define_merge_function PRD

## Description
This node defines a function to merge two sorted lists into one sorted sorted list. It takes two sorted integer lists and combines them efficiently to produce a single sorted list, maintaining order.


## Conceptual Info

This node implements the merging step needed for the merge sort algorithm, combining two sorted lists into one sorted list efficiently.

## Docstring

### Summary
Merges two sorted lists into a single sorted list.

### Parameters

- **input_list1** (List[int]): First sorted list of integers.
- **input_list2** (List[int]): Second sorted list of integers.

### Returns

List[int]: A single sorted list containing all elements from both input lists.

### Raises

- TypeError: Raised if either input is not a list of integers.

### Examples

```python
>>> merge_lists([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
```

```python
>>> merge_lists([1, 2], [3, 4])
[1, 2, 3, 4]
```
