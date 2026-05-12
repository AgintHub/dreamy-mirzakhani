# write_chapter_2 PRD

## Description
Writes Chapter 2, receiving Chapter 1 output to continue the narrative.


## Conceptual Info

This node continues the narrative of the story by writing the second chapter, incorporating the previous chapter's output, the outline, character profiles, and environmental setting.

## Docstring

### Summary
Writes Chapter 2 using the provided inputs.

### Parameters

- **chapter_1_output** (str): The text of the first chapter, used as a basis for the second chapter's writing.
- **outline** (dict): A structured dictionary containing the story outline, including title, chapter titles, event bullet points, and the dog's favorite color.
- **character_profiles** (dict): A dictionary containing the richly detailed character biographies, including each character's name, age, personality traits, plot role, and favorite color.
- **story_setting** (dict): A dictionary describing the rich, immersive setting of the narrative, including geographic locale, temporal context, environmental conditions, and the protagonist's favorite color.

### Returns

str: The complete text of Chapter 2.

### Raises

- ValueError: If any of the input parameters are missing or invalid.

### Examples

```python
>>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']}, character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits': 'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}}, story_setting={'location': 'Beach', 'time_period': 'Summer', 'environmental_details': 'Sunny', 'favorite_color': 'Red'})
<text of Chapter 2>
```

```python
>>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']}, character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits': 'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}}, story_setting={'location': 'Forest', 'time_period': 'Fall', 'environmental_details': 'Rainy', 'favorite_color': 'Green'})
<text of Chapter 2>
```
