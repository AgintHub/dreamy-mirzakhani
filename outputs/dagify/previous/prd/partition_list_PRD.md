# partition_list PRD

## Description
Partition the list into elements less than, equal to, and greater than the pivot.


## Conceptual Info

Divides an unsorted integer list into three distinct sub‑lists based on a pivot value supplied by the parent node. This is the core partition step of the quick‑sort algorithm.

## Docstring

### Summary
Partition a list of integers into three groups relative to a pivot value: less than, equal to, and greater than the pivot.

### Parameters

- **input_list** (List[int]): The unsorted list of integers to be partitioned.
- **pivot** (int): The pivot value around which the list is partitioned. Obtained from the `select_pivot` node.

### Returns

Dict[str, List[int]]: A dictionary with keys 'less', 'equal', and 'greater' mapping to the respective sub‑lists of integers.

### Raises

- TypeError: If `input_list` is not a list of integers or if `pivot` is not an integer.
- ValueError: If `input_list` is empty.

### Examples

```python
>>> partition_list([9, 3, 5, 2, 8, 5, 1], 5)
{'less': [3, 2, 1], 'equal': [5, 5], 'greater': [9, 8]}
```

```python
>>> partition_list([4, 4, 4], 4)
{'less': [], 'equal': [4, 4, 4], 'greater': []}
```
