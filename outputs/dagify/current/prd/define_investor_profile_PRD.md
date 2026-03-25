# define_investor_profile PRD

## Description
Articulates the target investor segment.


## Conceptual Info

This node is responsible for defining the target investor segment, including their characteristics and preferences.

## Docstring

### Summary
Define the target investor segment for the fund.

### Parameters

- **fund_objectives** (dict): Fund objectives as defined by the `clarify_fund_objectives` node.

### Returns

dict: Defined investor profile as a dictionary with keys for investor type, ticket size, risk tolerance, liquidity preference, and geographic focus.

### Examples

```python
>>> define_investor_profile(fund_objectives={
...     'investment_purpose': 'capital appreciation',
...     'target_return_profile': 'high return',
...     'competitive_advantage': 'unique investment strategy',
...     'long_term_vision': 'long-term growth',
...     'other_objectives': 'diversification'"
                "})
{'investor_type': 'family offices', 'ticket_size': 1000000, 'risk_tolerance': 0.7, 'liquidity_preference': 'medium', 'geographic_focus': 'global'}
```
