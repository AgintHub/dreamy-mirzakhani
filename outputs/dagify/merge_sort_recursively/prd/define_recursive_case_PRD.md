# define_recursive_case PRD

## Description
Define the recursive case for the merge sort function.


## Conceptual Info

The recursive case for the merge sort function, which recursively splits the input list into two halves, sorts each half, and then merges the two sorted halves.

## Docstring

### Summary
Define the recursive case for the merge sort function, which splits the input list into two halves, recursively sorts each half, and then merges the two sorted halves.

### Parameters

- **input_list** (List[int]): The input list to be recursively sorted.
- **recursion_depth** (int): The current recursion depth of the merge sort function.

### Returns

List[List[int]]: The two sorted halves of the input list.

### Raises

- ValueError: If the input list is not a list of integers.

### Examples

```python
>>> sorted_halves = define_recursive_case([1, 3, 5, 7, 9])
>>> print(sorted_halves)
[[1, 3, 5], [7, 9]]
```

```python
>>> sorted_halves = define_recursive_case([2, 4, 6, 8, 10])
>>> print(sorted_halves)
[[2, 4, 6], [8, 10]]
```
