# _select_jurisdiction - Complete PRD Documentation

## Overview
PRDs for nodes in the '_select_jurisdiction' module.

## Table of Contents

- [validate_objectives_input](#validate_objectives_input)

- [extract_fund_requirements](#extract_fund_requirements)

- [get_jurisdiction_candidates](#get_jurisdiction_candidates)

- [score_jurisdictions](#score_jurisdictions)

- [select_optimal_jurisdiction](#select_optimal_jurisdiction)

- [extract_key_advantages](#extract_key_advantages)

- [extract_key_disadvantages](#extract_key_disadvantages)

- [generate_justification](#generate_justification)



---

## validate_objectives_input

### Description
Validates the input objectives for selecting a jurisdiction, ensuring they are properly formatted and contain the required information.

### Conceptual Info

The validate_objectives_input shim plays a crucial role in the jurisdiction selection process by verifying that the provided objectives are valid and properly structured, which is essential for the subsequent steps in the process.

### Docstring

**Summary:** Validate the input objectives to ensure they are correctly formatted and contain the necessary information for jurisdiction selection.

**Parameters:**

- objectives (str): A string representing the objectives input, which should be a list of bullet points summarizing the investment purpose, competitive advantages, target return profiles, and long-term vision.
**Returns:** str - A string indicating the validation result, which can be either a success message or an error message detailing the issues with the objectives input.

**Raises:**

- ValueError: Raised when the objectives input is invalid, such as when it is not a list of bullet points or when it contains insufficient information.
- TypeError: Raised when the objectives input is not a string.
**Examples:**

```python
>>> validate_objectives_input(objectives="['Investment purpose', 'Competitive advantages', 'Target return profiles', 'Long-term vision']")
'Objectives input is valid.'
```

```python
>>> validate_objectives_input(objectives="Invalid input")
'Error: Objectives input must be a list of bullet points.'
```



---

## extract_fund_requirements

### Description
Parses a list of investment objective bullet points and returns a JSON string summarizing the required jurisdiction attributes for fund structuring.

### Conceptual Info

The shim extracts structured fund requirements from unstructured objective bullet points, enabling downstream jurisdiction scoring and selection.

### Docstring

**Summary:** Extracts and normalizes fund requirements from a list of bullet-point objectives.

**Parameters:**

- objectives (list of str): Each element is a bullet point summarizing the fund’s investment purpose, target return profile, competitive advantages, and long‑term vision.
**Returns:** str - A JSON string representing a dictionary with keys such as `investment_type`, `target_return`, `risk_tolerance`, `target_market`, `preferred_currency`, and `legal_requirements` extracted from the input.

**Raises:**

- ValueError: If any bullet point is empty or cannot be parsed into a known requirement.
- TypeError: If the input is not a list of strings.
**Examples:**

```python
>>> input_bullets = [
...     "A global equity fund targeting 12% annual return with moderate risk",
...     "Preferable jurisdiction: low corporate tax, strong investor protection",
...     "Investment focus on emerging markets in Asia and Africa"
>>> ]
>>> print(extract_fund_requirements(objectives=input_bullets))
"{\n  \"investment_type\": \"equity\",\n  \"target_return\": 12,\n  \"risk_tolerance\": \"moderate\",\n  \"target_market\": [\"Asia\", \"Africa\"],\n  \"preferred_currency\": \"USD\",\n  \"legal_requirements\": [\"low corporate tax\", \"strong investor protection\"]\n}"
```

```python
>>> input_bullets = [
...     "A fixed‑income fund seeking 5% return with low risk",
...     "Focus on sovereign bonds in developed markets",
...     "Jurisdiction should offer flexible regulatory frameworks"
>>> ]
>>> print(extract_fund_requirements(objectives=input_bullets))
"{\n  \"investment_type\": \"fixed‑income\",\n  \"target_return\": 5,\n  \"risk_tolerance\": \"low\",\n  \"target_market\": [\"developed markets\"],\n  \"preferred_currency\": \"USD\",\n  \"legal_requirements\": [\"flexible regulatory frameworks\"]\n}"
```



---

## get_jurisdiction_candidates

### Description
Retrieves a list of potential jurisdictions, each represented as a dictionary containing jurisdiction details required for later scoring and selection.

### Conceptual Info

This shim serves as the data source for the jurisdiction selection pipeline, providing raw candidate information that is later enriched, scored, and filtered.

### Docstring

**Summary:** Return a list of jurisdiction candidate dictionaries for scoring and selection.

**Returns:** LIST_STR - A list of jurisdiction dictionaries, e.g., [{'name': 'Cayman Islands', 'tax_rate': 0, 'regulatory_flexibility': 9}, ...].

**Raises:**

- RuntimeError: If the underlying data source is unreachable or returns malformed data.
**Examples:**

```python
>>> >>> candidates = get_jurisdiction_candidates()
>>> >>> print(candidates[0]['name'])
Cayman Islands
```

```python
>>> >>> for j in get_jurisdiction_candidates()[:2]:
>>> ...     print(j['name'], j['tax_rate'])
Cayman Islands 0\nBritish Virgin Islands 0
```



---

## score_jurisdictions

### Description
Scores jurisdictions based on their suitability for a fund with given requirements.

### Conceptual Info

The score_jurisdictions shim function evaluates a list of candidate jurisdictions against a set of fund requirements and returns a scored list of jurisdictions.

### Docstring

**Summary:** Scores jurisdictions based on their suitability for a fund with given requirements.

**Parameters:**

- candidates (str): A string representing candidate jurisdictions.
- requirements (str): A string representing fund requirements.
**Returns:** List[dict] - A list of dictionaries containing scored jurisdictions.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> score_jurisdictions(candidates='{"jurisdiction1": "desc1"}, {"jurisdiction2": "desc2"}', requirements='{"req1": "desc1"}, {"req2": "desc2"}')
[{"jurisdiction": "jurisdiction1", "score": 0.8}, {"jurisdiction": "jurisdiction2", "score": 0.6}]
```



---

## select_optimal_jurisdiction

### Description
Selects the optimal jurisdiction from a list of scored options based on fund objectives and strategy.

### Conceptual Info

The select_optimal_jurisdiction shim function is responsible for selecting the most suitable jurisdiction for a fund based on its objectives and strategy. It takes a list of scored jurisdiction options as input and returns the optimal jurisdiction.

### Docstring

**Summary:** Selects the optimal jurisdiction from a list of scored options.

**Parameters:**

- scored_options (str): A list of dictionaries containing jurisdiction data and scores.
**Returns:** str - The optimal jurisdiction

**Raises:**

- ValueError: When the input list is empty.
- TypeError: When the input is not a list of dictionaries.
**Examples:**

```python
>>> select_optimal_jurisdiction(scored_options=[{'name': 'Jurisdiction A', 'score': 90}, {'name': 'Jurisdiction B', 'score': 80}])
{'name': 'Jurisdiction A', 'score': 90}
```

```python
>>> select_optimal_jurisdiction(scored_options=[{'name': 'Jurisdiction C', 'score': 70}, {'name': 'Jurisdiction D', 'score': 60}])
{'name': 'Jurisdiction C', 'score': 70}
```



---

## extract_key_advantages

### Description
Returns a list of the top N key advantages of a given jurisdiction based on its data dictionary.

### Conceptual Info

This shim analyzes jurisdiction metadata to surface the most compelling advantages that support fund strategy decisions.

### Docstring

**Summary:** Extracts a specified number of key advantages from a jurisdiction data dictionary.

**Parameters:**

- jurisdiction_data (dict): A dictionary containing jurisdiction attributes, expected to include an 'advantages' list or a free‑text 'description' field.
- count (int): The number of top advantages to return. Must be a positive integer.
**Returns:** List[str] - A list of up to `count` advantage strings sorted by relevance.

**Raises:**

- TypeError: If `jurisdiction_data` is not a dictionary or `count` is not an integer.
- ValueError: If `count` is less than 1 or exceeds the available advantage entries.
**Examples:**

```python
>>> data = {
...     'name': 'Cyprus',
...     'advantages': ['Low tax rates', 'EU membership', 'English common law', 'Fast company registration']
>>> }
>>> print(extract_key_advantages(jurisdiction_data=data, count=2))
['Low tax rates', 'EU membership']
```

```python
>>> data = {
...     'name': 'Guernsey',
...     'description': 'Guernsey offers a stable regulatory environment, tax neutrality, and access to the UK market.'
>>> }
>>> print(extract_key_advantages(jurisdiction_data=data, count=3))
['Stable regulatory environment', 'Tax neutrality', 'Access to the UK market']
```



---

## extract_key_disadvantages

### Description
Extracts key disadvantages from a given jurisdiction data.

### Conceptual Info

The extract_key_disadvantages shim function is used to extract key disadvantages from a given jurisdiction data. This function plays a crucial role in evaluating the pros and cons of a jurisdiction for a fund.

### Docstring

**Summary:** Extracts key disadvantages from a given jurisdiction data.

**Parameters:**

- jurisdiction_data (str): The jurisdiction data to extract disadvantages from.
- count (str): The number of disadvantages to extract.
**Returns:** List[str] - A list of key disadvantages of the given jurisdiction.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> extract_key_disadvantages(jurisdiction_data='{"name": "Singapore", "disadvantages": ["high taxes", "complex regulations"]}', count='2')
['high taxes', 'complex regulations']
```

```python
>>> extract_key_disadvantages(jurisdiction_data='{"name": "Cayman Islands", "disadvantages": ["limited investor protection", "reputation risks"]}', count='1')
['limited investor protection']
```



---

## generate_justification

### Description
This shim generates a justification text linking the chosen jurisdiction to the fund's objectives and strategy based on provided jurisdiction, objectives, advantages, and disadvantages.

### Conceptual Info

The generate_justification shim is used to create a textual justification for the selection of a jurisdiction based on the fund's objectives and the jurisdiction's characteristics.

### Docstring

**Summary:** Generate a justification text based on the provided jurisdiction, objectives, advantages, and disadvantages.

**Parameters:**

- jurisdiction (str): The name of the selected jurisdiction.
- objectives (str): The objectives of the fund.
- advantages (str): The advantages of the chosen jurisdiction.
- disadvantages (str): The disadvantages of the chosen jurisdiction.
**Returns:** str - The generated justification text.

**Raises:**

- ValueError: If any of the input parameters are empty or invalid.
- TypeError: If the input parameters are not of the correct type.
**Examples:**

```python
>>> justification = generate_justification('Luxembourg', 'Invest in EU stocks', 'Tax benefits, EU market access', 'High setup costs, regulatory complexity')
>>> print(justification)
'The selection of Luxembourg as the jurisdiction is justified by its tax benefits and access to the EU market, which align with the fund\'s objective to invest in EU stocks, despite the high setup costs and regulatory complexity.'
```

