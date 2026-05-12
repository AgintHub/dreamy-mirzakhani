# _write_chapter_1 - Complete PRD Documentation

## Overview
PRDs for nodes in the '_write_chapter_1' module.

## Table of Contents

- [validate_inputs](#validate_inputs)

- [create_chapter_structure](#create_chapter_structure)

- [extract_character_context](#extract_character_context)

- [extract_setting_context](#extract_setting_context)

- [integrate_color_themes](#integrate_color_themes)

- [craft_opening_scene](#craft_opening_scene)

- [develop_chapter_events](#develop_chapter_events)

- [weave_chapter_prose](#weave_chapter_prose)

- [validate_chapter_output](#validate_chapter_output)



---

## validate_inputs

### Description
This shim node validates the inputs from the generate_story_outline, generate_character_profiles, and generate_story_setting nodes before they are used in the write_chapter_1 function.

### Conceptual Info

This shim node acts as a pre-processing step in the write_chapter_1 function, ensuring that the inputs from other nodes meet the required criteria before further processing.

### Docstring

**Summary:** Validates the inputs from the generate_story_outline, generate_character_profiles, and generate_story_setting nodes before passing them to the write_chapter_1 function.

**Parameters:**

- story_outline (str): Input parameter representing the story outline from the generate_story_outline node.
- character_profiles (str): Input parameter representing the character profiles from the generate_character_profiles node.
- story_setting (str): Input parameter representing the story setting from the generate_story_setting node.
**Returns:** str - A string indicating whether the inputs are valid or not. If valid, outputs 'Inputs are valid.'; otherwise, outputs an error message.

**Raises:**

- ValueError: When any of the input parameters are empty.
- TypeError: When the type of any of the input parameters does not match the expected type (i.e., string).
**Examples:**

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



---

## create_chapter_structure

### Description
Creates a structured dictionary for a chapter based on provided bullet points and story title.

### Conceptual Info

This shim creates a structured chapter structure based on user-provided bullet points and story title.

### Docstring

**Summary:** Creates a dictionary representing a chapter based on bullet points and story title.

**Parameters:**

- chapter_bullet_points (str): String containing bullet points for the chapter.
- story_title (str): String containing the story title.
**Returns:** dict - A dictionary representing the chapter content with keys for bullet points and story title.

**Raises:**

- ValueError: If the input parameters are not valid.
- TypeError: If the input parameters are not strings.
**Examples:**

```python
>>> create_chapter_structure('Chapter 1 bullet points', 'Story Title')
{'bullet_points': 'Chapter 1 bullet points', 'story_title': 'Story Title'}
```

```python
>>> create_chapter_structure('Another chapter bullet points', 'Another Story Title')
{'bullet_points': 'Another chapter bullet points', 'story_title': 'Another Story Title'}
```



---

## extract_character_context

### Description
Provides the character profile information from the given character profile input, extracted in a structured format.

### Conceptual Info

This shim extracts character profile information from the given input, providing a structured output for further processing.

### Docstring

**Summary:** Extract character context from the given character profile input string.

**Parameters:**

- character_profile (str): The input character profile string, expected to be in the format of a JSON object.
**Returns:** STR - A JSON object containing the character profile information, with specific fields such as character name, age, personality traits, role in the story, favorite color, and dog profile.

**Raises:**

- ValueError: When the input character profile string is invalid or cannot be parsed.
- TypeError: When the input character profile string is not in the expected format.
**Examples:**

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



---

## extract_setting_context

### Description
Extracts a setting context dictionary from a given story setting string.

### Conceptual Info

extract_setting_context is a shim node responsible for taking a story setting string and transforming it into a JSON-formatted dictionary. Its primary role is to provide a standardized way of handling story setting inputs, making it easier to integrate with other nodes in the system.

### Docstring

**Summary:** This function takes a story setting string as input and returns a dictionary containing the extracted setting context.

**Parameters:**

- story_setting (str): The story setting string from which the setting context will be extracted.
**Returns:** dict - A dictionary containing the setting context, with keys representing the different setting elements and values representing their corresponding values.

**Raises:**

- ValueError: If the input story setting string is malformed or missing required elements.
- TypeError: If the input story setting string cannot be properly converted to a dictionary.
**Examples:**

```python
>>> extract_setting_context('location: city, time_period: past, environmental_details: sunny')
>>> print(extract_setting_context('location: forest, time_period: present, environmental_details: rainy'))
{"location": "forest", "time_period": "present", "environmental_details": "rainy"}
```

```python
>>> extract_setting_context('invalid setting string')
>>> print(extract_setting_context('missing required elements'))
ValueError: Invalid story setting string
```



---

## integrate_color_themes

### Description
This shim integrates the colors of the story outline, character profiles, and story setting to generate a cohesive color theme.

### Conceptual Info

This shim integrates the colors from the story outline, character profiles, and story setting to create a harmonious and cohesive color theme.

### Docstring

**Summary:** Integrate color themes from different story components.

**Parameters:**

- outline_color (str): The color theme from the story outline.
- character_color (str): The color theme from the character profiles.
- setting_color (str): The color theme from the story setting.
**Returns:** dict - A dictionary containing the integrated color themes.

**Raises:**

- ValueError: When the input colors are invalid or inconsistent.
- TypeError: When the input colors have incorrect data types.
**Examples:**

```python
>>> integrate_color_themes(outline_color='blue', character_color='green', setting_color='yellow')
>>> print(output)
{}
```

```python
>>> integrate_color_themes(outline_color='red', character_color='orange', setting_color='red')
>>> print(output)
{"color": "red"}
```



---

## craft_opening_scene

### Description
Generates a typed opening scene based on the character context, setting context, and color themes.

### Conceptual Info

The `craft_opening_scene` shim generates an opening scene for a story by incorporating the character context, setting context, and color themes. This node serves as a crucial step in the creative process, ensuring a captivating start to the narrative.

### Docstring

**Summary:** This shim crafts an opening scene for a story based on the character context, setting context, and color themes.

**Parameters:**

- character_context (str): A string describing the character's context in the scene.
- setting_context (str): A string describing the setting's context in the scene.
- color_themes (str): A string describing the color themes used in the scene.
**Returns:** dict - A dictionary containing the crafted opening scene, character context, setting context, and color themes.

**Raises:**

- ValueError: If the input parameters are not strings or the color themes are not provided.
- TypeError: If the character context, setting context, or color themes are not strings.
**Examples:**

```python
>>> character_context = {'name': 'John Doe', 'age': 30, ' occupation': 'Programmer'}
>>> setting_context = {'location': 'New York', 'time_period': '2022'}
>>> color_themes = 'Bright and vibrant colors'
>>> output = craft_opening_scene(character_context=character_context, setting_context=setting_context, color_themes=color_themes)
{'opening_scene': 'John Doe walked down the bustling streets of New York, feeling energized by the bright and vibrant colors surrounding him. He was a programmer by day and an artist by night, and this city was his playground.'}
```

```python
>>> character_context = {'name': 'Jane Doe', 'age': 25, ' occupation': 'Artist'}
>>> setting_context = {'location': 'Paris', 'time_period': '2018'}
>>> color_themes = 'Muted and monochromatic colors'
>>> output = craft_opening_scene(character_context=character_context, setting_context=setting_context, color_themes=color_themes)
{'opening_scene': 'Jane Doe sat at a small café in Paris, surrounded by the muted and monochromatic colors of the 1950s. She was an artist, and this city was her muse.'}
```



---

## develop_chapter_events

### Description
Develops a well-structured chapter by integrating character context and setting details with given bullet points.

### Conceptual Info

This shim function plays a crucial role in shaping the narrative by developing a coherent and engaging chapter that harmoniously combines given elements.

### Docstring

**Summary:** Crafts a chapter by integrating character context and setting details with given bullet points.

**Parameters:**

- bullet_points (str): Three bullet points summarizing the chapter's content.
- character_context (str): Contextual background on the protagonist or main character in the chapter.
- setting_context (str): Description of the setting or environment where the chapter takes place.
**Returns:** str - Formatted chapter that accurately reflects the provided context.

**Raises:**

- ValueError: Raised when input validation fails, such as missing or misformatted context.
- TypeError: Raised when input types are incorrect or incompatible.
**Examples:**

```python
>>> develop_chapter_events(bullet_points='Point 1. Point 2. Point 3.', character_context='Context about main character.', setting_context='Setting details.')
A well-structured chapter with character context, setting details, and bullet points.
```

```python
>>> develop_chapter_events(bullet_points='Another point 1. Another point 2. Another point 3.', character_context='Different context about main character.', setting_context='Different setting details.')
Another well-structured chapter with different character context, setting details, and bullet points.
```



---

## weave_chapter_prose

### Description
Creates a well-formed, cohesive chapter by interweaving the opening scene, chapter body, and color themes.

### Conceptual Info

This shim node plays a crucial role in creating a coherent chapter, which is a critical component of a story. It receives inputs for the opening scene, chapter body, and color themes, and returns a formatted chapter text.

### Docstring

**Summary:** Creates a chapter by weaving together opening scene, chapter body, and color themes.

**Parameters:**

- opening_scene (str): The opening scene of the chapter, setting the tone and introducing the main elements.
- chapter_body (str): The body of the chapter, elaborating on the opening scene and advancing the plot.
- color_themes (str): The color themes that permeate the chapter, adding a visual and emotional depth.
**Returns:** str - A well-formatted chapter text, incorporating the provided inputs and meeting the requirements of a cohesive narrative.

**Raises:**

- ValueError: Raised when the input parameters are invalid or incomplete, preventing the creation of a coherent chapter.
- TypeError: Raised when the input parameters have incorrect types, hindering the formation of a well-structured chapter.
**Examples:**

```python
>>> weave_chapter_prose(opening_scene='The dark forest loomed before us.', chapter_body='As we ventured deeper, the trees seemed to close in, their branches creaking ominously.', color_themes='The red moon cast an eerie glow over the forest, while the trees seemed to absorb the faint light, making it almost invisible.')
>>> complete_chapter = chapter_text
The dark forest loomed before us. As we ventured deeper, the trees seemed to close in, their branches creaking ominously. The red moon cast an eerie glow over the forest, while the trees seemed to absorb the faint light, making it almost invisible.
```



---

## validate_chapter_output

### Description
Validates whether a generated chapter meets the expected format and content.

### Conceptual Info

This shim node validates whether a generated chapter meets the expected format and content.

### Docstring

**Summary:** Validates whether a generated chapter meets the expected format and content. Returns True if the chapter is valid and False otherwise.

**Parameters:**

- chapter_text (str): The complete text of the chapter to be validated.
**Returns:** PrimitiveType.BOOL - True if the chapter is well-formed and non-empty; otherwise False.

**Raises:**

- ValueError: When the chapter text is empty or malformed.
- TypeError: When the chapter text is not a string.
**Examples:**

```python
>>> class ChapterValidator:
...     def __init__(self):
...         pass
...     def validate_chapter_output(self, chapter_text)
...         # Validation logic goes here"
              "        return chapter_text != ''
            ],
            "output": "True"
          },
          {
            "lines": [
              "validator = ChapterValidator()",
              "print(validator.validate_chapter_output(''))
False
```

