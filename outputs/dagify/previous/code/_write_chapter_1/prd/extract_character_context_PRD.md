# extract_character_context PRD

## Description
Provides the character profile information from the given character profile input, extracted in a structured format.


## Conceptual Info

This shim extracts character profile information from the given input, providing a structured output for further processing.

## Docstring

### Summary
Extract character context from the given character profile input string.

### Parameters

- **character_profile** (str): The input character profile string, expected to be in the format of a JSON object.

### Returns

STR: A JSON object containing the character profile information, with specific fields such as character name, age, personality traits, role in the story, favorite color, and dog profile.

### Raises

- ValueError: When the input character profile string is invalid or cannot be parsed.
- TypeError: When the input character profile string is not in the expected format.

### Examples

```python
>>> import json

>>> character_profile = '{{"name": "John Doe", "age": 30, "personality_traits": ["introvert", "creative"], "role": "protagonist", "favorite_color": "blue", "dog_profile": "labrador retriever"}}'

>>> output = extract_character_context(character_profile)
{
  "character_name": "John Doe",
  "age": 30,
  "personality_traits": ["introvert", "creative"],
  "role_in_plot": "protagonist",
  "favorite_color": "blue",
  "dog_profile": "labrador retriever"
}
```

```python
>>> import json

>>> character_profile = '{{"name": "Jane Smith", "age": 25, "personality_traits": ["outgoing", "ambitious"], "role": "supporting character", "favorite_color": "red", "dog_profile": "poodle"}}'

>>> output = extract_character_context(character_profile)
{
  "character_name": "Jane Smith",
  "age": 25,
  "personality_traits": ["outgoing", "ambitious"],
  "role_in_plot": "supporting character",
  "favorite_color": "red",
  "dog_profile": "poodle"
}
```
