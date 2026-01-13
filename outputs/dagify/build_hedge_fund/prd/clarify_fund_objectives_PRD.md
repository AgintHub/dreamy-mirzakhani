# clarify_fund_objectives PRD

## Description
Define the core business and investment objectives for the hedge fund


## Conceptual Info

Generates a concise, bullet‑point list of the hedge fund’s core business and investment objectives, providing a clear foundation for strategy selection, legal structuring, investor targeting, and jurisdiction choice.

## Docstring

### Summary
Generate a list of up to eight bullet points that capture the hedge fund’s investment purpose, risk/reward expectations, and target market differentiation.

### Parameters

- **prompt** (str): Instruction string that specifies the maximum number of bullets and the focus areas (investment purpose, risk/reward, target market).

### Returns

List[str]: A list of bullet‑point strings, each describing a distinct business or investment objective.

### Raises

- ValueError: Raised if the input prompt is empty or does not contain a clear instruction.

### Examples

```python
>>> output = clarify_fund_objectives(prompt)
>>> print(output)
["Generate alpha through a diversified long/short equity strategy.", "Maintain portfolio volatility below 15% annualized.", "Deliver 20% gross annual returns to institutional investors.", "Differentiate by leveraging proprietary quantitative models."]
```

```python
>>> output = clarify_fund_objectives(prompt)
>>> print(len(output))
4
```
