# run_regression_tests PRD

## Description
This node orchestrates the execution of regression test scenarios for unchanged features, collecting baseline vs actual results, state drift indicators, and performance metrics.


## Conceptual Info

Orchestrates end-to-end regression testing for unchanged features by executing regression scenarios, capturing baseline vs actual results, detecting state drift, and collecting performance metrics for downstream analysis.

## Docstring

### Summary
Run regression test scenarios and aggregate baseline vs actual results, drift indicators, and performance metrics.

### Parameters

- **inputs** (None or object): No explicit input parameters for this node in the current DAG; the node consumes plan artifacts from design_regression_test_cases and environment setup. If provided, it would be an execution context or configuration structure in extended usage.

### Returns

Tuple[List[str], List[str], List[str]]: A tuple containing: baseline_vs_actual_results, state_drift_indicators, and performance_metrics.

### Raises

- ValueError: Raised if the regression plan is missing or malformed.
- RuntimeError: Raised if environment prerequisites are not satisfied or test execution fails catastrophically.

### Examples

```python
>>> run_regression_tests()
(['baseline_A_vs_actual_A', 'baseline_B_vs_actual_B'], ['drift_A_detected', 'drift_B_detected'], ['latency=120ms', 'throughput=350rps'])
```

```python
>>> run_regression_tests()
(['baseline_A2_vs_actual_A2'], ['no_drift'], ['latency=110ms', 'throughput=420rps'])
```
