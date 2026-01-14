# combine_sorted_partitions PRD

## Description
Concatenate sorted left + equal + sorted right


## Conceptual Info

The combine_sorted_partitions node merges the three sublists—sorted left, equal elements, and sorted right—into one fully sorted list, forming the core step that assembles the final quicksort result.

## Docstring

### Summary
Concatenates the sorted left partition, the equal-to-pivot partition, and the sorted right partition to produce a single sorted list.

### Parameters

- **sorted_left** (List[int]): A list of integers that has been recursively sorted and contains all elements less than the pivot.
- **equal_elements** (List[int]): A list of integers that are equal to the pivot.
- **sorted_right** (List[int]): A list of integers that has been recursively sorted and contains all elements greater than the pivot.

### Returns

List[int]: A list containing all elements from sorted_left, equal_elements, and sorted_right in that order.

### Raises

- TypeError: If any input is not a list of integers.

### Examples

```python
>>> combine_partitions([1, 2], [3], [4, 5])
[1, 2, 3, 4, 5]
```

```python
>>> combine_partitions([1, 2, 2], [2, 2], [3, 4])
[1, 2, 2, 2, 2, 3, 4]
```
