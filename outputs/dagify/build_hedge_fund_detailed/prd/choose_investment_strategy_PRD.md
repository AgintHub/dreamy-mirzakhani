# choose_investment_strategy PRD

## Description
Select hedge fund strategy aligned with objectives


## Conceptual Info

This node translates the fund’s high‑level objectives into a concrete investment strategy choice, ensuring alignment between stated goals and the selected hedge fund approach.

## Docstring

### Summary
Chooses a primary hedge fund strategy category that best aligns with the fund's objectives and returns a concise rationale.

### Parameters

- **objectives** (List[str]): Bullet list of the fund’s primary business objectives (investment purpose, competitive edge, long‑term vision).
- **investment_purpose** (str): Explicit description of the investment purpose extracted from the objectives.
- **competitive_edge** (str): Competitive advantage statement derived from the objectives.
- **long_term_vision** (str): Long‑term vision statement derived from the objectives.

### Returns

Dict[str, str]: Dictionary containing the selected strategy category and a one‑sentence rationale.

### Raises

- ValueError: Raised if any of the input objective components are missing or empty.
- RuntimeError: Raised if no single strategy can be determined to satisfy all objectives.

### Examples

```python
>>> choose_investment_strategy(

...     objectives=["Generate alpha with low correlation to markets", "Maintain flexibility to trade multiple asset classes"],

...     investment_purpose="Create diversified alpha sources for institutional clients", 

...     competitive_edge="Access to proprietary data analytics", 

...     long_term_vision="Become a leading multi‑strategy fund in the next decade"

>>> )
{
  "strategy_category": "Multi‑Strategy (Long/Short Equity + Macro) ",
  "strategy_rationale": "Combines equity alpha generation with macro exposure to meet diversification and flexibility goals."
}
```

```python
>>> choose_investment_strategy(

...     objectives=["Achieve 15% annual gross return", "Limit volatility to 20%"],

...     investment_purpose="Deliver high risk‑adjusted returns to high‑net‑worth investors", 

...     competitive_edge="In‑house algorithmic models", 

...     long_term_vision="Establish a scalable, technology‑driven hedge fund"

>>> )
{
  "strategy_category": "Quantitative (Statistical Arbitrage) ",
  "strategy_rationale": "Algorithmic models enable consistent high returns while controlling volatility."
}
```
