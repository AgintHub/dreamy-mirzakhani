# _define_investor_profile - Complete PRD Documentation

## Overview
PRDs for nodes in the '_define_investor_profile' module.

## Table of Contents

- [extract_fund_objectives](#extract_fund_objectives)

- [analyze_target_investor_types](#analyze_target_investor_types)

- [calculate_minimum_investment](#calculate_minimum_investment)

- [determine_liquidity_expectations](#determine_liquidity_expectations)

- [assess_risk_tolerance_levels](#assess_risk_tolerance_levels)

- [define_geographic_focus](#define_geographic_focus)



---

## extract_fund_objectives

### Description
Extracts a concise fund objectives summary from a list of bullet points.

### Conceptual Info

The extract_fund_objectives shim function takes a list of bullet points describing a fund's objectives and returns a concise summary of these objectives.

### Docstring

**Summary:** Extracts a concise fund objectives summary from a list of bullet points.

**Parameters:**

- objectives_bullets (str): List of bullet points summarizing investment purpose, competitive advantages, target return profiles, and long-term vision (maximum 8 bullets).
**Returns:** str - Concise summary of fund objectives.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> extract_fund_objectives(objectives_bullets=['Invest in tech stocks', 'Target 10% annual returns', 'Long-term growth strategy'])
'This fund aims to achieve long-term growth through investments in tech stocks, targeting 10% annual returns.'
```



---

## analyze_target_investor_types

### Description
Analyzes fund objectives to determine the target investor types.

### Conceptual Info

This shim function analyzes the fund objectives to determine the target investor types.

### Docstring

**Summary:** Analyzes fund objectives to determine the target investor types.

**Parameters:**

- objectives (str): Fund objectives, including investment purpose, competitive advantages, target return profiles, and long-term vision.
**Returns:** List[str] - List of target investor types, such as family offices, pensions, etc.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> analyze_target_investor_types(objectives='long-term growth')
['family offices', 'pensions']
```

```python
>>> analyze_target_investor_types(objectives='short-term gains')
['hedge funds', 'high net worth individuals']
```



---

## calculate_minimum_investment

### Description
Calculates the minimum investment required based on the fund strategy and target investors.

### Conceptual Info

The calculate_minimum_investment shim function determines the minimum investment required for a fund based on its strategy and target investors.

### Docstring

**Summary:** Calculates the minimum investment required in USD based on the fund strategy and target investors.

**Parameters:**

- fund_strategy (str): The fund strategy, e.g., objectives, competitive advantages, target return profiles, and long-term vision.
- target_investors (str): The target investors, e.g., family offices, pensions.
**Returns:** int - The minimum investment required in USD.

**Raises:**

- ValueError: When the minimum investment is not a positive integer.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> calculate_minimum_investment(fund_strategy='conservative', target_investors='family offices')
>>> 100000
100000
```

```python
>>> calculate_minimum_investment(fund_strategy='aggressive', target_investors='pensions')
>>> 500000
500000
```



---

## determine_liquidity_expectations

### Description
Generates a textual description of the expected liquidity terms for a fund based on investor types and fund objectives.

### Conceptual Info

This shim encapsulates the logic to translate high‑level investor profiles and strategic objectives into a concise liquidity expectations statement, which is then used to inform potential investors about the fund’s redemption schedule, lock‑in periods, and cash‑flow management.

### Docstring

**Summary:** Return a description of liquidity expectations for a fund given investor types and fund objectives.

**Parameters:**

- investor_types (str): Comma‑separated list of investor categories (e.g., "family office, pension, high net worth individual")
- fund_objectives (str): Brief summary of the fund’s investment strategy and target performance (e.g., "long‑term growth in emerging markets with a focus on ESG compliance")
**Returns:** str - A sentence or two explaining the fund’s liquidity policy, such as lock‑in periods, redemption frequency, and any maturity schedules.

**Raises:**

- ValueError: If either investor_types or fund_objectives is empty or consists only of whitespace.
- TypeError: If investor_types or fund_objectives is not a string.
**Examples:**

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



---

## assess_risk_tolerance_levels

### Description
This shim assesses and determines the risk tolerance levels of investors based on the provided fund strategy and target demographics.

### Conceptual Info

This shim plays a crucial role in determining the risk tolerance levels of investors, which is essential for defining an investor's profile and making informed investment decisions.

### Docstring

**Summary:** Assesses the risk tolerance levels of investors based on the provided fund strategy and target demographics.

**Parameters:**

- fund_strategy (str): The strategy of the fund, which influences the risk tolerance levels.
- target_demographics (str): The target demographics of the investors, which affects their risk tolerance levels.
**Returns:** List[str] - A list of risk tolerance levels (e.g., aggressive, conservative) determined by the shim.

**Raises:**

- ValueError: If the input parameters are invalid or cannot be processed.
- TypeError: If the input parameters are of the wrong type.
**Examples:**

```python
>>> risk_levels = assess_risk_tolerance_levels(fund_strategy='aggressive_growth', target_demographics='young_adults')
>>> print(risk_levels)
['aggressive', 'moderate']
```

```python
>>> risk_levels = assess_risk_tolerance_levels(fund_strategy='conservative_income', target_demographics='retirees')
>>> print(risk_levels)
['conservative', 'cautious']
```



---

## define_geographic_focus

### Description
Generates a concise description of the geographic focus of a fund based on its objectives and target investor base.

### Conceptual Info

In the investment strategy pipeline, this shim encapsulates the logic that maps high‑level fund objectives and investor demographics to a concise geographic focus description. It acts as a bridge between objective‑level data and downstream profile generation.

### Docstring

**Summary:** Return a geographic focus description for a fund.

**Parameters:**

- objectives (str): A textual summary of the fund’s investment strategy, target returns, and long‑term vision.
- investor_base (str): A comma‑separated list of investor types (e.g., "family office, pension fund, high net worth individual").
**Returns:** str - A concise human‑readable sentence or short paragraph that specifies the geographic focus (e.g., "The fund targets emerging markets in Southeast Asia and Eastern Europe.").

**Raises:**

- ValueError: Raised when either `objectives` or `investor_base` is empty or only whitespace.
- TypeError: Raised when `objectives` or `investor_base` is not of type `str`.
**Examples:**

```python
>>> define_geographic_focus(objectives="Invest in high‑growth tech startups with a focus on sustainability", investor_base="family office, pension fund")
"The fund focuses on high‑growth tech startups in North America and Western Europe, prioritizing sustainable investment themes."
```

```python
>>> define_geographic_focus(objectives="Expand renewable energy projects across emerging markets", investor_base="high net worth individual, sovereign wealth fund")
"The fund targets renewable energy projects in emerging markets across Latin America and Africa."
```

