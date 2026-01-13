# parse_fund_objectives PRD

## Description
This shim function takes a string of fund objectives bullet points as input and returns a dictionary representing the parsed objectives.


## Conceptual Info

The parse_fund_objectives shim is responsible for interpreting and structuring fund objectives provided as unstructured bullet points into a usable format for further analysis or processing.

## Docstring

### Summary
Parses a string of fund objectives bullet points into a structured dictionary format.

### Parameters

- **objectives_bullets** (str): A string containing fund objectives as bullet points.

### Returns

str: A JSON string representing the parsed objectives as a dictionary.

### Raises

- ValueError: If the input string is not a valid representation of bullet points or if parsing fails.
- TypeError: If the input is not a string.

### Examples

```python
>>> objectives_str = "• Investment purpose: Long-term growth\n• Competitive advantages: Diversified portfolio\n• Target return profiles: 8-12% per annum"
>>> parsed_objectives = parse_fund_objectives(objectives_bullets=objectives_str)
{'investment_purpose': 'Long-term growth', 'competitive_advantages': 'Diversified portfolio', 'target_return_profiles': '8-12% per annum'}
```

```python
>>> objectives_str = "• Long-term vision: Market leadership\n• Risk tolerance: Moderate"
>>> parsed_objectives = parse_fund_objectives(objectives_bullets=objectives_str)
{'long_term_vision': 'Market leadership', 'risk_tolerance': 'Moderate'}
```
