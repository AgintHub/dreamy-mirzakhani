# test_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'test_workflow' module.

## Table of Contents

- [construct_test_workflow](#construct_test_workflow)

- [decompose_objective](#decompose_objective)

- [map_decomposed_objective](#map_decomposed_objective)

- [validate_test_workflow](#validate_test_workflow)



---

## construct_test_workflow

### Description
Construct the fundamental workflow DAG from the mapped tasks.

### Conceptual Info

This node constructs a fundamental workflow DAG from mapped tasks, aiming for maximum concurrency, asynchrony, and parallelism.

### Docstring

**Summary:** Constructs a fundamental workflow DAG from mapped tasks.

**Parameters:**

- mapped_objectives (List[object] or MappedObjective object or MappedObjectives list or MappedObjectives object): The mapped objectives from the Elemental Thoughts framework to serve as the basis for the workflow DAG.
**Returns:** dict or ConstructedWorkflow object or dict of list/dict structure - The constructed workflow DAG with its specified attributes.

**Raises:**

- ValueError: Raised if the mapped objectives are empty or invalid.
**Examples:**

```python
>>> (task_name, task_description) = construct_test_workflow(mapped_objectives=[{'objective1': 'description1'}]
{ 'workflow_name': 'new_workflow1', 'workflow_description': 'this is a workflow', 'graph_json': '{1: [2], 2: [3, 4], 3: [], 4: []}', 'dag_metrics': [1.0, 0.0, 0.0], 'acyclicity_status': False }
```



---

## decompose_objective

### Description
Decompose the parsed objective into constituent tasks.

### Conceptual Info

Decomposes the given task into constituent tasks to facilitate further operations.

### Docstring

**Summary:** Decomposes the given task into constituent tasks.

**Parameters:**

- fundamental_task (str): The fundamental task to be decomposed.
**Returns:** dict[str, str|list[str]] - A dictionary containing the decomposed task, list of component tasks and type of operation.

**Raises:**

- TypeError: If the input task is not a string.
**Examples:**

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



---

## map_decomposed_objective

### Description
Map each decomposed task to Elemental Thoughts framework.

### Conceptual Info

Maps decomposed tasks from the decomposed_objective node to the Elemental Thoughts framework.

### Docstring

**Summary:** Maps decomposed tasks to the Elemental Thoughts framework.

**Parameters:**

- task (str): The decomposed task to be mapped to the Elemental Thoughts framework.
**Returns:** tuple[List[str], List[str], List[str]] - A tuple containing the list of objectives mapped to Elemental Thoughts framework, the list of execution statuses for each decomposed task, and the list of error messages encountered during mapping process.

**Raises:**

- ValueError: If the task is not in the correct format for mapping.
**Examples:**

```python
>>> result, statuses, errors = map_decomposed_objective(task)
>>> print(result)
>>> print(statuses)
>>> print(errors)
['Mapped Object 1', 'Mapped Object 2', ...] 
['Success', 'Failure', ...] 
['Error 1', 'Error 2', ...]
```



---

## validate_test_workflow

### Description
Validate that the constructed workflow DAG adheres to acyclicity and dependency requirements.

### Conceptual Info

Validates the constructed workflow DAG's acyclicity and dependency adherence.

### Docstring

**Summary:** Verifies the constructed workflow DAG's acyclic nature and correct dependency enforcement.

**Returns:** dict - A dictionary containing the validation status.

**Raises:**

- ValueError: If the workflow DAG has cyclic dependencies.
- DependencyError: If the workflow DAG does not enforce correct dependencies.
**Examples:**

```python
>>> inputs = construct_test_workflow()
>>> validity_status = validate_test_workflow(inputs)
>>> print(validity_status)
True
```

```python
>>> inputs = construct_test_workflow(cyclic_DAG=True)
>>> validity_status = validate_test_workflow(inputs)
>>> print(validity_status)
False
```

