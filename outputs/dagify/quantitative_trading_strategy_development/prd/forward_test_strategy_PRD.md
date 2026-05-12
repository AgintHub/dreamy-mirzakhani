# forward_test_strategy PRD

## Description
This node validates the refined strategy on unseen data.


## Conceptual Info

This node validates the refined strategy on unseen data, leveraging the refined strategy blueprint and optimized risk controls to produce refined performance metrics and a trade log.

## Docstring

### Summary
This function validates a refined strategy on unseen data.

### Parameters

- **refined_strategy_blueprint** (str): The refined strategy blueprint to validate.
- **optimized_risk_controls** (List[str]): The optimized risk controls to apply during validation.
- **walk_forward_window** (int): The number of days for the walk-forward window.

### Returns

dict: A dictionary containing the refined paper trade simulation result, refined performance metrics, and the refined trade log output.

### Raises

- ValueError: If the refined strategy blueprint or optimized risk controls are invalid.

### Examples

```python
>>> validate_refined_strategy(refined_strategy_blueprint='refined_blueprint', optimized_risk_controls=['control1', 'control2'], walk_forward_window=365)
{'paper_trade_simulation_result': 'refined_result', 'performance_metrics': ['metric1', 'metric2'], 'trade_log': 'refined_trade_log'}
```
