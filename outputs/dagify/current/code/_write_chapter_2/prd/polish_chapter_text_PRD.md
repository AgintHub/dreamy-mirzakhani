# polish_chapter_text PRD

## Description
Polishes the text of a chapter by processing its syntax and style, resulting in refined prose.


## Conceptual Info

This shim node's purpose is to refine the text of a chapter by processing its syntax and style, ultimately enhancing the narrative and engaging the reader.

## Docstring

### Summary
Polishes the text of a chapter by processing its syntax and style, resulting in refined prose.

### Parameters

- **raw_text** (str): The raw chapter text in its original state
- **story_context** (str): The narrative context of the chapter, including previous events and character interactions

### Returns

STR: The polished chapter text in prose format

### Raises

- ValueError: When the input text is invalid or cannot be processed.
- TypeError: When the input type is incorrect or missing.

### Examples

```python
>>> polished_chapter = polish_chapter_text('This is a raw chapter text.', 'This is the narrative context.')
'This is the polished chapter text.'
```

```python
>>> polished_chapter = polish_chapter_text('Another raw chapter text.', '')
'Another polished chapter text.'
```
