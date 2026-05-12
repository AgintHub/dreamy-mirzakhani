# generate_chapter_bullet_points PRD

## Description
This shim function generates three bullet points summarizing a chapter of a story.


## Conceptual Info

This shim function plays a role in generating story outlines by summarizing chapters in bullet points.

## Docstring

### Summary
Generate three bullet points summarizing a chapter of a story, given a prompt, chapter number, and chapter title.

### Parameters

- **prompt** (str): A markdown prompt for the chapter.
- **chapter_number** (str): The number of the chapter (e.g., 1 for Chapter 1).
- **chapter_title** (str): The title of the chapter.

### Returns

LIST_STR: A list of three bullet points summarizing the chapter. Each point is a string.

### Raises

- ValueError: If the prompt, chapter number, or chapter title is missing or invalid.
- TypeError: If the input types (prompt, chapter number, and chapter title) are incorrect.

### Examples

```python
>>> generate_chapter_bullet_points('This is a chapter about ...', 1, 'Chapter 1 Title')
["Bullet point 1", "Bullet point 2", "Bullet point 3"]
```

```python
>>> generate_chapter_bullet_points('This is another chapter about ...', 2, 'Chapter 2 Title')
["Another bullet point 1", "Another bullet point 2", "Another bullet point 3"]
```
