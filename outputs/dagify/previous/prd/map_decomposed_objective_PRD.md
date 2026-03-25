# map_decomposed_objective PRD

## Description
Map each decomposed task to Elemental Thoughts framework.


## Conceptual Info

Maps decomposed tasks from the decomposed_objective node to the Elemental Thoughts framework.

## Docstring

### Summary
Maps decomposed tasks to the Elemental Thoughts framework.

### Parameters

- **task** (str): The decomposed task to be mapped to the Elemental Thoughts framework.

### Returns

tuple[List[str], List[str], List[str]]: A tuple containing the list of objectives mapped to Elemental Thoughts framework, the list of execution statuses for each decomposed task, and the list of error messages encountered during mapping process.

### Raises

- ValueError: If the task is not in the correct format for mapping.

### Examples

```python
>>> result, statuses, errors = map_decomposed_objective(task)
>>> print(result)
>>> print(statuses)
>>> print(errors)
['Mapped Object 1', 'Mapped Object 2', ...] 
['Success', 'Failure', ...] 
['Error 1', 'Error 2', ...]
```
