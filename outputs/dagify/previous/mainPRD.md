# write_three_chapter_dog_story_with_surprise - Complete PRD Documentation

## Overview
PRDs for nodes in the 'write_three_chapter_dog_story_with_surprise' module.

## Table of Contents

- [add_grand_finale](#add_grand_finale)

- [generate_character_profiles](#generate_character_profiles)

- [generate_story_outline](#generate_story_outline)

- [generate_story_setting](#generate_story_setting)

- [write_chapter_1](#write_chapter_1)

- [write_chapter_2](#write_chapter_2)

- [write_chapter_3](#write_chapter_3)



---

## add_grand_finale

### Description
Elevates Chapter 3’s conclusion by introducing an intricate, M. Night Shyamalan-style grand finale—a masterfully constructed, emotionally resonant, and intellectually gripping twist that reframes the narrative arc in a surprising, yet thematically cohesive, new light, while incorporating a subtle visual motif to enhance thematic resonance and character psychology.

### Conceptual Info

This node crafts a surprise twist at the end of Chapter 3, enriching the narrative and deepening character connections.

### Docstring

**Summary:** Adds a grand finale twist to Chapter 3, maintaining narrative coherence while surprising the reader.

**Returns:** str - The revised final chapter with the grand finale twist and emotional resonance fully integrated.

**Examples:**

```python
>>> create_grand_finale_twist('write_chapter_3')
The grand finale twist is crafted, enriching the narrative and deepening character connections.
```

```python
>>> create_grand_finale_twist('write_chapter_3')
The emotional resonance of the twist enhances character psychology and thematic symbolism.
```



---

## generate_character_profiles

### Description
Generates richly detailed character biographies that capture identity, motivation, and narrative function. Each profile includes a name, age (when relevant), personality traits, plot role, and a favorite color that informs visual or thematic cues. The dog’s profile is expanded into a list of descriptive strings detailing breed, backstory, habits, and core motivations. The output is structured to support seamless integration with subsequent plot development and visual design stages.

### Conceptual Info

This node generates richly detailed character biographies for each person and the dog in the story.

### Docstring

**Summary:** Generate detailed character profiles.

**Parameters:**

- character_profiles (List[dict]): List of dictionaries containing character information for each person and the dog.
**Returns:** dict - A dictionary containing the generated character profiles where each key is a character name and each value is a dictionary with their profile information.

**Raises:**

- TypeError: If the input character_profiles is not a list of dictionaries.


---

## generate_story_outline

### Description
Creates a succinct, three-chapter outline for a dog-centric narrative, providing a title, chapter titles, event bullet points, and a favorite color for the dog’s character profile.

### Conceptual Info

This node generates a concise, three-chapter outline for a dog-centric narrative, including a title, chapter titles, event bullet points, and a favorite color for the dog’s character profile.

### Docstring

**Summary:** Generates a three-chapter outline for a dog story.

**Parameters:**

- prompt (str): A prompt for the story outline.
**Returns:** dict - A dictionary with story outline details.

**Raises:**

- Exception: If the prompt is invalid.
**Examples:**

```python
>>> generate_story_outline(prompt='A heartwarming dog story')
>>> output = {'title': 'The Adventures of Buddy', 'chapter_titles': ['Chapter 1: Introduction', 'Chapter 2: The Journey', 'Chapter 3: The Return'], 'chapter_1_bullet_points': ['Buddy meets a new friend', 'Buddy goes on an adventure', 'Buddy returns home'], 'chapter_2_bullet_points': ['Buddy faces a challenge', 'Buddy finds a treasure', 'Buddy makes a new friend'], 'chapter_3_bullet_points': ['Buddy concludes his journey', 'Buddy says goodbye to friends', 'Buddy returns home happy'], 'favorite_color': 'Blue'}
{'title': 'The Adventures of Buddy', 'chapter_titles': ['Chapter 1: Introduction', 'Chapter 2: The Journey', 'Chapter 3: The Return'], 'chapter_1_bullet_points': ['Buddy meets a new friend', 'Buddy goes on an adventure', 'Buddy returns home'], 'chapter_2_bullet_points': ['Buddy faces a challenge', 'Buddy finds a treasure', 'Buddy makes a new friend'], 'chapter_3_bullet_points': ['Buddy concludes his journey', 'Buddy says goodbye to friends', 'Buddy returns home happy'], 'favorite_color': 'Blue'}
```

```python
>>> generate_story_outline(prompt='A dog story with a mystery')
>>> output = {'title': 'The Mystery of the Missing Treats', 'chapter_titles': ['Chapter 1: The Mysterious Scene', 'Chapter 2: The Investigation', 'Chapter 3: The Suspect Revealed'], 'chapter_1_bullet_points': ['A treat goes missing', 'The scene is established', 'Clues are revealed'], 'chapter_2_bullet_points': ['The investigation begins', 'More clues are found', 'The plot thickens'], 'chapter_3_bullet_points': ['The suspect is revealed', 'The mystery is solved', 'The dog returns home'], 'favorite_color': 'Red'}
{'title': 'The Mystery of the Missing Treats', 'chapter_titles': ['Chapter 1: The Mysterious Scene', 'Chapter 2: The Investigation', 'Chapter 3: The Suspect Revealed'], 'chapter_1_bullet_points': ['A treat goes missing', 'The scene is established', 'Clues are revealed'], 'chapter_2_bullet_points': ['The investigation begins', 'More clues are found', 'The plot thickens'], 'chapter_3_bullet_points': ['The suspect is revealed', 'The mystery is solved', 'The dog returns home'], 'favorite_color': 'Red'}
```



---

## generate_story_setting

### Description
Creates a rich, immersive setting that anchors the narrative. It specifies the geographic locale, temporal context, environmental conditions, and introduces a favorite color that reflects character traits or thematic undercurrents. This comprehensive backdrop informs mood, plot direction, and visual storytelling.

### Conceptual Info

This node creates a rich, immersive setting for the story by specifying the geographic locale, temporal context, environmental conditions, and introducing a favorite color that reflects character traits or thematic undercurrents.

### Docstring

**Summary:** Generate a story setting based on the input parameters.

**Parameters:**

- location (str): The geographic place where the story unfolds.
- time_period (str): The historical or temporal setting of the narrative.
- environmental_details (str): Key environmental factors—weather, terrain, societal norms—that influence the dog’s adventure.
- favorite_color (str): A color favored by the protagonist, offering insight into personality or thematic symbolism.
**Returns:** [str, str, str, str] - A list of strings representing the location, time period, environmental details, and favorite color.

**Raises:**

- TypeError: If any of the input parameters are not of the correct type.
**Examples:**

```python
>>> location = 'New York City'
>>> time_period = '1980s'
>>> environmental_details = 'cold weather, urban terrain, hipster society'
>>> favorite_color = 'blue'
['New York City', '1980s', 'cold weather, urban terrain, hipster society', 'blue']
```



---

## write_chapter_1

### Description
Crafts the opening chapter of the story by weaving together the concise outline, richly detailed character profiles (including each character’s favorite color), and the environmental context. The chapter must vividly introduce the canine protagonist, establish the setting, and present the inciting incident that propels the narrative forward.

### Conceptual Info

The write_chapter_1 node crafts the opening chapter of a story by integrating the provided story outline, character profiles with their favorite colors, and environmental details.

### Docstring

**Summary:** Crafts the opening chapter of a story by weaving together the provided story outline, character profiles with their favorite colors, and environmental context.

**Parameters:**

- story_outline (dict): The concise story outline for the narrative.
- character_profiles (list): A list of richly detailed character biographies.
- story_setting (dict): The comprehensive story setting including the geographic locale, temporal context, environmental conditions, and a favorite color that reflects character traits or thematic undercurrents.
**Returns:** dict - {'chapter_text': 'The complete, prose-formatted text of Chapter 1', 'valid_output': True/False}

**Raises:**

- ValueError: If the input story outline, character profiles, or story setting is invalid or missing.
**Examples:**

```python
>>> story_outline = {'title': 'Story Title', 'chapter_titles': ['Chapter 1', 'Chapter 2'], 'event_bullet_points': ['Point 1', 'Point 2', 'Point 3']}
>>> character_profiles = [{'name': 'John', 'age': 30, 'personality_traits': 'friendly', 'role_in_plot': 'protagonist', 'favorite_color': 'red'}]
>>> story_setting = {'location': 'Park', 'time_period': 'Now', 'environmental_details': 'sunny', 'favorite_color': 'blue'}
>>> write_chapter_1(story_outline, character_profiles, story_setting)
{'chapter_text': 'The complete, prose-formatted text of Chapter 1', 'valid_output': True}
```



---

## write_chapter_2

### Description
Writes Chapter 2, receiving Chapter 1 output to continue the narrative.

### Conceptual Info

This node continues the narrative of the story by writing the second chapter, incorporating the previous chapter's output, the outline, character profiles, and environmental setting.

### Docstring

**Summary:** Writes Chapter 2 using the provided inputs.

**Parameters:**

- chapter_1_output (str): The text of the first chapter, used as a basis for the second chapter's writing.
- outline (dict): A structured dictionary containing the story outline, including title, chapter titles, event bullet points, and the dog's favorite color.
- character_profiles (dict): A dictionary containing the richly detailed character biographies, including each character's name, age, personality traits, plot role, and favorite color.
- story_setting (dict): A dictionary describing the rich, immersive setting of the narrative, including geographic locale, temporal context, environmental conditions, and the protagonist's favorite color.
**Returns:** str - The complete text of Chapter 2.

**Raises:**

- ValueError: If any of the input parameters are missing or invalid.
**Examples:**

```python
>>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']}, character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits': 'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}}, story_setting={'location': 'Beach', 'time_period': 'Summer', 'environmental_details': 'Sunny', 'favorite_color': 'Red'})
<text of Chapter 2>
```

```python
>>> write_chapter_2(chapter_1_output='<text>', outline={'title': 'The Story', 'chapter_titles': ['Chapter 1', 'Chapter 2', 'Chapter 3']}, character_profiles={'dog': {'name': 'Max', 'age': 2, 'personality_traits': 'Friendly', 'role_in_plot': 'Protagonist', 'favorite_color': 'Blue'}}, story_setting={'location': 'Forest', 'time_period': 'Fall', 'environmental_details': 'Rainy', 'favorite_color': 'Green'})
<text of Chapter 2>
```



---

## write_chapter_3

### Description
Writes Chapter 3, receiving Chapter 2 output to conclude the story.

### Conceptual Info

This node is responsible for crafting the final chapter of the story, incorporating the plot developments from Chapter 2 and setting the scene for a satisfying conclusion.

### Docstring

**Summary:** Generates the final chapter of the story, using the provided outline, character profiles, and setting to conclude the dog's adventure.

**Parameters:**

- chapter_2_output (str): The complete text of Chapter 2.
**Returns:** dict[str, str] - Contains the title, content, and summary of the final chapter.

**Raises:**

- TypeError: If chapter_2_output is not a string.
**Examples:**

```python
>>> final_chapter = write_chapter_3(chapter_2_output)
>>> print(final_chapter['chapter_title'])
>>> print(final_chapter['chapter_content'])
>>> print(final_chapter['chapter_summary'])
Chapter Title: The Final Chapter
Chapter Content: The final chapter of the story.
Chapter Summary: The dog's adventure concludes with ​​.
```

