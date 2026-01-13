# build_risk_rules PRD

## Description
Create portfolio-level risk controls


## Conceptual Info

This node creates a set of risk limit rules to control portfolio-level risks.

## Docstring

### Summary
Builds portfolio-level risk controls based on given risk limit rules and thresholds.

### Parameters

- **performance_benchmarks** (dict): Performance benchmarks output from 'set_performance_benchmarks' node
- **risk_limit_rules_input** (dict): Input dictionary containing risk limit rules and their thresholds

### Returns

dict: A dictionary containing the portfolio volatility limit, sector concentration limit, drawdown trigger limit, position correlation limit, and a list of risk limit rules with their thresholds

### Raises

- ValueError: If the input dictionary is empty or missing required keys
- TypeError: If the input dictionary values are not of the correct type

### Examples

```python
>>> performance_benchmarks = {'cagr_target': 0.15, 'annual_volatility_constraint': 0.20, 'drawdown_limit': 0.25, 'sharpe_ratio_goal': 1.5}
>>> risk_limit_rules_input = {'portfolio_volatility': 0.10, 'sector_concentration': 0.30, 'drawdown_trigger': 0.20, 'position_correlation': 0.50}
>>> risk_limits = build_risk_rules(performance_benchmarks, risk_limit_rules_input)
{'portfolio_volatility_limit': 0.10, 'sector_concentration_limit': 0.30, 'drawdown_trigger_limit': 0.20, 'position_correlation_limit': 0.50, 'risk_limit_rules': ['portfolio_volatility: 0.10', 'sector_concentration: 0.30', 'drawdown_trigger: 0.20', 'position_correlation: 0.50']}
```
