# inject_style PRD

## Description
Add CSS styling rules


## Conceptual Info

The `inject_style` node generates a string of CSS style rules tailored for the base HTML document produced by `generate_html_content`. It ensures that the styles are responsive and compatible across modern browsers, embedding them within a `<style>` tag that can later be merged into the final HTML output.

## Docstring

### Summary
Generate responsive CSS rules from the base HTML skeleton.

### Parameters

- **html_structure** (str): Base HTML5 document skeleton produced by `generate_html_content`. Expected to contain a `<head>` tag where style rules can be inserted.

### Returns

str: CSS rules wrapped in a `<style>` tag that can be injected into the HTML document.

### Raises

- ValueError: Raised if `html_structure` is empty or does not include a `<head>` element.
- RuntimeError: Raised if internal CSS generation fails due to unexpected parsing errors.

### Examples

```python
>>> html = "<html><head></head><body>Sample</body></html>"
>>> css = inject_style(html)
>>> print(css)
"<style>\n/* Responsive base styles */\nbody { margin:0; font-family:Arial, sans-serif; }\n@media (max-width: 600px) { body { background:#f0f0f0; } }\n</style>"
```

```python
>>> try:
...     inject_style("<html><body>No head</body></html>")
>>> except ValueError as e:
...     print(e)
"Error: Input HTML must contain a <head> element."
```
