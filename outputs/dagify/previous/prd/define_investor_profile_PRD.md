# define_investor_profile PRD

## Description
Characterize target investor demographic


## Conceptual Info

The node captures the demographic and financial profile of the intended investor base, ensuring alignment with the fund’s strategic objectives and regulatory constraints.

## Docstring

### Summary
Generates a concise list of four key traits defining the target investor demographic.

### Parameters

- **investment_objectives** (List[str]): Bullet list of the hedge fund’s primary business objectives, as produced by the `clarify_fund_objectives` node.

### Returns

Dict[str, List[str]]: Dictionary containing the key‑characteristics list under the key `investor_profile_characteristics`.

### Raises

- ValueError: Raised if `investment_objectives` is empty or not a list of strings.

### Examples

```python
>>> investment_objectives = [
...     "Generate >12% annual gross return",
...     "Maintain volatility below 12%",
...     "Target institutional investors in North America",
...     "Offer 30‑day liquidity window"
>>> ]
>>> result = define_investor_profile(investment_objectives)
>>> print(result['investor_profile_characteristics'])
["Institutional investors", "North America", "Minimum investment $5M", "30‑day liquidity window"]
```

```python
>>> investment_objectives = ["Focus on macro opportunities", "Target high net worth retail"]
>>> result = define_investor_profile(investment_objectives)
>>> print(result['investor_profile_characteristics'])
["High net worth retail", "Global reach", "Minimum investment $500k", "Monthly liquidity"]
```
