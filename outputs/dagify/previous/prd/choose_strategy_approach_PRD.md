# choose_strategy_approach PRD

## Description
Select trading methodology framework


## Conceptual Info

This node maps a high‑level strategy objective to a concrete methodological framework, providing justification and technical rationale that guides downstream rule and model design.

## Docstring

### Summary
Selects the trading methodology (rule‑based, machine‑learning, or hybrid) that best fits the strategy objective.

### Parameters

- **strategy_sentence** (str): One‑sentence statement of the strategy’s objective, e.g., 'Capture momentum in small‑cap stocks with <3% daily volatility'.
- **cagr_target** (float): Target Compound Annual Growth Rate expressed as a decimal (e.g., 0.15).
- **annual_vol_target** (float): Maximum acceptable annual volatility expressed as a decimal (e.g., 0.20).
- **max_drawdown** (float): Maximum drawdown limit expressed as a decimal (e.g., 0.25).
- **sharpe_goal** (float): Target Sharpe ratio to be achieved.

### Returns

dict: Dictionary containing `methodology`, `justifications`, and `technical_reasons` as described in the output structure.

### Raises

- ValueError: Raised if any required input is missing or of incorrect type.

### Examples

```python
>>> result = choose_strategy_approach(
...     strategy_sentence='Capture momentum in small-cap stocks with <3% daily volatility',
...     cagr_target=0.15,
...     annual_vol_target=0.20,
...     max_drawdown=0.25,
...     sharpe_goal=1.5)
>>> print(result['methodology'])
>>> print(result['justifications'])
>>> print(result['technical_reasons'])
```
methodology: 'rule-based'
justifications: ['Momentum signals are well captured by trend-following rules.', 'Requires minimal computational overhead for high-frequency execution.']
technical_reasons: ['Historical data is abundant and clean.', 'Model interpretability is critical for regulatory compliance.', 'Low latency execution is achievable with rule-based logic.']
```
```

```python
>>> result = choose_strategy_approach(
...     strategy_sentence='Generate alpha from mean-reversion patterns in high-volatility futures',
...     cagr_target=0.20,
...     annual_vol_target=0.35,
...     max_drawdown=0.30,
...     sharpe_goal=2.0)
>>> print(result['methodology'])
```
methodology: 'machine-learning'
```
```
