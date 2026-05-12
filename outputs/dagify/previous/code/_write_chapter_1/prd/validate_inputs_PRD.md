# validate_inputs PRD

## Description
This shim node validates the inputs from the generate_story_outline, generate_character_profiles, and generate_story_setting nodes before they are used in the write_chapter_1 function.


## Conceptual Info

This shim node acts as a pre-processing step in the write_chapter_1 function, ensuring that the inputs from other nodes meet the required criteria before further processing.

## Docstring

### Summary
Validates the inputs from the generate_story_outline, generate_character_profiles, and generate_story_setting nodes before passing them to the write_chapter_1 function.

### Parameters

- **story_outline** (str): Input parameter representing the story outline from the generate_story_outline node.
- **character_profiles** (str): Input parameter representing the character profiles from the generate_character_profiles node.
- **story_setting** (str): Input parameter representing the story setting from the generate_story_setting node.

### Returns

str: A string indicating whether the inputs are valid or not. If valid, outputs 'Inputs are valid.'; otherwise, outputs an error message.

### Raises

- ValueError: When any of the input parameters are empty.
- TypeError: When the type of any of the input parameters does not match the expected type (i.e., string).

### Examples

```python
>>> validate_inputs('Valid story outline example', 'Valid character profiles example', 'Valid story setting example')
>>> print(validate_inputs(...))
'Inputs are valid.'
```

```python
>>> validate_inputs('', 'Invalid character profiles example', 'Valid story setting example')
>>> print(validate_inputs(...))
Error: Empty input parameter(s).
```
