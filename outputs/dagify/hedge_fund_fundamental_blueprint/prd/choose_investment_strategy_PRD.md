# choose_investment_strategy PRD

## Description
Select primary investment approach


## Conceptual Info

This node determines the flagship investment strategy for the hedge fund, ensuring alignment with the fund’s stated objectives, competitive positioning, and target return profile.

## Docstring

### Summary
Selects the primary investment strategy category and generates a rationale and risk profile based on the fund's objectives.

### Parameters

- **objectives_bullets** (List[str]): Bullet points summarizing the fund’s investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets). These are the outputs of the parent node `clarify_fund_objectives`.

### Returns

Dict[str, str]: A dictionary with keys `strategy_category`, `rationale`, and `risk_profile`, each mapping to a string describing the chosen strategy, its alignment with objectives, and the anticipated risk characteristics.

### Raises

- ValueError: Raised if `objectives_bullets` is empty or does not contain any actionable points.
- RuntimeError: Raised if no suitable strategy category can be inferred from the provided objectives.

### Examples

```python
>>> strategy = choose_investment_strategy(objectives_bullets=[
...     "Generate 15% annual gross return through diversified equity strategies.",
...     "Maintain low correlation with global macro factors.",
...     "Leverage proprietary quantitative models.",
...     "Target a volatility of 8-10%.",
...     "Seek alpha in both bull and bear markets.",
...     "Operate within a liquid asset universe.",
...     "Aim for a Sharpe ratio above 1.5.",
...     "Focus on long-term capital preservation."] )
>>> print(strategy['strategy_category'])
>>> print(strategy['rationale'])
>>> print(strategy['risk_profile'])
"Event‑Driven Equity"\n"The fund will focus on exploiting corporate event catalysts such as M&A, restructurings, and spin‑offs, leveraging its quantitative edge to generate asymmetric returns in both bullish and bearish market regimes. This aligns with the objective of producing 15% gross annual returns while maintaining low correlation to macro trends.\n"The strategy offers medium to high volatility with potential for sharp downside during illiquid event periods, but mitigated by strict position limits and liquidity buffers. Expected volatility: 8‑10% with drawdown controls at 25%."
```

```python
>>> strategy = choose_investment_strategy(objectives_bullets=[
...     "Provide long‑term growth for institutional pension funds.",
...     "Capitalize on global macro opportunities.",
...     "Maintain a conservative risk appetite."] )
>>> print(strategy['strategy_category'])
"Global Macro"
```
