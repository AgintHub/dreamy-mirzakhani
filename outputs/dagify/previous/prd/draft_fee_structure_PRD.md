# draft_fee_structure PRD

## Description
Define compensation model


## Conceptual Info

Creates a concise fee proposal that balances investor appeal with incentive alignment, integrating performance targets set by the risk‑management node.

## Docstring

### Summary
Generate a structured fee schedule for a hedge fund based on performance and risk targets.

### Parameters

- **gross_return** (float): Target annual gross return (e.g., 0.15 for 15%) obtained from set_performance_and_risk_targets.
- **volatility** (float): Target annual volatility percentage from set_performance_and_risk_targets.
- **sharpe_ratio** (float): Target annual Sharpe ratio from set_performance_and_risk_targets.
- **max_drawdown** (float): Target maximum annual drawdown percentage from set_performance_and_risk_targets.

### Returns

dict: A dictionary containing management_fee_percentage, performance_fee_percentage, hurdle_rate_percentage, and summary_sentences.

### Raises

- ValueError: If any input target is None or not a number.
- AssertionError: If performance_fee_percentage would exceed 50% or be negative.

### Examples

```python
>>> fee_structure = draft_fee_structure(gross_return=0.15, volatility=0.25, sharpe_ratio=1.5, max_drawdown=0.30)
{'management_fee_percentage': 0.025, 'performance_fee_percentage': 0.20, 'hurdle_rate_percentage': 0.08, 'summary_sentences': ['The fund charges a 2.5% annual management fee.', 'Performance fees of 20% apply to gains above an 8% hurdle.', 'This structure aligns manager incentives with investor returns.']}
```

```python
>>> fee_structure = draft_fee_structure(gross_return=0.10, volatility=0.20, sharpe_ratio=1.2, max_drawdown=0.25)
{'management_fee_percentage': 0.02, 'performance_fee_percentage': 0.15, 'hurdle_rate_percentage': 0.05, 'summary_sentences': ['The fund charges a 2% annual management fee.', 'Performance fees of 15% are charged on gains exceeding a 5% hurdle.', 'This fee schedule balances competitive pricing with strong incentive alignment.']}
```
