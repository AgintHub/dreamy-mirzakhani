# merge_sort_recursively - Complete PRD Documentation

## Overview
PRDs for nodes in the 'merge_sort_recursively' module.

## Table of Contents

- [define_base_case](#define_base_case)

- [define_merge_function](#define_merge_function)

- [define_recursive_case](#define_recursive_case)

- [define_split_function](#define_split_function)



---

## define_base_case

### Description
Define the base case for the recursive merge sort function.

### Conceptual Info

The base case for the recursive merge sort function defines whether a list is already sorted and has a length of 1 or less.

### Docstring

**Summary:** Determines if a list is a base case for the recursive merge sort function.

**Parameters:**

- input_list (List[str]): The input list to be sorted.
**Returns:** bool - Whether the input list is a base case (i.e., length 1 or less).

**Examples:**

```python
>>> define_base_case([1])
>>> define_base_case([])
True
True
```



---

## define_merge_function

### Description
This node defines a function to merge two sorted lists into one sorted sorted list. It takes two sorted integer lists and combines them efficiently to produce a single sorted list, maintaining order.

### Conceptual Info

This node implements the merging step needed for the merge sort algorithm, combining two sorted lists into one sorted list efficiently.

### Docstring

**Summary:** Merges two sorted lists into a single sorted list.

**Parameters:**

- input_list1 (List[int]): First sorted list of integers.
- input_list2 (List[int]): Second sorted list of integers.
**Returns:** List[int] - A single sorted list containing all elements from both input lists.

**Raises:**

- TypeError: Raised if either input is not a list of integers.
**Examples:**

```python
>>> merge_lists([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
```

```python
>>> merge_lists([1, 2], [3, 4])
[1, 2, 3, 4]
```



---

## define_recursive_case

### Description
Define the recursive case for the merge sort function.

### Conceptual Info

The recursive case for the merge sort function, which recursively splits the input list into two halves, sorts each half, and then merges the two sorted halves.

### Docstring

**Summary:** Define the recursive case for the merge sort function, which splits the input list into two halves, recursively sorts each half, and then merges the two sorted halves.

**Parameters:**

- input_list (List[int]): The input list to be recursively sorted.
- recursion_depth (int): The current recursion depth of the merge sort function.
**Returns:** List[List[int]] - The two sorted halves of the input list.

**Raises:**

- ValueError: If the input list is not a list of integers.
**Examples:**

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



---

## define_split_function

### Description
Define a function to split a list into two halves.

### Conceptual Info

Splits a list into two halves.

### Docstring

**Summary:** Splits a list into two halves.

**Parameters:**

- input_list (List[Int]): The list to be split.
**Returns:** Tuple[List[Int], List[Int]] - A tuple containing the two halves of the input list.

**Raises:**

- ValueError: If the input list is None or empty.
**Examples:**

```python
>>> def split_list(input_list):
...   mid_index = len(input_list) // 2
...   return input_list[:mid_index], input_list[mid_index:]
([0, 1, 2], [3, 4, 5])
```

```python
>>> list_to_split = [1, 2, 3, 4, 5]
>>> left_half, right_half = split_list(list_to_split)
([1, 2], [3, 4, 5])
```

