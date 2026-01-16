# decompose_objective PRD

## Description
Decompose the parsed objective into constituent tasks.


## Conceptual Info

Decomposes the given task into constituent tasks to facilitate further operations.

## Docstring

### Summary
Decomposes the given task into constituent tasks.

### Parameters

- **fundamental_task** (str): The fundamental task to be decomposed.

### Returns

dict[str, str|list[str]]: A dictionary containing the decomposed task, list of component tasks and type of operation.

### Raises

- TypeError: If the input task is not a string.

### Examples

```python
>>> decompose_objective(fundamental_task='execute_service')
>>> print(decompose_objective(fundamental_task='execute_service'))
{'decomposed_task': 'execute_service', 'component_tasks': ['task_1', 'task_2'], 'operation_type': 'sequential'}
```

```python
>>> decompose_objective(fundamental_task='run_pipeline')
>>> print(decompose_objective(fundamental_task='run_pipeline'))
{'decomposed_task': 'run_pipeline', 'component_tasks': ['task_3', 'task_4'], 'operation_type': 'parallel'}
```
