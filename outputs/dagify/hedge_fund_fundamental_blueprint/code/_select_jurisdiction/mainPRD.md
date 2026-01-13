# _select_jurisdiction - Complete PRD Documentation

## Overview
PRDs for nodes in the '_select_jurisdiction' module.

## Table of Contents

- [validate_objectives_input](#validate_objectives_input)

- [parse_fund_objectives](#parse_fund_objectives)

- [get_candidate_jurisdictions](#get_candidate_jurisdictions)

- [analyze_jurisdictions](#analyze_jurisdictions)

- [select_optimal_jurisdiction](#select_optimal_jurisdiction)

- [extract_jurisdiction_advantages](#extract_jurisdiction_advantages)

- [extract_jurisdiction_disadvantages](#extract_jurisdiction_disadvantages)

- [generate_jurisdiction_justification](#generate_jurisdiction_justification)



---

## validate_objectives_input

### Description
Validates the input objectives to ensure they are properly formatted and contain required information for subsequent processing.

### Conceptual Info

This shim function acts as a gatekeeper, ensuring that the objectives input is correctly structured and contains all necessary details before proceeding with further analysis or processing.

### Docstring

**Summary:** Validate the input objectives string to check for proper formatting and required content, returning a validated string or an error message.

**Parameters:**

- objectives (str): The input objectives string to be validated, expected to contain specific details about investment purposes, competitive advantages, target return profiles, and long-term vision.
**Returns:** str - A string indicating the validation result, which could be a success message, a list of errors, or a reformatted version of the input objectives.

**Raises:**

- ValueError: Raised when the input objectives string is empty, malformed, or missing critical information.
- TypeError: Raised when the input objectives is not a string.
**Examples:**

```python
>>> validate_objectives_input(objectives='Investment purpose: maximize returns; Competitive advantage: experienced team; Target return: 10%; Long-term vision: sustainable growth')
'Objectives input is valid.'
```

```python
>>> validate_objectives_input(objectives='Invalid input: missing details')
'Error: Objectives input is invalid. Please provide complete details.'
```



---

## parse_fund_objectives

### Description
This shim node takes a string of investment objectives and returns a dictionary with parsed objectives.

### Conceptual Info

The parse_fund_objectives shim is responsible for extracting and organizing investment objectives from a string input, playing a crucial role in subsequent fund analysis and jurisdiction selection.

### Docstring

**Summary:** Parse a string of investment objectives into a dictionary for further analysis.

**Parameters:**

- objectives (str): A string containing investment objectives, which may include investment purpose, competitive advantages, target return profiles, and long-term vision.
**Returns:** str - A JSON string representing a dictionary with keys such as 'tax_efficiency', 'regulatory_simplicity', 'investor_appeal', etc., and their corresponding values based on the input string.

**Raises:**

- ValueError: If the input string is empty, None, or cannot be parsed into a meaningful dictionary of objectives.
- TypeError: If the input is not a string.
**Examples:**

```python
>>> objectives_str = 'Invest for growth, prioritize tax efficiency, and appeal to institutional investors.'
>>> parsed_objectives = parse_fund_objectives(objectives_str)
{'growth': True, 'tax_efficiency': True, 'institutional_investors': True}
```

```python
>>> objectives_str = 'Focus on sustainable investing, aim for competitive returns, and ensure regulatory simplicity.'
>>> parsed_objectives = parse_fund_objectives(objectives_str)
{'sustainable_investing': True, 'competitive_returns': True, 'regulatory_simplicity': True}
```



---

## get_candidate_jurisdictions

### Description
Returns a list of candidate jurisdictions for fund domicile based on unclear criteria.

### Conceptual Info

The get_candidate_jurisdictions shim function provides a list of potential jurisdictions for fund domicile. The exact criteria for selection are not specified and will be determined in the future.

### Docstring

**Summary:** Returns a list of candidate jurisdictions for fund domicile.

**Returns:** List[str] - List of candidate jurisdictions

**Raises:**

- ValueError: When the list of candidate jurisdictions cannot be generated.
- TypeError: When the output type is incorrect.
**Examples:**

```python
>>> get_candidate_jurisdictions()
['Cayman Islands', 'Luxembourg', 'Singapore']
```

```python
>>> get_candidate_jurisdictions()
['Ireland', 'Switzerland', 'Hong Kong']
```



---

## analyze_jurisdictions

### Description
Analyze a list of candidate jurisdictions against tax, regulatory, and investor criteria to produce a structured assessment dictionary.

### Conceptual Info

This shim serves as the core decision‑support engine that evaluates each candidate jurisdiction on multiple dimensions—tax efficiency, regulatory simplicity, and investor appeal—and returns a comprehensive, machine‑readable analysis for downstream selection logic.

### Docstring

**Summary:** Evaluates candidate jurisdictions against specified criteria and returns a detailed analysis as a JSON string.

**Parameters:**

- candidates (List[str]): A list of jurisdiction names (e.g., ['Cayman Islands', 'Bermuda']) to be evaluated.
- tax_requirements (str): A short description of the desired tax efficiency (e.g., 'low withholding tax', 'zero corporate tax').
- regulatory_preferences (str): A short description of preferred regulatory characteristics (e.g., 'fast registration', 'minimal reporting').
- investor_targets (str): A short description of the target investor profile (e.g., 'high net worth individuals', 'institutional investors').
**Returns:** str - A JSON‑formatted string containing a dictionary. Each key is a jurisdiction name; each value is a dictionary with keys such as 'tax_score', 'regulatory_score', 'investor_score', 'advantages', 'disadvantages', and 'summary'.

**Raises:**

- ValueError: Raised when the candidates list is empty or any required criterion string is missing or empty.
- TypeError: Raised when any argument is not of the expected type.
**Examples:**

```python
>>> result = analyze_jurisdictions(

...     candidates=['Cayman Islands', 'Bermuda'],

...     tax_requirements='zero corporate tax',

...     regulatory_preferences='fast registration',

...     investor_targets='high net worth individuals'

>>> )
"{\n  \"Cayman Islands\": {\n    \"tax_score\": 9,\n    \"regulatory_score\": 8,\n    \"investor_score\": 7,\n    \"advantages\": [\"Low tax\", \"Robust financial sector\"],\n    \"disadvantages\": [\"Limited banking options\", \"High setup costs\"],\n    \"summary\": \"Suitable for private equity funds targeting high net worth investors.\"\n  },\n  \"Bermuda\": {\n    \"tax_score\": 8,\n    \"regulatory_score\": 7,\n    \"investor_score\": 8,\n    \"advantages\": [\"No capital gains tax\", \"Strong legal framework\"],\n    \"disadvantages\": [\"Regulatory scrutiny\", \"Higher operational costs\"],\n    \"summary\": \"Good for funds focused on institutional investors.\"\n  }\n}"
```

```python
>>> try:
...     analyze_jurisdictions([], 'zero tax', 'fast', 'individuals')
>>> except ValueError as e:
...     print(e)
"candidates list cannot be empty"
```



---

## select_optimal_jurisdiction

### Description
Selects the optimal jurisdiction for a fund based on analysis and objectives.

### Conceptual Info

This shim function determines the most suitable jurisdiction for a fund based on given analysis and objectives.

### Docstring

**Summary:** Selects the optimal jurisdiction for a fund based on analysis and objectives.

**Parameters:**

- analysis (str): A dictionary containing jurisdiction analysis results
- objectives (str): A dictionary containing fund objectives
**Returns:** str - The name of the optimal jurisdiction

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> select_optimal_jurisdiction(analysis={'tax_efficiency': 'high', 'regulatory_simplicity': 'medium'}, objectives={'tax_efficiency': 'high', 'investor_appeal': 'high'})
'Optimal Jurisdiction Name'
```



---

## extract_jurisdiction_advantages

### Description
Returns a list of two key advantages for a specified jurisdiction based on analysis data.

### Conceptual Info

The shim extracts the top advantages of a jurisdiction from a pre‑computed analysis dictionary to inform fund domicile selection.

### Docstring

**Summary:** Extracts the two most relevant advantages of the specified jurisdiction from the provided analysis data.

**Parameters:**

- jurisdiction (str): Name of the jurisdiction whose advantages are to be extracted.
- analysis (dict): Dictionary containing detailed analysis information keyed by jurisdiction names.
**Returns:** List[str] - A list containing two strings, each describing a key advantage of the jurisdiction.

**Raises:**

- KeyError: Raised when the jurisdiction key is missing from the analysis dictionary.
- ValueError: Raised when the extracted advantages list does not contain exactly two items.
- TypeError: Raised if inputs are not of the expected types.
**Examples:**

```python
>>> analysis_data = {
...     'Cayman Islands': {
...         'advantages': ['No direct taxes', 'Strong confidentiality laws'],
...         'disadvantages': ['Limited local market', 'High regulatory scrutiny']
...     }
>>> }
>>> extract_jurisdiction_advantages('Cayman Islands', analysis_data)
['No direct taxes', 'Strong confidentiality laws']
```

```python
>>> analysis_data = {
...     'Delaware': {
...         'advantages': ['Favorable corporate law', 'Established legal framework'],
...         'disadvantages': ['Higher filing fees', 'Limited privacy']
...     }
>>> }
>>> extract_jurisdiction_advantages('Delaware', analysis_data)
['Favorable corporate law', 'Established legal framework']
```



---

## extract_jurisdiction_disadvantages

### Description
This shim function extracts and returns a list of disadvantages for a given jurisdiction based on the provided analysis.

### Conceptual Info

The extract_jurisdiction_disadvantages shim is designed to take a jurisdiction and its analysis as input and return a list of disadvantages associated with that jurisdiction, playing a crucial role in evaluating and selecting the most appropriate jurisdiction for a fund.

### Docstring

**Summary:** Extracts a list of disadvantages for a given jurisdiction based on the provided analysis, which is essential for making informed decisions about fund domicile selection.

**Parameters:**

- jurisdiction (str): The name of the jurisdiction for which to extract disadvantages.
- analysis (str): The analysis of the jurisdiction, containing information used to identify disadvantages.
**Returns:** List[str] - A list of strings, where each string describes a disadvantage of the specified jurisdiction.

**Raises:**

- ValueError: If the input jurisdiction or analysis is invalid or cannot be processed.
- TypeError: If the jurisdiction or analysis is not of the expected type (str).
**Examples:**

```python
>>> disadvantages = extract_jurisdiction_disadvantages('Luxembourg', 'regulatory_challenges')
>>> print(disadvantages)
['High regulatory costs', 'Complex compliance procedures']
```

```python
>>> disadvantages = extract_jurisdiction_disadvantages('United States', 'tax_burdens')
>>> print(disadvantages)
['Double taxation issues', 'High corporate tax rates']
```



---

## generate_jurisdiction_justification

### Description
Generates a justification text explaining the selection of a jurisdiction based on the fund's objectives, advantages, and disadvantages.

### Conceptual Info

The generate_jurisdiction_justification shim function generates a justification text that explains why a particular jurisdiction was selected for a fund based on its objectives, advantages, and disadvantages.

### Docstring

**Summary:** Generates a justification text explaining the selection of a jurisdiction based on the fund's objectives, advantages, and disadvantages.

**Parameters:**

- jurisdiction (str): The selected jurisdiction.
- objectives (str): The fund's objectives.
- advantages (str): The advantages of the selected jurisdiction.
- disadvantages (str): The disadvantages of the selected jurisdiction.
**Returns:** str - The generated justification text.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> generate_jurisdiction_justification(jurisdiction='Singapore', objectives='long-term growth', advantages='stable government', disadvantages='high taxes')
"The jurisdiction of Singapore was selected due to its stable government, which aligns with the fund's long-term growth objectives. While Singapore has high taxes, its stable government provides a favorable business environment."
```

```python
>>> generate_jurisdiction_justification(jurisdiction='Cayman Islands', objectives='tax efficiency', advantages='low taxes', disadvantages='limited investor protection')
"The jurisdiction of the Cayman Islands was selected due to its low taxes, which aligns with the fund's tax efficiency objectives. However, the Cayman Islands have limited investor protection, which may be a consideration for investors."
```

