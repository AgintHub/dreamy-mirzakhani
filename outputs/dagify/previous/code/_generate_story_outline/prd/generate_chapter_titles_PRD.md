# generate_chapter_titles PRD

## Description
Returns a list of chapter titles given a prompt and a story title.


## Conceptual Info

The generate_chapter_titles shim generates chapter titles based on a prompt and story title.

## Docstring

### Summary
Generate chapter titles given a prompt and story title.

### Parameters

- **prompt** (str): Input prompt used to generate chapter titles.
- **story_title** (str): Story title used to generate chapter titles.

### Returns

List[str]: A list of chapter titles.

### Raises

- ValueError: If either prompt or story title is empty.
- TypeError: If prompt or story title is not a string.

### Examples

```python
>>> from story_gen_shims import generate_chapter_titles
>>> chapter_titles = generate_chapter_titles('Example prompt', 'Example story title')
>>> print(chapter_titles)
['Chapter 1', 'Chapter 2', 'Chapter 3']
```
