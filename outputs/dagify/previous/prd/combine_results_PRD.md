# combine_results PRD

## Description
Combine the sorted left partition, the equal pivot partition, and the sorted right partition into a single, fully sorted list.


## Conceptual Info

This node assembles the results of the recursive quicksort steps. It takes three pieces: the sorted elements less than the pivot, the elements equal to the pivot (the pivot value replicated as needed), and the sorted elements greater than the pivot. By concatenating these three lists, it yields the final sorted sequence for the current recursive call.

## Docstring

### Summary
Merge three parts (sorted less, equal pivot, sorted greater) into the final sorted list.

### Parameters

- **sorted_less** (List[int]): The sorted sublist of elements that are less than the pivot.
- **equal** (List[int]): The list of elements from the input that are exactly equal to the pivot value.
- **sorted_greater_sublist** (List[int]): The sorted sublist of elements that are greater than the pivot.

### Returns

List[int]: The final concatenated list representing the sorted sequence for this partition.

### Raises

- TypeError: If any input is not a list of integers.
- ValueError: If inputs contain non-integer elements.

### Examples

```python
>>> combine_results([1, 2], [3, 3], [4, 5, 6])
[1, 2, 3, 3, 4, 5, 6]
```

```python
>>> combine_results([], [], [7, 8, 9])
[7, 8, 9]
```
