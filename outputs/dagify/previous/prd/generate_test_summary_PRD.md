# generate_test_summary PRD

## Description
Prepare structured test validation report


## Conceptual Info

This node's purpose is to generate a structured test validation report by analyzing aggregated test data.

## Docstring

### Summary
Prepare a human-readable test summary document including success metrics, failure analysis, and anomaly highlights using aggregated test data.

### Parameters

- **aggregated_test_data** (object): Aggregated test data obtained from the `aggregate_test_results` node.

### Returns

object: 
              A dictionary containing the following key-value pairs:
              - `success_metrics`: Human-readable format of success metrics
              - `failure_analysis`: Detailed analysis of test failures
              - `anomaly_highlights`: Notable anomalies detected in test results
            

### Examples

```python
>>> aggregated_test_data = aggregate_test_results.run(...)
>>> test_summary = generate_test_summary.run(aggregated_test_data)

                {
                  'success_metrics': 'Test pass rate: 80%, Test fail rate: 20%',
                  'failure_analysis': 'Detailed analysis of test failures',
                  'anomaly_highlights': 'Notable anomalies detected in test results'
                }
              
```
