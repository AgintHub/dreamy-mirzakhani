# base_case_check PRD

## Description
Check if array is empty and return it directly if true


## Conceptual Info

Determines whether a list of integers is empty and propagates the list unchanged, providing a boolean flag for downstream logic.

## Docstring

### Summary
Return the input list unchanged while indicating if it is empty.

### Parameters

- **array** (List[int]): List of integers to be checked.

### Returns

Tuple[bool, List[int]]: A tuple containing a boolean flag `is_empty` and the original input list `output_array`.

### Raises

- TypeError: If the input is not a list or contains non-integer elements.

### Examples

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
