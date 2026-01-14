# quicksort_functional_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'quicksort_functional_workflow' module.

## Table of Contents

- [base_case_check](#base_case_check)

- [select_first_element_pivot](#select_first_element_pivot)

- [partition_less_than](#partition_less_than)

- [partition_equal_to](#partition_equal_to)

- [partition_greater_than](#partition_greater_than)

- [sort_left_partition](#sort_left_partition)

- [sort_right_partition](#sort_right_partition)

- [combine_sorted_partitions](#combine_sorted_partitions)

- [quicksort](#quicksort)



---

## base_case_check

### Description
Check if array is empty and return it directly if true

### Conceptual Info

This node serves as the quicksort algorithm's base case checker, immediately returning empty arrays to terminate recursion for efficiency.

### Docstring

**Summary:** Check if input array is empty and return a tuple with boolean flag and array. Returns same array regardless of emptiness for non-empty cases.

**Parameters:**

- array (List[int]): Input list of integers to check for emptiness
**Returns:** Tuple[bool, List[int]] - is_empty: Boolean indicating array emptiness, output_array: Same input array or empty list

**Examples:**

```python
>>> base_case_check([])
{'is_empty': True, 'output_array': []}
```

```python
>>> base_case_check([3, 1, 4])
{'is_empty': False, 'output_array': [3, 1, 4]}
```



---

## select_first_element_pivot

### Description
Select first element as pivot

### Conceptual Info

Selects the first element of a non-empty array as the pivot for quicksort. This provides a deterministic pivot choice and tracks its original index for partitioning.

### Docstring

**Summary:** Returns the first element of a non-empty array as the pivot value and its index.

**Parameters:**

- arr (List[int]): Non-empty array from base_case_check validation. Assumed to contain only integers.
**Returns:** Tuple[int, int] - Tuple where first element is the pivot value (int) and second is the pivot index (int, always 0).

**Raises:**

- ValueError: If input array is empty. Note: This should never occur as base_case_check already validates non-emptiness.
**Examples:**

```python
>>> select_pivot([7, 2, 5, 1])
(7, 0)
```

```python
>>> select_pivot([42])
(42, 0)
```



---

## partition_less_than

### Description
Create list of elements < pivot

### Conceptual Info

Filters the input array to produce a new list containing only elements strictly less than the selected pivot value. This is a core partitioning step in the quicksort algorithm.

### Docstring

**Summary:** Returns a list of all elements in the input array that are strictly less than the specified pivot value.

**Parameters:**

- array (List[int]): The input list of integers to filter.
- pivot (int): The pivot value for comparison, selected via the parent node.
**Returns:** List[int] - A list containing all elements from 'array' that are less than 'pivot'.

**Raises:**

- ValueError: If input array is empty (validated by parent nodes).
**Examples:**

```python
>>> partition_less_than([3,1,2], 3)
{'less_than_elements': [1, 2]}
```

```python
>>> partition_less_than([5,4,5,6], 5)
{'less_than_elements': [4]}
```



---

## partition_equal_to

### Description
Create list of elements == pivot

### Conceptual Info

Filters the original array to extract all elements strictly equal to the selected pivot value.

### Docstring

**Summary:** Extracts elements from the array that are equal to the provided pivot value.

**Parameters:**

- array (List[int]): The original array to partition after base case check and pivot selection
- pivot (int): The pivot value selected by the select_first_element_pivot node
**Returns:** List[int] - A list containing only the elements from the array equal to the pivot

**Examples:**

```python
>>> partition_equal_to([3,2,1,3,4], pivot=3)
[3, 3]
```

```python
>>> partition_equal_to([5,5,5], pivot=5)
[5, 5, 5]
```



---

## partition_greater_than

### Description
Create list of elements > pivot

### Conceptual Info

Filters elements from the input array that are strictly greater than the selected pivot, used for partitioning in the quicksort workflow.

### Docstring

**Summary:** Returns a list of elements from the input array that are strictly greater than the given pivot.

**Parameters:**

- array (List[int]): The unmodified input array from which to filter elements (does not exclude the pivot itself).
- pivot (int): The pivot value selected by 'select_first_element_pivot', used as the comparison threshold.
**Returns:** List[int] - A new list containing only elements from the input array with values > pivot, preserving original order.

**Raises:**

- ValueError: If the input array is empty (though unlikely due to upstream 'base_case_check').
**Examples:**

```python
>>> partition_greater_than([5, 3, 8, 1, 6], 5)
[8, 6]
```

```python
>>> partition_greater_than([5, 5, 5], 5)
[]
```



---

## sort_left_partition

### Description
Recursively sort the elements that are less than the pivot.

### Conceptual Info

Recursively sorts a list of elements less than a pivot using the quicksort algorithm, as part of a functional decomposition.

### Docstring

**Summary:** Applies a recursive quicksort to the output of the 'partition_less_than' node, returning a sorted list.

**Parameters:**

- less_than_elements (List[int]): List of integers less than the pivot from the 'partition_less_than' node output
**Returns:** List[int] - A sorted list of integers produced by recursively applying the quicksort algorithm

**Examples:**

```python
>>> sort_left([3, 1, 2])
[1, 2, 3]
```

```python
>>> sort_left([5, 4, 3])
[3, 4, 5]
```



---

## sort_right_partition

### Description
Recursively sort greater-than partition

### Conceptual Info

Recursively sort the elements greater than the chosen pivot using quicksort.

### Docstring

**Summary:** Recursively applies quicksort to the list of elements greater than the chosen pivot and returns the sorted list.

**Parameters:**

- greater_than_partition (List[int]): The list of elements greater than the pivot that need to be sorted.
**Returns:** List[int] - A sorted list of the elements that were greater than the pivot.

**Raises:**

- ValueError: If 'greater_than_partition' is not a list or contains non-integer elements.
**Examples:**

```python
>>> sorted_list = sort_right([3, 1, 4])
[1, 3, 4]
```

```python
>>> sorted_list = sort_right([])
[]
```



---

## combine_sorted_partitions

### Description
Concatenate sorted left + equal + sorted right

### Conceptual Info

The combine_sorted_partitions node merges the three sublists—sorted left, equal elements, and sorted right—into one fully sorted list, forming the core step that assembles the final quicksort result.

### Docstring

**Summary:** Concatenates the sorted left partition, the equal-to-pivot partition, and the sorted right partition to produce a single sorted list.

**Parameters:**

- sorted_left (List[int]): A list of integers that has been recursively sorted and contains all elements less than the pivot.
- equal_elements (List[int]): A list of integers that are equal to the pivot.
- sorted_right (List[int]): A list of integers that has been recursively sorted and contains all elements greater than the pivot.
**Returns:** List[int] - A list containing all elements from sorted_left, equal_elements, and sorted_right in that order.

**Raises:**

- TypeError: If any input is not a list of integers.
**Examples:**

```python
>>> combine_partitions([1, 2], [3], [4, 5])
[1, 2, 3, 4, 5]
```

```python
>>> combine_partitions([1, 2, 2], [2, 2], [3, 4])
[1, 2, 2, 2, 2, 3, 4]
```



---

## quicksort

### Description
Main quicksort function that executes full sorting workflow

### Conceptual Info

The quicksort node implements the full quicksort sorting algorithm. It orchestrates the workflow defined by the preceding nodes: it first checks for the base case (empty array), then selects the first element as a pivot, partitions the remaining elements into less‑than, equal, and greater‑than groups, recursively sorts the less and greater partitions, and finally concatenates the sorted left partition, the pivot group, and the sorted right partition into the final sorted list.

### Docstring

**Summary:** Recursively sorts a list of integers using the quicksort algorithm.

**Parameters:**

- array (List[int]): The list of integers to be sorted.
**Returns:** List[int] - A new list containing the elements of `array` sorted in non‑decreasing order.

**Raises:**

- TypeError: If `array` is not a list.
- ValueError: If any element of `array` is not an integer.
**Examples:**

```python
>>> quicksort([3, 1, 4, 1, 5, 9, 2, 6])
[1, 1, 2, 3, 4, 5, 6, 9]
```

```python
>>> quicksort([])
[]
```

