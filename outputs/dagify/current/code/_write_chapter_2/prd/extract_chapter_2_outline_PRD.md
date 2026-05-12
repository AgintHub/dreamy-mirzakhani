# extract_chapter_2_outline PRD

## Description
Typed node for shim extract_chapter_2_outline that extracts the chapter 2 outline from a given story outline and bullet points.


## Conceptual Info

This shim function is responsible for extracting the chapter 2 outline from a given story outline and bullet points.

## Docstring

### Summary
Extracts the chapter 2 outline from a given story outline and bullet points.

### Parameters

- **outline** (str): The story outline as a string
- **bullet_points** (str): The chapter 2 bullet points as a string

### Returns

PRIMITIVEType.STR dict: The extracted chapter 2 outline as a dictionary with string values

### Raises

- ValueError: When the input outline or bullet points are invalid
- TypeError: When the input type is incorrect

### Examples

```python
>>> output = extract_chapter_2_outline('story_outline', 'chapter_2_bullet_points')
>>> print(output)
{'chapter_2_heading': 'Chapter 2 Heading', 'chapter_2_subheading': 'Chapter 2 Subheading'}
```

```python
>>> output = extract_chapter_2_outline('story_outline_with_error', 'chapter_2_bullet_points_with_error')
>>> print(output)
ValueError: Invalid input outline
```
