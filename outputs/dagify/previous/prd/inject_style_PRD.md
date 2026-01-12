# inject_style PRD

## Description
Add CSS styling rules to an existing HTML document skeleton.


## Conceptual Info

Provides responsive CSS rules that are injected into a basic HTML5 document skeleton, enabling layout, typography, and visual theming.

## Docstring

### Summary
Generates a string of CSS style rules tailored to the supplied HTML skeleton. The function ensures the resulting CSS is responsive and minimally invasive, suitable for immediate inclusion in a `<style>` tag.

### Parameters

- **html_structure** (str): Base HTML5 document skeleton. The function analyzes the presence of common containers (header, nav, main, footer) to inject context‑aware styles.

### Returns

str: A CSS string containing responsive style rules that can be inserted into the `<head>` of the HTML document.

### Raises

- ValueError: Raised when `html_structure` is an empty string or contains only whitespace.
- TypeError: Raised when `html_structure` is not of type `str`.

### Examples

```python
>>> skeleton = """\
>>> <!DOCTYPE html>\
>>> <html>\
>>> <head>\
...   <title>Test Page</title>\
>>> </head>\
>>> <body>\
...   <header></header>\
...   <main></main>\
...   <footer></footer>\
>>> </body>\
>>> </html>"""
>>> css = inject_style(skeleton)
>>> print(css)
"""\n/* Base responsive styles */\nbody {\n  margin: 0;\n  font-family: Arial, sans-serif;\n  display: flex;\n  flex-direction: column;\n  min-height: 100vh;\n}\nheader, footer {\n  background: #f8f9fa;\n  padding: 1rem;\n}\nmain {\n  flex: 1;\n  padding: 1rem;\n}\n@media (min-width: 600px) {\n  main {\n    padding: 2rem;\n  }\n}\n"""
```

```python
>>> skeleton = "<!DOCTYPE html><html><head><title></title></head><body></body></html>"
>>> css = inject_style(skeleton)
>>> print(css)
"""\n/* Base responsive styles */\nbody {\n  margin: 0;\n  font-family: Arial, sans-serif;\n  display: flex;\n  flex-direction: column;\n  min-height: 100vh;\n}\n"""
```
