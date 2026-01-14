# base_case_check PRD

## Description
Check if array is empty and return it directly if true


## Conceptual Info

This node serves as the quicksort algorithm's base case checker, immediately returning empty arrays to terminate recursion for efficiency.

## Docstring

### Summary
Check if input array is empty and return a tuple with boolean flag and array. Returns same array regardless of emptiness for non-empty cases.

### Parameters

- **array** (List[int]): Input list of integers to check for emptiness

### Returns

Tuple[bool, List[int]]: is_empty: Boolean indicating array emptiness, output_array: Same input array or empty list

### Examples

```python
>>> base_case_check([])
{'is_empty': True, 'output_array': []}
```

```python
>>> base_case_check([3, 1, 4])
{'is_empty': False, 'output_array': [3, 1, 4]}
```
