# quicksort_functional_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'quicksort_functional_workflow' module.

## Table of Contents

- [base_case_check](#base_case_check)

- [combine_sorted_partitions](#combine_sorted_partitions)

- [partition_equal_to](#partition_equal_to)

- [partition_greater_than](#partition_greater_than)

- [partition_less_than](#partition_less_than)

- [select_first_element_pivot](#select_first_element_pivot)

- [sort_left_partition](#sort_left_partition)

- [sort_right_partition](#sort_right_partition)



---

## base_case_check

### Description
Check if array is empty and return it directly if true

### Conceptual Info

Determines whether a list of integers is empty and propagates the list unchanged, providing a boolean flag for downstream logic.

### Docstring

**Summary:** Return the input list unchanged while indicating if it is empty.

**Parameters:**

- array (List[int]): List of integers to be checked.
**Returns:** Tuple[bool, List[int]] - A tuple containing a boolean flag `is_empty` and the original input list `output_array`.

**Raises:**

- TypeError: If the input is not a list or contains non-integer elements.
**Examples:**

```python
>>> is_empty, output_array = base_case_check([3, 1, 4])
False
[3, 1, 4]
```

```python
>>> is_empty, output_array = base_case_check([])
True
[]
```



---

## combine_sorted_partitions

### Description
Concatenate sorted left + equal + sorted right

### Conceptual Info

This node combines three sorted partitions into a single sorted list.

### Docstring

**Summary:** Concatenates sorted left, equal, and sorted right partitions into a single sorted list.

**Parameters:**

- sorted_left (List[int]): Sorted list of elements less than the pivot.
- equal_elements (List[int]): List of elements equal to the pivot.
- sorted_right (List[int]): Sorted list of elements greater than the pivot.
**Returns:** List[int] - The fully concatenated sorted list.

**Examples:**

```python
>>> combine_sorted_partitions([1, 3], [2, 2], [4, 5])
[1, 3, 2, 2, 4, 5]
```

```python
>>> combine_sorted_partitions([], [1], [2, 3])
[1, 2, 3]
```



---

## partition_equal_to

### Description
Create list of elements == pivot

### Conceptual Info

This node creates a list of elements that are equal to the pivot element, which is obtained from the 'select_pivot' function.

### Docstring

**Summary:** Creates a list of elements from the input array that are equal to the pivot element.

**Parameters:**

- array (List[int]): The input array to process.
- pivot (int): The pivot element to compare with.
**Returns:** List[int] - A list of elements equal to the pivot.

**Raises:**

- ValueError: If the input array is empty.
**Examples:**

```python
>>> array = [1, 2, 3, 2, 4, 2, 5]
>>> pivot = 2
>>> result = partition_equal(array, pivot)
[2, 2, 2]
```

```python
>>> array = [10, 20, 30, 40, 50]
>>> pivot = 30
>>> result = partition_equal(array, pivot)
[30]
```



---

## partition_greater_than

### Description
Create list of elements > pivot

### Conceptual Info

This node is responsible for partitioning the input array into elements greater than the pivot.

### Docstring

**Summary:** Partitions the input array into elements greater than the pivot.

**Parameters:**

- array (List[int]): The input array to be partitioned.
- pivot (int): The pivot element to partition around.
**Returns:** List[int] - A list of elements greater than the pivot.

**Raises:**

- ValueError: If the input array is empty.
**Examples:**

```python
>>> array = [3, 6, 8, 10, 1, 4, 7]
>>> pivot = 6
>>> greater_than_partition = partition_greater(array, pivot)
[8, 10, 7]
```

```python
>>> array = [1, 2, 3, 4, 5]
>>> pivot = 3
>>> greater_than_partition = partition_greater(array, pivot)
[4, 5]
```



---

## partition_less_than

### Description
Create list of elements < pivot

### Conceptual Info

Partitions the input array into elements less than the given pivot.

### Docstring

**Summary:** Partitions the input array into elements less than the given pivot.

**Parameters:**

- array (List[int]): The input array to be partitioned.
- pivot (int): The pivot element used for partitioning.
**Returns:** List[int] - A list of elements less than the pivot.

**Examples:**

```python
>>> partition_less_than([3, 1, 4, 1, 5, 9, 2], 5)
[3, 1, 4, 1, 2]
```

```python
>>> partition_less_than([5, 5, 5], 5)
[]
```



---

## select_first_element_pivot

### Description
Select first element as pivot

### Conceptual Info

This node selects the first element of a non-empty array as the pivot for further processing.

### Docstring

**Summary:** Selects the first element of a non-empty array as the pivot.

**Parameters:**

- array (List[int]): A non-empty array of integers
**Returns:** Tuple[int, int] - A tuple containing the pivot element and its index in the original array

**Raises:**

- ValueError: If the input array is empty
**Examples:**

```python
>>> array = [5, 2, 8, 3]
>>> pivot, pivot_index = select_pivot(array)
(5, 0)
```

```python
>>> array = [10, 7, 4, 1]
>>> pivot, pivot_index = select_pivot(array)
(10, 0)
```



---

## sort_left_partition

### Description
Recursively sort the elements that are less than the pivot.

### Conceptual Info

The `sort_left` function implements the left‑partition recursion of the functional quicksort algorithm. It takes the list of elements that are smaller than the chosen pivot (produced by `partition_less_than`) and returns that sub‑list sorted in ascending order.

### Docstring

**Summary:** Recursively sort the sub‑list of elements less than the pivot using quicksort.

**Parameters:**

- less_than_elements (List[int]): A list of integers that are strictly smaller than the pivot selected by `select_first_element_pivot`.
**Returns:** List[int] - A new list containing the same integers as `less_than_elements`, but sorted in non‑decreasing order.

**Raises:**

- ValueError: If an element in `less_than_elements` is not an integer.
**Examples:**

```python
>>> sorted_left = sort_left([5, 2, 3])
>>> print(sorted_left)
[2, 3, 5]
```

```python
>>> sorted_left = sort_left([])
>>> print(sorted_left)
[]
```



---

## sort_right_partition

### Description
Recursively sort greater-than partition

### Conceptual Info

This node takes the list of elements greater than the chosen pivot and recursively applies the quicksort algorithm to produce a fully sorted list of those elements.

### Docstring

**Summary:** Recursively sorts the partition containing elements greater than the pivot using the quicksort algorithm.

**Parameters:**

- greater_than_partition (List[int]): List of integers that are strictly greater than the pivot element.
**Returns:** List[int] - A new list containing the elements from `greater_than_partition` sorted in non‑decreasing order.

**Raises:**

- ValueError: If an element in `greater_than_partition` is not an integer.
**Examples:**

```python
>>> def sort_right(greater_than_partition):
...     if len(greater_than_partition) <= 1:
...         return greater_than_partition
...     pivot = greater_than_partition[0]
...     less = [x for x in greater_than_partition[1:] if x < pivot]
...     equal = [x for x in greater_than_partition[1:] if x == pivot]
...     greater = [x for x in greater_than_partition[1:] if x > pivot]
...     return sort_right(less) + [pivot] + equal + sort_right(greater)
[2, 3, 5, 8]
```

```python
>>> print(sort_right([9, 7, 10, 8]))
[7, 8, 9, 10]
```

