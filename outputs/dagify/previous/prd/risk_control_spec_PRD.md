# risk_control_spec PRD

## Description
Specify risk control parameters.


## Conceptual Info

This node defines risk control parameters based on the risk metrics calculated by the parent node.

## Docstring

### Summary
Define risk control specifications.

### Parameters

- **risk_metrics** (tuple[float, float, float]): Tuple of VaR at 95%, exposure limits per asset, and liquidity risk values.

### Returns

tuple[List[bool], List[float], List[int]]: A tuple of stop-loss rules, take-profit thresholds, and maximum position sizes.

### Examples

```python
>>> risk_metrics = calculate_risk_metrics()
>>> risk_control_specs = risk_control_spec(risk_metrics)
stop-loss rules: [True, False, True], take-profit thresholds: [1.0, 2.0, 3.0], maximum position sizes: [10, 20, 30]
```
