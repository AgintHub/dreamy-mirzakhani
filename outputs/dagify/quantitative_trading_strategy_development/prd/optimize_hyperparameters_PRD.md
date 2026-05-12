# optimize_hyperparameters PRD

## Description
Tune model hyperparameters.


## Conceptual Info

The node optimizes the hyperparameters of machine learning models using a grid search approach.

## Docstring

### Summary
Tune the hyperparameters of machine learning models using a grid search approach.

### Parameters

- **model** (object): Machine learning model to optimize the hyperparameters for.

### Returns

object: Best parameter sets found in the grid search along with the corresponding evaluation metrics.

### Raises

- Exception: If the model is not a machine learning model or if the grid search fails.

### Examples

```python
>>> optimized_model = optimize_hyperparameters(model)
optimized_model
```

```python
>>> evaluation_metrics = optimize_hyperparameters(model)
evaluation_metrics
```
