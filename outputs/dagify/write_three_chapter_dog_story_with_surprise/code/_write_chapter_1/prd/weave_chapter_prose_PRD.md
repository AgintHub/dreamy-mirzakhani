# weave_chapter_prose PRD

## Description
Creates a well-formed, cohesive chapter by interweaving the opening scene, chapter body, and color themes.


## Conceptual Info

This shim node plays a crucial role in creating a coherent chapter, which is a critical component of a story. It receives inputs for the opening scene, chapter body, and color themes, and returns a formatted chapter text.

## Docstring

### Summary
Creates a chapter by weaving together opening scene, chapter body, and color themes.

### Parameters

- **opening_scene** (str): The opening scene of the chapter, setting the tone and introducing the main elements.
- **chapter_body** (str): The body of the chapter, elaborating on the opening scene and advancing the plot.
- **color_themes** (str): The color themes that permeate the chapter, adding a visual and emotional depth.

### Returns

str: A well-formatted chapter text, incorporating the provided inputs and meeting the requirements of a cohesive narrative.

### Raises

- ValueError: Raised when the input parameters are invalid or incomplete, preventing the creation of a coherent chapter.
- TypeError: Raised when the input parameters have incorrect types, hindering the formation of a well-structured chapter.

### Examples

```python
>>> weave_chapter_prose(opening_scene='The dark forest loomed before us.', chapter_body='As we ventured deeper, the trees seemed to close in, their branches creaking ominously.', color_themes='The red moon cast an eerie glow over the forest, while the trees seemed to absorb the faint light, making it almost invisible.')
>>> complete_chapter = chapter_text
The dark forest loomed before us. As we ventured deeper, the trees seemed to close in, their branches creaking ominously. The red moon cast an eerie glow over the forest, while the trees seemed to absorb the faint light, making it almost invisible.
```
