# inject_script PRD

## Description
Add JavaScript interactivity


## Conceptual Info

Creates a JavaScript snippet that can be injected into an existing HTML skeleton to provide client‑side interactivity.

## Docstring

### Summary
Injects a dynamic JavaScript snippet into the provided HTML structure, returning the script tag string.

### Parameters

- **html_structure** (str): Base HTML document skeleton produced by generate_html_content.

### Returns

str: A JavaScript snippet wrapped in `<script>` tags, ready to be injected into the final HTML document.

### Raises

- ValueError: If `html_structure` is an empty string.
- TypeError: If `html_structure` is not of type `str`.

### Examples

```python
>>> js_code = inject_script('<html><head></head><body></body></html>')
'<script>/* dynamic JS */</script>'
```

```python
>>> try:
...     inject_script('')
>>> except ValueError as e:
...     print(e)
"html_structure cannot be empty."
```
