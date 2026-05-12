# _generate_story_outline - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_story_outline' module.

## Table of Contents

- [validate_prompt](#validate_prompt)

- [generate_story_title](#generate_story_title)

- [generate_chapter_titles](#generate_chapter_titles)

- [generate_chapter_bullet_points](#generate_chapter_bullet_points)

- [generate_dog_favorite_color](#generate_dog_favorite_color)



---

## validate_prompt

### Description
Validates the input prompt for correct formatting and content.

### Conceptual Info

The validate_prompt shim is used to validate and sanitize user input to ensure correct formatting and content.

### Docstring

**Summary:** A shim function that takes in a user-provided prompt and returns a validated version of the prompt.

**Parameters:**

- prompt (str): User-provided prompt to be validated.
**Returns:** dict - A dictionary containing the validated prompt and the final output string. The dictionary has two keys: 'prompt' and 'output'.

**Raises:**

- ValueError: When the input prompt is empty or invalid.
- TypeError: When the input prompt is not a string.
**Examples:**

```python
>>> validated_prompt = validate_prompt('example input')
{'prompt': 'example input', 'output': 'Example Input'}
```

```python
>>> validated_prompt = validate_prompt('another input')
{'prompt': 'another input', 'output': 'Another Input'}
```



---

## generate_story_title

### Description
Generates a story title based on a given input prompt.

### Conceptual Info

A shim node to generate a story title based on a given input prompt.

### Docstring

**Summary:** Generates a story title from a given input prompt using natural language processing techniques.

**Parameters:**

- prompt (str): Input prompt to base the story title on.
**Returns:** str - Generated story title.

**Raises:**

- ValueError: When input prompt is empty or None.
- TypeError: When input prompt is of incorrect type.
**Examples:**

```python
>>> story_title = generate_story_title('A tale of adventure')
'A Tale of Adventure'
```

```python
>>> story_title = generate_story_title('A story of friendship')
'A Story of Friendship'
```



---

## generate_chapter_titles

### Description
Returns a list of chapter titles given a prompt and a story title.

### Conceptual Info

The generate_chapter_titles shim generates chapter titles based on a prompt and story title.

### Docstring

**Summary:** Generate chapter titles given a prompt and story title.

**Parameters:**

- prompt (str): Input prompt used to generate chapter titles.
- story_title (str): Story title used to generate chapter titles.
**Returns:** List[str] - A list of chapter titles.

**Raises:**

- ValueError: If either prompt or story title is empty.
- TypeError: If prompt or story title is not a string.
**Examples:**

```python
>>> from story_gen_shims import generate_chapter_titles
>>> chapter_titles = generate_chapter_titles('Example prompt', 'Example story title')
>>> print(chapter_titles)
['Chapter 1', 'Chapter 2', 'Chapter 3']
```



---

## generate_chapter_bullet_points

### Description
This shim function generates three bullet points summarizing a chapter of a story.

### Conceptual Info

This shim function plays a role in generating story outlines by summarizing chapters in bullet points.

### Docstring

**Summary:** Generate three bullet points summarizing a chapter of a story, given a prompt, chapter number, and chapter title.

**Parameters:**

- prompt (str): A markdown prompt for the chapter.
- chapter_number (str): The number of the chapter (e.g., 1 for Chapter 1).
- chapter_title (str): The title of the chapter.
**Returns:** LIST_STR - A list of three bullet points summarizing the chapter. Each point is a string.

**Raises:**

- ValueError: If the prompt, chapter number, or chapter title is missing or invalid.
- TypeError: If the input types (prompt, chapter number, and chapter title) are incorrect.
**Examples:**

```python
>>> generate_chapter_bullet_points('This is a chapter about ...', 1, 'Chapter 1 Title')
["Bullet point 1", "Bullet point 2", "Bullet point 3"]
```

```python
>>> generate_chapter_bullet_points('This is another chapter about ...', 2, 'Chapter 2 Title')
["Another bullet point 1", "Another bullet point 2", "Another bullet point 3"]
```



---

## generate_dog_favorite_color

### Description
This shim function extracts and generates a dog's favorite color based on the provided story context and prompt.

### Conceptual Info

This shim function determines the dog's favorite color based on story context and prompt, facilitating personalized story elements.

### Docstring

**Summary:** Extracts and generates a string representing the dog's favorite color from the given story context and prompt, requiring implementation to interpret context and produce an appropriate color.

**Parameters:**

- prompt (str): A descriptive prompt used for generating the dog's favorite color.
- story_context (str): The context of the story, such as the story title, that informs the color generation.
**Returns:** str - A string indicating the dog's favorite color, such as 'blue', 'red', or 'green'.

**Raises:**

- ValueError: Raised if the input parameters are invalid or cannot be interpreted properly.
- TypeError: Raised if the input parameters are not of type str.
**Examples:**

```python
>>> generate_dog_favorite_color('Describe the dog', 'A story about a brave dog')
'blue'
```

```python
>>> generate_dog_favorite_color('Favorite color for a playful dog', 'Adventure in the park')
'green'
```

