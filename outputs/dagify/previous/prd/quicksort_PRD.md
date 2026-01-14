# quicksort PRD

## Description
Main quicksort function that executes full sorting workflow


## Conceptual Info

The quicksort node implements the full quicksort sorting algorithm. It orchestrates the workflow defined by the preceding nodes: it first checks for the base case (empty array), then selects the first element as a pivot, partitions the remaining elements into less‑than, equal, and greater‑than groups, recursively sorts the less and greater partitions, and finally concatenates the sorted left partition, the pivot group, and the sorted right partition into the final sorted list.

## Docstring

### Summary
Recursively sorts a list of integers using the quicksort algorithm.

### Parameters

- **array** (List[int]): The list of integers to be sorted.

### Returns

List[int]: A new list containing the elements of `array` sorted in non‑decreasing order.

### Raises

- TypeError: If `array` is not a list.
- ValueError: If any element of `array` is not an integer.

### Examples

```python
>>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]
```

```python
>>> quicksort([])
[]
```
