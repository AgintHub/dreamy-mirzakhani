# inject_script PRD

## Description
Add JavaScript interactivity


## Conceptual Info

Injects JavaScript to enhance the base HTML with dynamic interactivity.

## Docstring

### Summary
Generates JavaScript code that adds event listeners and dynamic behavior to the supplied HTML structure.

### Parameters

- **html_structure** (str): Base HTML skeleton string produced by `generate_html_content`.

### Returns

str: JavaScript code snippet that implements interactivity for the HTML document.

### Raises

- ValueError: Raised when `html_structure` is empty or not a string.

### Examples

```python
>>> js_code = inject_script('<!DOCTYPE html><html><head></head><body></body></html>')
"// JavaScript that attaches click listeners to all <button> elements\n" +
"document.addEventListener('DOMContentLoaded', () => {\n" +
"  document.querySelectorAll('button').forEach(btn => btn.addEventListener('click', () => alert('Clicked!')));\n" +
"});\n"
```

```python
>>> html = ('<!DOCTYPE html><html><head></head><body>' +
...        '<div id="counter">0</div>' +
...        '<button id="inc">Increment</button>' +
...        '</body></html>')
>>> js_code = inject_script(html)
"// JavaScript that increments a counter on button click\n" +
"document.addEventListener('DOMContentLoaded', () => {\n" +
"  const counter = document.getElementById('counter');\n" +
"  const incBtn = document.getElementById('inc');\n" +
"  incBtn.addEventListener('click', () => {\n" +
"    counter.textContent = parseInt(counter.textContent) + 1;\n" +
"  });\n" +
"});\n"
```
