# construct_test_workflow PRD

## Description
Construct the fundamental workflow DAG from the mapped tasks.


## Conceptual Info

This node constructs a fundamental workflow DAG from mapped tasks, aiming for maximum concurrency, asynchrony, and parallelism.

## Docstring

### Summary
Constructs a fundamental workflow DAG from mapped tasks.

### Parameters

- **mapped_objectives** (List[object] or MappedObjective object or MappedObjectives list or MappedObjectives object): The mapped objectives from the Elemental Thoughts framework to serve as the basis for the workflow DAG.

### Returns

dict or ConstructedWorkflow object or dict of list/dict structure: The constructed workflow DAG with its specified attributes.

### Raises

- ValueError: Raised if the mapped objectives are empty or invalid.

### Examples

```python
>>> (task_name, task_description) = construct_test_workflow(mapped_objectives=[{'objective1': 'description1'}]
{ 'workflow_name': 'new_workflow1', 'workflow_description': 'this is a workflow', 'graph_json': '{1: [2], 2: [3, 4], 3: [], 4: []}', 'dag_metrics': [1.0, 0.0, 0.0], 'acyclicity_status': False }
```
