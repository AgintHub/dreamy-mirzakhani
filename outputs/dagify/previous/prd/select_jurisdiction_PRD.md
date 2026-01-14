# select_jurisdiction PRD

## Description
Determine optimal fund registration location


## Conceptual Info

Selects the most suitable domicile for the hedge fund based on its business objectives, providing concise justification and a balanced view of benefits and drawbacks.

## Docstring

### Summary
Chooses a fund domicile and returns a rationale, pros, and cons based on investment objectives.

### Parameters

- **investment_objectives** (List[str]): A list of up to eight bullet points outlining the hedge fund's primary business objectives, covering investment purpose, risk/reward expectations, and target market differentiation.

### Returns

Dict[str, Any]: A dictionary containing the chosen jurisdiction name, a one‑sentence rationale, two pros, and two cons.

### Raises

- ValueError: If `investment_objectives` is empty or None.

### Examples

```python
>>> investment_objectives = [
...     "Generate high risk‑adjusted returns via long/short equity",
...     "Maintain volatility below 12%",
...     "Target institutional investors in North America"
>>> ]
>>> result = select_jurisdiction(investment_objectives)
{
  "jurisdiction_name": "Cayman Islands",
  "rationale": "The Cayman Islands provide a flexible regulatory environment and tax neutrality that align with the fund's high‑return, low‑volatility strategy.",
  "pros": ["Tax‑free jurisdiction", "Well‑established legal framework for funds"],
  "cons": ["Limited investor protection compared to EU jurisdictions", "Higher compliance costs for certain regulatory filings"]
}
```

```python
>>> investment_objectives = [
...     "Focus on global macro opportunities",
...     "Cap volatility at 15%",
...     "Target both institutional and accredited retail investors"
>>> ]
>>> result = select_jurisdiction(investment_objectives)
{
  "jurisdiction_name": "Delaware, USA",
  "rationale": "Delaware offers a mature legal system and favorable corporate law for global macro funds seeking a U.S. presence.",
  "pros": ["Strong legal precedent", "Ease of accessing U.S. capital markets"],
  "cons": ["U.S. corporate tax implications", "Mandatory SEC reporting requirements"]
}
```
