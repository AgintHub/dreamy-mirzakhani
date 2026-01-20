# analyze_regression_test_results PRD

## Description
Identify regression risks by analyzing results from regression testing and surface actionable anomalies.


## Conceptual Info

Parses regression test run outputs to extract concrete regression anomalies, encapsulating the feature-level impact and a succinct summary for triage and defect reporting.

## Docstring

### Summary
Analyze regression test results to extract structured regression anomalies with feature name, before/after state, impact, and a summary.

### Parameters

- **baseline_vs_actual_results** (List[str]): List of baseline vs actual results per regression scenario, derived from run_regression_tests.
- **state_drift_indicators** (List[str]): List of textual indicators signaling state drift or anomalies detected during regression tests.
- **performance_metrics** (List[str]): List of performance-related metrics captured during regression testing.

### Returns

List[Dict[str, Union[str, int]]]: A list of regression anomaly records, each with feature_name, before_after_state_comparison, impact_severity_estimation, and regression_summary.

### Raises

- TypeError: Raised if any input is not a list of strings or is None.
- ValueError: Raised if inputs are empty or no anomalies can be inferred.

### Examples

```python
>>> analyze_regression_test_results(
...   baseline_vs_actual_results=["FeatureA: 100ms -> 250ms"],
...   state_drift_indicators=["FeatureA drift detected"],
...   performance_metrics=["avg_latency_increase: 150ms"]
>>> )
[{'feature_name': 'FeatureA', 'before_after_state_comparison': 'baseline 100ms; current 250ms', 'impact_severity_estimation': 8, 'regression_summary': 'Significant latency regression observed for FeatureA.'}]
```

```python
>>> analyze_regression_test_results(
...   baseline_vs_actual_results=["FeatureB: 200ms -> 290ms"],
...   state_drift_indicators=["FeatureB drift"],
...   performance_metrics=["throughput decline"]
>>> )
[{'feature_name': 'FeatureB', 'before_after_state_comparison': 'before 200ms; after 290ms', 'impact_severity_estimation': 9, 'regression_summary': 'Critical latency regression detected for FeatureB.'}]
```
