# _generate_character_profiles - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_character_profiles' module.

## Table of Contents

- [extract_character_profiles_from_input](#extract_character_profiles_from_input)

- [validate_character_profiles_input](#validate_character_profiles_input)

- [identify_main_character](#identify_main_character)

- [extract_character_name](#extract_character_name)

- [determine_character_age](#determine_character_age)

- [generate_personality_traits](#generate_personality_traits)

- [determine_plot_role](#determine_plot_role)

- [assign_favorite_color](#assign_favorite_color)

- [extract_dog_information](#extract_dog_information)

- [generate_dog_profile_sentences](#generate_dog_profile_sentences)



---

## extract_character_profiles_from_input

### Description
Extracts and validates character profiles from the input data.

### Conceptual Info

The shim node is responsible for extracting character profiles from a given input data, ensuring the extracted data conforms to a specific structure and format.

### Docstring

**Summary:** Extracts character profiles from the input data, validating the extracted data against a prescribed schema.

**Parameters:**

- input_data (STR): Input data containing character profile information.
- kwargs (STR): Additional keyword arguments used to configure the extraction process.
**Returns:** List[dict] - A list of dictionaries containing validated character profile data. Each dictionary represents a character with its associated attributes and values.

**Raises:**

- ValueError: Raised when the input data fails to meet the prescribed structure and format requirements.
- TypeError: Raised when the input data contains unexpected or malformed types.
**Examples:**

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



---

## validate_character_profiles_input

### Description
This shim function validates the structure and integrity of character profile data extracted from input text.

### Conceptual Info

This shim function checks the correctness, completeness, and consistency of character profile data before further processing in the story generation pipeline.

### Docstring

**Summary:** Validate the structure and content of character profile data extracted from input, raising errors if validation fails.

**Parameters:**

- character_profiles (str): A JSON string representing a list of character profile dictionaries extracted from user input.
**Returns:** str - A success message if validation passes, or raises an error if validation fails.

**Raises:**

- ValueError: Raised when validation detects missing required fields or inconsistent data in character profiles.
- TypeError: Raised when character_profiles is not a correctly formatted JSON string or contains data of unexpected types.
**Examples:**

```python
>>> validate_character_profiles_input(character_profiles='[{"name": "Alice", "age": 30}]')
'Validation successful: character profiles are valid.'
```

```python
>>> validate_character_profiles_input(character_profiles='[{"name": 123, "age": "unknown"}]')
ValueError: Invalid data types in character profiles.
```



---

## identify_main_character

### Description
Identifies the main character from a list of character profiles.

### Conceptual Info

This shim node identifies the main character from a list of character profiles based on their attributes.

### Docstring

**Summary:** Identifies the main character from a list of character profiles.

**Parameters:**

- character_profiles (Dict[str, str]): A dictionary of character profiles where each key is a character name and each value is a JSON string containing character attributes
**Returns:** Dict - A dictionary representing the main character's profile with attributes as keys and corresponding values

**Raises:**

- ValueError: If input validation fails, e.g., invalid JSON in the character profiles dict
- TypeError: If input types are incorrect, e.g., non-string keys in the character profiles dict
**Examples:**

```python
>>> char_profiles = {'Harry Potter': '{"age": 17, "hobby": "Quidditch"}', 'Ron Weasley': '{"age": 17, "hobby": "Pranks"}'}",
"identify_main_character(character_profiles=char_profiles)"
{"name": "Harry Potter", "age": 17, "hobby": "Quidditch"}
```

```python
>>> char_profiles = {'Dumbledore': '{"age": 115, "hobby": "Potions"}', 'Hermione Granger': '{"age": 17, "hobby": "Reading"}'}",
"identify_main_character(character_profiles=char_profiles)"
{"name": "Dumbledore", "age": 115, "hobby": "Potions"}
```



---

## extract_character_name

### Description
Extracts the character's full name from the main character's data.

### Conceptual Info

This shim function plays a critical role in the character profile generation process by extracting the main character's name from their associated data.

### Docstring

**Summary:** Extracts the character's full name from the main character's data.

**Parameters:**

- character_data (str): The input character data containing the character's name.
**Returns:** str - The extracted character name as a string, formatted and processed for further use in character profile generation.

**Raises:**

- ValueError: When input validation fails, e.g., character name not found.
- TypeError: When input types are incorrect, e.g., non-string input.
**Examples:**

```python
>>> main_character = {'name': 'John Doe', 'age': 30, 'traits': ['introverted']}
>>> character_name = extract_character_name(character_data=main_character)
>>> print(character_name)
'John Doe'
```

```python
>>> main_character = {'name': 'Jane Smith', 'age': 25, 'traits': ['outgoing']}
>>> character_name = extract_character_name(character_data=main_character)
>>> print(character_name)
'Jane Smith'
```



---

## determine_character_age

### Description
Determine the age of a character given their data.

### Conceptual Info

This shim functions calculates the age of a character based on provided data, ensuring accuracy and consistency.

### Docstring

**Summary:** Determine the age of a character given their data.

**Parameters:**

- character_data (dict): A dictionary containing the character's data, including birthdate, for accurate age calculation.
**Returns:** float - The calculated age of the character

**Raises:**

- ValueError: When invalid or missing data is provided, or when date calculations fail.
- TypeError: When the input data is of an incorrect type, causing calculation errors.
**Examples:**

```python
>>> character_data = {'birthdate': '1990-01-01'}
>>> character_age = determine_character_age(character_data)
30
```

```python
>>> character_data = {'birthdate': '1980-01-01'}
>>> character_age = determine_character_age(character_data)
42
```



---

## generate_personality_traits

### Description
Generates a concise list of defining personality traits for a given character.

### Conceptual Info

This shim node generates personality traits for a character based on the provided input.

### Docstring

**Summary:** Generates a concise list of personality traits for a given character based on the input character data.

**Parameters:**

- character_data (str): Input parameter of type str containing the character's information, such as their name, age, and background.
**Returns:** str - A concise list of defining personality traits for the character, formatted as a string.

**Raises:**

- ValueError: Raised when the input character data is invalid or cannot be processed.
- TypeError: Raised when the input type is incorrect.
**Examples:**

```python
>>> character_data = {'name': 'John Doe', 'age': 30, 'background': 'Engineer'}
>>> print(generate_personality_traits(character_data))
>>> # Output: "A reserved and analytical individual who values efficiency and precision."
A reserved and analytical individual who values efficiency and precision.
```

```python
>>> character_data = {'name': 'Jane Doe', 'age': 25, 'background': 'Artist'}
>>> print(generate_personality_traits(character_data))
>>> # Output: "A free-spirited and creative individual who values self-expression and originality."
A free-spirited and creative individual who values self-expression and originality.
```



---

## determine_plot_role

### Description
This shim node determines the character's functional role within the story.

### Conceptual Info

This shim node is used to determine the character's role in the story based on their characteristics.

### Docstring

**Summary:** Determine the character's role in the plot based on their characteristics.

**Parameters:**

- character_data (str): The character's name, age, personality traits, etc., formatted as a string.
**Returns:** str - The character's functional role within the story, represented as a string.

**Raises:**

- ValueError: When the input string is invalid or missing required information.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> function(input) -> expected output
>>> determine_plot_role('John, 30, brave, loyal') -> 'protagonist'
>>> determine_plot_role('Jane, 25, sweet, naive') -> 'sidekick'
'protagonist'
```

```python
>>> function(input) -> expected output
>>> determine_plot_role('Bob, 40, mean, stubborn') -> 'antagonist'
'antagonist'
```



---

## assign_favorite_color

### Description
Assigns a favorite color to a character based on their personality traits.

### Conceptual Info

The shim assign_favorite_color calculates a character's favorite color based on their personality traits.

### Docstring

**Summary:** Calculates a character's favorite color based on their personality traits.

**Parameters:**

- character_data (str): A string representing the character's details.
**Returns:** STR - A color that encapsulates the character's essence or aesthetic.

**Raises:**

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> favorite_color = assign_favorite_color(character_data={'name': 'John', 'personality': 'calm'})
'blue'
```

```python
>>> favorite_color = assign_favorite_color(character_data={'name': 'Jane', 'personality': 'adventurous'})
'purple'
```



---

## extract_dog_information

### Description
Extracts key information about a dog from the character profiles.

### Conceptual Info

This shim node is responsible for extracting key information about a dog from the given character profiles. It takes in a string of character profiles and returns a JSON object containing the extracted dog information.

### Docstring

**Summary:** Extracts key information about a dog from the given character profiles.

**Parameters:**

- character_profiles (str): The character profiles input as a string.
**Returns:** dict - A JSON object containing key information about the dog, such as its breed, background, quirks, and motivations.

**Raises:**

- ValueError: When the input string is malformed or empty.
- TypeError: When the input parameter is not a string.
**Examples:**

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



---

## generate_dog_profile_sentences

### Description
Generate a list of sentences describing a dog's breed, background, quirks, and motivations.

### Conceptual Info

This shim function is responsible for generating a list of sentences describing a dog's characteristics based on the provided input data.

### Docstring

**Summary:** Generate a list of sentences describing a dog's breed, background, quirks, and motivations.

**Parameters:**

- dog_data (str): Input parameter containing dog information to be used for generating profile sentences.
**Returns:** List[str] - A list of sentences detailing the dog's characteristics.

**Raises:**

- TypeError: When the input data is not a string.
- ValueError: When the input data is empty or invalid.
**Examples:**

```python
>>> dog_data = 'Breed: Labrador, Age: 3, Personality: Friendly'
[Breed: Labrador, Age: 3, Personality: Friendly]
```

```python
>>> dog_data = 'Breed: Golden Retriever, Age: 5, Personality: Loyal'
[Breed: Golden Retriever, Age: 5, Personality: Loyal]
```

