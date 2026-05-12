# create_chapter_structure PRD

## Description
Creates a structured dictionary for a chapter based on provided bullet points and story title.


## Conceptual Info

This shim creates a structured chapter structure based on user-provided bullet points and story title.

## Docstring

### Summary
Creates a dictionary representing a chapter based on bullet points and story title.

### Parameters

- **chapter_bullet_points** (str): String containing bullet points for the chapter.
- **story_title** (str): String containing the story title.

### Returns

dict: A dictionary representing the chapter content with keys for bullet points and story title.

### Raises

- ValueError: If the input parameters are not valid.
- TypeError: If the input parameters are not strings.

### Examples

```python
>>> create_chapter_structure('Chapter 1 bullet points', 'Story Title')
{'bullet_points': 'Chapter 1 bullet points', 'story_title': 'Story Title'}
```

```python
>>> create_chapter_structure('Another chapter bullet points', 'Another Story Title')
{'bullet_points': 'Another chapter bullet points', 'story_title': 'Another Story Title'}
```
