# select_pivot PRD

## Description
Select a pivot element from the unsorted list.


## Conceptual Info

The node extracts a single pivot value from an input list of integers, typically the first element, and returns it wrapped in a one‑element list. This pivot is later used to partition the list for the quicksort algorithm.

## Docstring

### Summary
Select the pivot element for quicksort.

The function receives an unsorted list of integers and returns a one‑element list containing the chosen pivot value. By convention the first element of the input list is used as the pivot, but the implementation may be changed without affecting downstream nodes as long as the return type remains a single‑element integer list.

### Parameters

- **unsorted_list** (list[int]): The list of integers from which the pivot will be selected. Must contain at least one element.

### Returns

list[int]: A list of length 1 whose sole element is the selected pivot value.

### Raises

- ValueError: If ``unsorted_list`` is empty, because a pivot cannot be selected from an empty collection.
- TypeError: If ``unsorted_list`` is not a list of integers.

### Examples

```python
>>> select_pivot([7, 3, 9, 1])
[7]
```

```python
>>> select_pivot([42])
[42]
```
