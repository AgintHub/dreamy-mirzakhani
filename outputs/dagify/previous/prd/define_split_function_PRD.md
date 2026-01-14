# define_split_function PRD

## Description
Define a function to split a list into two halves.


## Conceptual Info

Splits a list into two halves.

## Docstring

### Summary
Splits a list into two halves.

### Parameters

- **input_list** (List[Int]): The list to be split.

### Returns

Tuple[List[Int], List[Int]]: A tuple containing the two halves of the input list.

### Raises

- ValueError: If the input list is None or empty.

### Examples

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
