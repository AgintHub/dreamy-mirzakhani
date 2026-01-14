# format_objectives_bullets PRD

## Description
Formats a list of raw bullet points into a polished and structured list of objectives.


## Conceptual Info

The format_objectives_bullets shim is responsible for taking a list of raw bullet points and formatting them into a structured and polished list of objectives. This is a critical step in presenting the investment objectives of a fund in a clear and concise manner.

## Docstring

### Summary
Formats a list of raw bullet points into a polished and structured list of objectives.

### Parameters

- **raw_bullets** (str): A string containing the raw bullet points to be formatted, separated by newline characters or commas.

### Returns

list[str]: A list of formatted bullet points, with each bullet point being a string.

### Raises

- ValueError: When the input string is empty or contains no valid bullet points.
- TypeError: When the input is not a string.

### Examples

```python
>>> format_objectives_bullets(raw_bullets='\n- Invest in sustainable energy\n- Focus on long-term growth')
['- Invest in sustainable energy', '- Focus on long-term growth']
```

```python
>>> format_objectives_bullets(raw_bullets='Invest in technology, Enhance customer experience')
['Invest in technology', 'Enhance customer experience']
```
