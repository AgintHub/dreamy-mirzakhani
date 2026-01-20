# test_overfitting PRD

## Description
Detect excessive parameter fitting


## Conceptual Info

Evaluates the robustness of the optimized strategy to parameter perturbations by performing out‑of‑sample evaluations on randomly perturbed parameter sets, summarizing the performance distribution relative to the baseline optimized set.

## Docstring

### Summary
Detects overfitting by perturbing strategy parameters and evaluating out-of-sample performance metrics.

### Parameters

- **metric_names** (List[str]): Names of the performance metrics to compare.
- **baseline_values** (List[float]): Baseline metric values obtained from the original optimized parameter set.
- **optimized_params** (List[float]): The optimized parameter values used to generate the baseline.
- **sample_count** (int): Number of random perturbed parameter sets to generate (default 5).
- **perturbation_percentage** (float): Magnitude of ± perturbation applied to each parameter (default 0.2 for 20%).

### Returns

Dict[str, Any]: Dictionary containing performance metric statistics and overfitting detection flag.

### Raises

- ValueError: Raised if metric_names and baseline_values lists are of unequal length.
- RuntimeError: Raised if any perturbed evaluation fails.

### Examples

```python
>>> result = test_overfitting(metric_names=['cagr', 'sharpe'], baseline_values=[0.15, 1.5], optimized_params=[0.1, 0.2], sample_count=3, perturbation_percentage=0.2)
>>> print(result)
{'metric_names': ['cagr', 'sharpe'], 'baseline_values': [0.15, 1.5], 'perturbed_mean_values': [0.14, 1.48], 'perturbed_std_values': [0.01, 0.05], 'perturbed_min_values': [0.13, 1.42], 'perturbed_max_values': [0.16, 1.55], 'perturbation_percentage': 0.2, 'sample_count': 3, 'overfitting_detected': False}
```

```python
>>> result = test_overfitting(metric_names=['cagr'], baseline_values=[0.12], optimized_params=[0.05], sample_count=5, perturbation_percentage=0.2)
>>> print(result)
{'metric_names': ['cagr'], 'baseline_values': [0.12], 'perturbed_mean_values': [0.119], 'perturbed_std_values': [0.003], 'perturbed_min_values': [0.115], 'perturbed_max_values': [0.123], 'perturbation_percentage': 0.2, 'sample_count': 5, 'overfitting_detected': False}
```
