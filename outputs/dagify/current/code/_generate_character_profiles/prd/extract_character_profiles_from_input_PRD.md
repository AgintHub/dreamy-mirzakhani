# extract_character_profiles_from_input PRD

## Description
Extracts and validates character profiles from the input data.


## Conceptual Info

The shim node is responsible for extracting character profiles from a given input data, ensuring the extracted data conforms to a specific structure and format.

## Docstring

### Summary
Extracts character profiles from the input data, validating the extracted data against a prescribed schema.

### Parameters

- **input_data** (STR): Input data containing character profile information.
- **kwargs** (STR): Additional keyword arguments used to configure the extraction process.

### Returns

List[dict]: A list of dictionaries containing validated character profile data. Each dictionary represents a character with its associated attributes and values.

### Raises

- ValueError: Raised when the input data fails to meet the prescribed structure and format requirements.
- TypeError: Raised when the input data contains unexpected or malformed types.

### Examples

```python
>>> input_data = 'Character 1: John Doe, Age: 25, Traits: Extroverted', 'Character 2: Jane Doe, Age: 30, Traits: Introverted'
>>> # Example usage
>>> character_profiles = extract_character_profiles_from_input(input_data=input_data, kwargs={'required_keys': ['Name', 'Age']})
[
  {
    'Name': 'John Doe',
    'Age': 25,
    'Traits': ['Extroverted']
  },
  {
    'Name': 'Jane Doe',
    'Age': 30,
    'Traits': ['Introverted']
  }
]
```

```python
>>> # Invalid input data
>>> input_data = 'Invalid character profile data'
>>> # Attempting to extract character profiles with malformed input data raises a ValueError
>>> try:
...     character_profiles = extract_character_profiles_from_input(input_data=input_data, kwargs={'required_keys': ['Name', 'Age']})
ValueError: Input data does not conform to the prescribed structure and format.
```
