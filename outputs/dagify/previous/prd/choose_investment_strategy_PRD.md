# choose_investment_strategy PRD

## Description
Chooses a high-level investment strategy


## Conceptual Info

Chooses a high-level investment strategy based on the objectives of the fund.

## Docstring

### Summary
Selects a primary hedge-fund strategy category that best serves the objectives.

### Parameters

- **fund_objectives** (dict): Output from 'clarify_fund_objectives' node containing primary business objectives.

### Returns

dict: A dictionary containing the 'chosen_investment_strategy' and 'justification' values.

### Examples

```python
>>> fund_objectives = {'investment_purpose': 'Capital appreciation', 'target_return_profile': 'Above market', 'competitive_advantage': 'Active management', 'long_term_vision': 'Long-term growth'}"
                "chosen_investment_strategy, justification = choose_investment_strategy(fund_objectives)
{'chosen_investment_strategy': 'Activemanagement', 'justification': 'To capture above-market returns through active management'}
```
