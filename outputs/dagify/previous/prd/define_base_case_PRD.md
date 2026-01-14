# define_base_case PRD

## Description
Define the base case for the recursive merge sort function.


## Conceptual Info

The base case for the recursive merge sort function defines whether a list is already sorted and has a length of 1 or less.

## Docstring

### Summary
Determines if a list is a base case for the recursive merge sort function.

### Parameters

- **input_list** (List[str]): The input list to be sorted.

### Returns

bool: Whether the input list is a base case (i.e., length 1 or less).

### Examples

```python
>>> define_base_case([1])
>>> define_base_case([])
True
True
```
