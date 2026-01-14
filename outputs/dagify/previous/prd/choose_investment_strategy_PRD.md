# choose_investment_strategy PRD

## Description
Select primary investment approach and strategy classification


## Conceptual Info

This node selects a primary investment strategy and explains its alignment with the fund's objectives.

## Docstring

### Summary
Selects a hedge fund strategy and explains its alignment with fund objectives.

### Parameters

- **investment_objectives** (List[str]): List of fund objectives defined in the clarify_fund_objectives node

### Returns

{chosen_strategy: str, alignment_explanation: str}: A dictionary containing the chosen strategy and its alignment explanation

### Raises

- ValueError: If the chosen strategy is not one of the predefined categories

### Examples

```python
>>> investment_objectives = ['generate alpha', 'manage risk']
>>> chosen_strategy = 'long/short equity'
>>> alignment_explanation = 'The long/short equity strategy aligns with the objectives by generating alpha through stock selection and managing risk through hedging'
{'chosen_strategy': 'long/short equity', 'alignment_explanation': 'The long/short equity strategy aligns with the objectives by generating alpha through stock selection and managing risk through hedging'}
```
