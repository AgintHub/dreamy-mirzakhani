# validate_test_workflow PRD

## Description
Validate that the constructed workflow DAG adheres to acyclicity and dependency requirements.


## Conceptual Info

Validates the constructed workflow DAG's acyclicity and dependency adherence.

## Docstring

### Summary
Verifies the constructed workflow DAG's acyclic nature and correct dependency enforcement.

### Returns

dict: A dictionary containing the validation status.

### Raises

- ValueError: If the workflow DAG has cyclic dependencies.
- DependencyError: If the workflow DAG does not enforce correct dependencies.

### Examples

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
