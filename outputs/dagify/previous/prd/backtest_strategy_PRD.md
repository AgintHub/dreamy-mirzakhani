# backtest_strategy PRD

## Description
Simulate strategy performance on historical data.


## Conceptual Info

This node simulates strategy performance on historical data, taking into account generated trade rules and feature matrices, and outputs daily equity curve values, trades logs, and backtest performance metrics.

## Docstring

### Summary
Simulate strategy performance on historical data.

### Parameters

- **trade_rules** (List[Dict[str, str]]): Generated trade rules from the 'generate_trade_rules' node.
- **feature_matrix** (List[List[float]]): Feature matrix generated from the 'assemble_feature_matrix' node.
- **slippage_model** (Dict[str, float]): Realistic slippage model parameters.
- **commission_model** (Dict[str, float]): Realistic commission model parameters.

### Returns

Dict[str, List[float]]: Daily equity curve values, trades logs, and backtest performance metrics.

### Raises

- ValueError: If input data formats are inconsistent.

### Examples

```python
>>> strategy_rules = [{'signal_threshold': 0.5, 'position_sizing_rule': 'fixed'}]
>>> feature_matrix = [[0.1, 0.2], [0.3, 0.4]]
>>> slippage_model = {'mean': 0.01, 'stddev': 0.001}
>>> commission_model = {'mean': 0.005, 'stddev': 0.0005}
{equity_curve: [0.1, 0.2, 0.3, 0.4], trade_log: [{'buy': 'signal', 'sell': 'threshold'}, {'buy': 'threshold', 'sell': 'rule'}], performance_metrics: [0.5, 0.6, 0.7]}
```
