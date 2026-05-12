# write_chapter_3 PRD

## Description
Writes Chapter 3, receiving Chapter 2 output to conclude the story.


## Conceptual Info

This node is responsible for crafting the final chapter of the story, incorporating the plot developments from Chapter 2 and setting the scene for a satisfying conclusion.

## Docstring

### Summary
Generates the final chapter of the story, using the provided outline, character profiles, and setting to conclude the dog's adventure.

### Parameters

- **chapter_2_output** (str): The complete text of Chapter 2.

### Returns

dict[str, str]: Contains the title, content, and summary of the final chapter.

### Raises

- TypeError: If chapter_2_output is not a string.

### Examples

```python
>>> final_chapter = write_chapter_3(chapter_2_output)
>>> print(final_chapter['chapter_title'])
>>> print(final_chapter['chapter_content'])
>>> print(final_chapter['chapter_summary'])
Chapter Title: The Final Chapter
Chapter Content: The final chapter of the story.
Chapter Summary: The dog's adventure concludes with ​​.
```
