# generate_performance_summary PRD

## Description
Generates a summary of performance metrics based on the provided metrics data.


## Conceptual Info

This shim node is responsible for taking in performance metrics data and producing a concise summary that can be used for reporting and analysis purposes.

## Docstring

### Summary
Generates a performance summary based on the input metrics.

### Parameters

- **metrics** (str): A string containing performance metrics data.

### Returns

str: A summary of the performance metrics in string format.

### Raises

- ValueError: If the input metrics string is malformed or empty.
- TypeError: If the input metrics is not a string.

### Examples

```python
>>> generate_performance_summary('latency: 100ms, throughput: 500req/s')
'Performance Summary: Latency = 100ms, Throughput = 500req/s'
```

```python
>>> generate_performance_summary('error_rate: 0.05, response_time: 200ms')
'Performance Summary: Error Rate = 0.05, Response Time = 200ms'
```
