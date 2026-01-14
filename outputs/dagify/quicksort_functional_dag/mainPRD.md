# quicksort_functional_dag - Complete PRD Documentation

## Overview
PRDs for nodes in the 'quicksort_functional_dag' module.

## Table of Contents

- [combine_results](#combine_results)

- [partition_list](#partition_list)

- [select_pivot](#select_pivot)

- [sort_left](#sort_left)

- [sort_right](#sort_right)



---

## combine_results

### Description
Combine the sorted left partition, the equal pivot partition, and the sorted right partition into a single, fully sorted list.

### Conceptual Info

This node assembles the results of the recursive quicksort steps. It takes three pieces: the sorted elements less than the pivot, the elements equal to the pivot (the pivot value replicated as needed), and the sorted elements greater than the pivot. By concatenating these three lists, it yields the final sorted sequence for the current recursive call.

### Docstring

**Summary:** Merge three parts (sorted less, equal pivot, sorted greater) into the final sorted list.

**Parameters:**

- sorted_less (List[int]): The sorted sublist of elements that are less than the pivot.
- equal (List[int]): The list of elements from the input that are exactly equal to the pivot value.
- sorted_greater_sublist (List[int]): The sorted sublist of elements that are greater than the pivot.
**Returns:** List[int] - The final concatenated list representing the sorted sequence for this partition.

**Raises:**

- TypeError: If any input is not a list of integers.
- ValueError: If inputs contain non-integer elements.
**Examples:**

```python
>>> combine_results([1, 2], [3, 3], [4, 5, 6])
[1, 2, 3, 3, 4, 5, 6]
```

```python
>>> combine_results([], [], [7, 8, 9])
[7, 8, 9]
```



---

## partition_list

### Description
Partition the list into elements less than, equal to, and greater than the pivot.

### Conceptual Info

Divides an unsorted integer list into three distinct sub‑lists based on a pivot value supplied by the parent node. This is the core partition step of the quick‑sort algorithm.

### Docstring

**Summary:** Partition a list of integers into three groups relative to a pivot value: less than, equal to, and greater than the pivot.

**Parameters:**

- input_list (List[int]): The unsorted list of integers to be partitioned.
- pivot (int): The pivot value around which the list is partitioned. Obtained from the `select_pivot` node.
**Returns:** Dict[str, List[int]] - A dictionary with keys 'less', 'equal', and 'greater' mapping to the respective sub‑lists of integers.

**Raises:**

- TypeError: If `input_list` is not a list of integers or if `pivot` is not an integer.
- ValueError: If `input_list` is empty.
**Examples:**

```python
>>> partition_list([9, 3, 5, 2, 8, 5, 1], 5)
{'less': [3, 2, 1], 'equal': [5, 5], 'greater': [9, 8]}
```

```python
>>> partition_list([4, 4, 4], 4)
{'less': [], 'equal': [4, 4, 4], 'greater': []}
```



---

## select_pivot

### Description
Select a pivot element from the unsorted list.

### Conceptual Info

The node extracts a single pivot value from an input list of integers, typically the first element, and returns it wrapped in a one‑element list. This pivot is later used to partition the list for the quicksort algorithm.

### Docstring

**Summary:** Select the pivot element for quicksort.

The function receives an unsorted list of integers and returns a one‑element list containing the chosen pivot value. By convention the first element of the input list is used as the pivot, but the implementation may be changed without affecting downstream nodes as long as the return type remains a single‑element integer list.

**Parameters:**

- unsorted_list (list[int]): The list of integers from which the pivot will be selected. Must contain at least one element.
**Returns:** list[int] - A list of length 1 whose sole element is the selected pivot value.

**Raises:**

- ValueError: If ``unsorted_list`` is empty, because a pivot cannot be selected from an empty collection.
- TypeError: If ``unsorted_list`` is not a list of integers.
**Examples:**

```python
>>> select_pivot([7, 3, 9, 1])
[7]
```

```python
>>> select_pivot([42])
[42]
```



---

## sort_left

### Description
Recursively apply quicksort to the left (less than pivot) partition.

### Conceptual Info

The `sort_left` node receives the `less` partition from `partition_list`, recursively sorts it using the same quicksort workflow, and outputs the sorted left sublist. It is a core recursive step that ensures all elements smaller than the current pivot end up in order before final concatenation.

### Docstring

**Summary:** Recursively sorts the 'less' partition of a list using the quicksort algorithm.

**Parameters:**

- less (List[int]): List of integers that are smaller than the current pivot, obtained from the `partition_list` node.
**Returns:** List[int] - A new list containing the elements of `less` sorted in ascending order.

**Raises:**

- TypeError: If `less` is not a list of integers.
- RecursionError: If the recursion depth exceeds Python's limit, indicating a possible non‑terminating input.
**Examples:**

```python
>>> sorted_less = sort_left([3, 1, 4, 2])
[1, 2, 3, 4]
```

```python
>>> sorted_less = sort_left([])
[]
```



---

## sort_right

### Description
Recursively apply quicksort to the right (greater than pivot) partition.

### Conceptual Info

This node receives the 'greater' partition from `partition_list` and recursively sorts it using the quicksort algorithm, returning the sorted sub‑list.

### Docstring

**Summary:** Recursively quicksort the sub‑list of elements greater than the pivot.

**Parameters:**

- greater_sublist (List[int]): List of integers that are greater than the current pivot, produced by the `partition_list` node.
**Returns:** List[int] - The input sub‑list sorted in ascending order.

**Raises:**

- TypeError: If `greater_sublist` is not a list of integers.
- RecursionError: If the recursion depth exceeds Python's limit due to malformed input.
**Examples:**

```python
>>> sorted_right = sort_right([9, 7, 5, 8])
[5, 7, 8, 9]
```

```python
>>> sort_right([])
[]
```

