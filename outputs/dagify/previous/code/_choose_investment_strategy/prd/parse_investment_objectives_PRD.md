# parse_investment_objectives PRD

## Description
Parses a string of investment objectives into a structured dictionary.


## Conceptual Info

The parse_investment_objectives shim function takes a string of bullet points representing investment objectives and returns a structured dictionary representing these objectives.

## Docstring

### Summary
Parses a string of investment objectives into a structured dictionary.

### Parameters

- **objectives_bullets** (str): A string of bullet points summarizing investment objectives.

### Returns

dict: A dictionary representing the parsed investment objectives.

### Raises

- ValueError: When the input string is not a valid list of bullet points.
- TypeError: When the input is not a string.

### Examples

```python
>>> parse_investment_objectives(objectives_bullets='* Objective 1\n* Objective 2')
{'objective_1': 'description', 'objective_2': 'description'}
```

```python
>>> parse_investment_objectives(objectives_bullets='')
{}
```
