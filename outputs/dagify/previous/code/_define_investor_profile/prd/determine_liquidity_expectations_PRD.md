# determine_liquidity_expectations PRD

## Description
Generates a textual description of the expected liquidity terms for a fund based on investor types and fund objectives.


## Conceptual Info

This shim encapsulates the logic to translate high‑level investor profiles and strategic objectives into a concise liquidity expectations statement, which is then used to inform potential investors about the fund’s redemption schedule, lock‑in periods, and cash‑flow management.

## Docstring

### Summary
Return a description of liquidity expectations for a fund given investor types and fund objectives.

### Parameters

- **investor_types** (str): Comma‑separated list of investor categories (e.g., "family office, pension, high net worth individual")
- **fund_objectives** (str): Brief summary of the fund’s investment strategy and target performance (e.g., "long‑term growth in emerging markets with a focus on ESG compliance")

### Returns

str: A sentence or two explaining the fund’s liquidity policy, such as lock‑in periods, redemption frequency, and any maturity schedules.

### Raises

- ValueError: If either investor_types or fund_objectives is empty or consists only of whitespace.
- TypeError: If investor_types or fund_objectives is not a string.

### Examples

```python
>>> determine_liquidity_expectations(
...     investor_types='family office, pension',
...     fund_objectives='mid‑term growth in technology sectors',
>>> )
"Liquidity terms: 12‑month lock‑in period with quarterly redemption windows, allowing investors to access capital after the initial year while maintaining portfolio stability."
```

```python
>>> determine_liquidity_expectations(
...     investor_types='high net worth individual',
...     fund_objectives='high‑risk, high‑return venture capital strategy',
>>> )
"Liquidity terms: 24‑month lock‑in period with semi‑annual liquidity events to balance high growth potential with capital preservation."
```
