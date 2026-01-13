# _define_investor_profile - Complete PRD Documentation

## Overview
PRDs for nodes in the '_define_investor_profile' module.

## Table of Contents

- [parse_fund_objectives](#parse_fund_objectives)

- [determine_investor_types](#determine_investor_types)

- [calculate_minimum_investment](#calculate_minimum_investment)

- [define_liquidity_expectations](#define_liquidity_expectations)

- [assess_risk_tolerance_levels](#assess_risk_tolerance_levels)

- [determine_geographic_focus](#determine_geographic_focus)



---

## parse_fund_objectives

### Description
Parses a list of objective bullets into a structured dictionary for downstream analysis.

### Conceptual Info

This shim converts unstructured textual bullet points about a fund's objectives into a machine‑readable dictionary that downstream nodes can consume for investor profiling, risk assessment, and market analysis.

### Docstring

**Summary:** Parses a list of objective bullets and returns a structured JSON string.

**Parameters:**

- objectives_bullets (str): A JSON array string of up to 8 bullet points describing the fund's investment purpose, strategy, target returns, and long‑term vision.
**Returns:** str - A JSON string representing a dictionary with keys: 'purpose', 'strategy', 'target_return', and 'vision'. Each value is a concise text extracted from the input bullets.

**Raises:**

- ValueError: Raised if the input JSON string does not decode to a list of strings or if any bullet is empty.
- TypeError: Raised if the input is not a string.
**Examples:**

```python
>>> parse_fund_objectives('["Deliver alpha through ESG investing", "Focus on renewable energy", "Target 8% IRR over 5 years"]')
"{\n  \"purpose\": \"Deliver alpha through ESG investing\",\n  \"strategy\": \"Focus on renewable energy\",\n  \"target_return\": \"Target 8% IRR over 5 years\",\n  \"vision\": \"\"\n}"
```

```python
>>> parse_fund_objectives('["Global macro strategy", "Liquidity horizon: 2 years", "Risk tolerance: moderate"]')
"{\n  \"purpose\": \"Global macro strategy\",\n  \"strategy\": \"Liquidity horizon: 2 years\",\n  \"target_return\": \"Risk tolerance: moderate\",\n  \"vision\": \"\"\n}"
```



---

## determine_investor_types

### Description
Determine the typical investor types based on the fund strategy and market analysis.

### Conceptual Info

The determine_investor_types shim function identifies potential investor types based on the provided fund strategy and market analysis.

### Docstring

**Summary:** Determine the typical investor types based on the fund strategy and market analysis.

**Parameters:**

- fund_strategy (str): The fund strategy to consider when determining investor types.
- market_analysis (str): The market analysis to consider when determining investor types.
**Returns:** List[str] - A list of typical investor types.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> determine_investor_types(fund_strategy='conservative', market_analysis='True')
['family offices', 'pensions']
```

```python
>>> determine_investor_types(fund_strategy='aggressive', market_analysis='False')
['hedge funds', 'venture capital']
```



---

## calculate_minimum_investment

### Description
Calculates the minimum investment required based on the strategy type and investor base.

### Conceptual Info

The calculate_minimum_investment shim function determines the minimum investment required for a specific investment strategy and investor base.

### Docstring

**Summary:** Calculates the minimum investment required based on the strategy type and investor base.

**Parameters:**

- strategy_type (str): The type of investment strategy.
- investor_base (str): The type of investor.
**Returns:** int - The minimum investment required in USD.

**Raises:**

- ValueError: When the calculated minimum investment is not a positive integer.
- TypeError: When the input strategy type or investor base is not a string.
**Examples:**

```python
>>> calculate_minimum_investment(strategy_type='conservative', investor_base='individual')
>>> 100000
100000
```

```python
>>> calculate_minimum_investment(strategy_type='aggressive', investor_base='institutional')
>>> 500000
500000
```



---

## define_liquidity_expectations

### Description
Defines liquidity expectations based on investor types and fund strategy.

### Conceptual Info

This shim function generates a description of liquidity expectations based on the types of investors and the fund's strategy.

### Docstring

**Summary:** Defines liquidity expectations based on investor types and fund strategy.

**Parameters:**

- investor_types (str): A string representing the types of investors (e.g., family offices, pensions).
- fund_strategy (str): A string representing the fund's strategy (e.g., growth, income, balanced).
**Returns:** str - A description of the liquidity expectations.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> define_liquidity_expectations(investor_types='family offices', fund_strategy='growth')
>>> define_liquidity_expectations(investor_types='pensions', fund_strategy='income')
'Liquidity expectations for growth strategy with family offices', 'Liquidity expectations for income strategy with pensions'
```



---

## assess_risk_tolerance_levels

### Description
Evaluates a fund’s objectives and its target investors to produce a list of suitable risk tolerance levels.

### Conceptual Info

This shim translates high‑level fund objectives and investor profiles into concrete risk tolerance categories that the fund can offer. It serves as a bridge between strategic intent and practical investment product design.

### Docstring

**Summary:** Generate risk tolerance levels for a fund based on its objectives and target investor types.

**Parameters:**

- fund_objectives (dict): Dictionary containing parsed fund objectives, typically including strategy type, target return, time horizon, and geographical focus.
- target_investors (list): List of strings representing the types of investors the fund intends to attract (e.g., ['family_office', 'pension_fund']).
**Returns:** list[str] - A list of risk tolerance levels appropriate for the given fund objectives and investor base.

**Raises:**

- ValueError: Raised if `fund_objectives` is empty or missing required keys.
- TypeError: Raised if `fund_objectives` is not a dict or `target_investors` is not a list.
**Examples:**

```python
>>> fund_obj = {"strategy_type": "growth", "target_return": 0.12, "time_horizon": 5, "geo_focus": "global"}
>>> investors = ["family_office", "institutional"]
>>> levels = assess_risk_tolerance_levels(fund_objectives=fund_obj, target_investors=investors)
>>> print(levels)
["Aggressive", "Moderate"]
```

```python
>>> fund_obj = {"strategy_type": "income", "target_return": 0.04, "time_horizon": 10, "geo_focus": "US"}
>>> investors = ["retirement_fund"]
>>> levels = assess_risk_tolerance_levels(fund_objectives=fund_obj, target_investors=investors)
>>> print(levels)
["Conservative"]
```



---

## determine_geographic_focus

### Description
Derives a geographic focus description for a fund based on investor demographics and regulatory requirements.

### Conceptual Info

This shim encapsulates the logic that interprets investor demographic data and applicable regulatory constraints to generate a concise geographic focus for a new investment fund, enabling downstream components to align strategy and compliance.

### Docstring

**Summary:** Determine the geographic focus of a fund from investor demographics and regulatory requirements.

**Parameters:**

- investor_demographics (str): JSON‑encoded string representing the target investor base, e.g., `{"types": ["family office", "pension fund"], "regions": ["North America", "Europe"]}`.
- regulatory_requirements (str): JSON‑encoded string of applicable regulatory constraints, e.g., `{"EU": true, "US": false}`.
**Returns:** str - A plain‑text sentence stating the fund's geographic focus, such as "The fund will primarily invest in North America and Europe, complying with EU investment regulations."

**Raises:**

- ValueError: Raised when either input string is empty or fails to provide required keys.
- TypeError: Raised when the input types are not strings.
**Examples:**

```python
>>> investor_demographics = "{\"types\": [\"family office\", \"pension fund\"], \"regions\": [\"North America\", \"Europe\"]}"
>>> regulatory_requirements = "{\"EU\": true, \"US\": false}"
>>> result = determine_geographic_focus(investor_demographics, regulatory_requirements)
>>> print(result)
"The fund will primarily invest in North America and Europe, complying with EU investment regulations."
```

```python
>>> investor_demographics = "{\"types\": [\"family office\"], \"regions\": [\"Asia\"]}"
>>> regulatory_requirements = "{\"EU\": false, \"US\": false}"
>>> print(determine_geographic_focus(investor_demographics, regulatory_requirements))
"The fund will primarily invest in Asia with no specific regulatory constraints."
```

