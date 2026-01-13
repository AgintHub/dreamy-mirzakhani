# parse_objectives_requirements PRD

## Description
Parses a given prompt into a structured dictionary of objectives and requirements.


## Conceptual Info

This shim function takes a prompt as input, extracts relevant information about objectives and requirements, and returns a structured dictionary.

## Docstring

### Summary
Parses a given prompt into a structured dictionary of objectives and requirements.

### Parameters

- **prompt** (str): The input prompt to be parsed, containing information about objectives and requirements.

### Returns

dict: A dictionary representing the parsed objectives and requirements.

### Raises

- ValueError: When the input prompt is invalid or cannot be parsed.
- TypeError: When the input prompt is not a string.

### Examples

```python
>>> parse_objectives_requirements(prompt='The fund aims to achieve a 10% annual return through investments in sustainable energy projects.')
>>> print(output)
{'objectives': ['achieve 10% annual return'], 'requirements': ['invest in sustainable energy projects']}
```

```python
>>> parse_objectives_requirements(prompt='The company seeks to develop a new product line with a competitive advantage in the tech industry.')
>>> print(output)
{'objectives': ['develop new product line'], 'requirements': ['achieve competitive advantage in tech industry']}
```
