# inject_style PRD

## Description
Add CSS styling rules to an existing HTML document skeleton.


## Conceptual Info

The `inject_style` node injects a responsive CSS block into a base HTML skeleton, returning the CSS as a string that can be embedded into the document.

## Docstring

### Summary
Inject responsive CSS rules into an existing HTML skeleton.

### Parameters

- **html_structure** (str): Base HTML5 document skeleton. Must contain at least `<html>` and `<head>` tags.

### Returns

str: CSS style block string that should be inserted inside the `<head>` of the provided HTML.

### Raises

- ValueError: If `html_structure` is not a valid HTML string or lacks `<head>` tags.

### Examples

```python
>>> html = """\
>>> <html>\
...   <head>\
...   </head>\
...   <body>\
...     <h1>Hello World</h1>\
...   </body>\
>>> </html>\
>>> """
>>> css = inject_style(html)
>>> print(css)
"<style>\n  body {margin:0; font-family:sans-serif;}\n  @media (max-width:600px) {h1 {font-size:1.5rem;}}\n</style>"
```

```python
>>> html_missing_head = "<html><body><p>No head</p></body></html>"
>>> try:
...     inject_style(html_missing_head)
>>> except ValueError as e:
...     print(str(e))
"ValueError: html_structure must contain a <head> element"
```
