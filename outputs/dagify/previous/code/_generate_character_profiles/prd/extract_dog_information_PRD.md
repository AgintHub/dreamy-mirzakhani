# extract_dog_information PRD

## Description
Extracts key information about a dog from the character profiles.


## Conceptual Info

This shim node is responsible for extracting key information about a dog from the given character profiles. It takes in a string of character profiles and returns a JSON object containing the extracted dog information.

## Docstring

### Summary
Extracts key information about a dog from the given character profiles.

### Parameters

- **character_profiles** (str): The character profiles input as a string.

### Returns

dict: A JSON object containing key information about the dog, such as its breed, background, quirks, and motivations.

### Raises

- ValueError: When the input string is malformed or empty.
- TypeError: When the input parameter is not a string.

### Examples

```python
>>> import json
>>> from pydantic import BaseModel
>>> def extract_dog_information(character_profiles: str) -> dict:
...     # Code to extract dog information from character profiles
...     return dog_info
>>> output = extract_dog_information('character profiles string')
>>> print(json.dumps(output, indent=4))
{
  'dog_breed': 'Golden Retriever',
  'dog_background': 'Household',
  'dog_quirks': ['Fur', 'Tail Wags'],
  'dog_motivations': ['Get treats', 'Play fetch']
}
```

```python
>>> import json
>>> from pydantic import BaseModel
>>> def extract_dog_information(character_profiles: str) -> dict:
...     # Code to extract dog information from character profiles
...     return dog_info
>>> output = extract_dog_information('')
>>> print(json.dumps(output, indent=4))
{}
```
