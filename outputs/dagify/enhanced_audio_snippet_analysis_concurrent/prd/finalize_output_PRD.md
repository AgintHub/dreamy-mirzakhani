# finalize_output PRD

## Description
Combine all document components


## Conceptual Info

The node merges a base HTML skeleton with injected CSS styles and JavaScript code, producing a ready‑to‑serve HTML document. It validates that each component is correctly formatted, reports any syntactic or semantic issues, and returns a rendering status flag.

## Docstring

### Summary
Merge base HTML with CSS and JavaScript injections to produce a complete HTML document.

### Parameters

- **html_structure** (str): Base HTML skeleton (e.g., output from generate_html_content).
- **css_injection** (str): CSS style block or link tags to be injected (e.g., output from inject_style).
- **js_injection** (str): JavaScript script block or external script tags to be injected (e.g., output from inject_script).

### Returns

dict: Dictionary containing `final_html` (str), `render_status` (bool), and `render_errors` (List[str]).

### Raises

- ValueError: Raised when any input string is empty or None.
- SyntaxError: Raised when the combined HTML contains unmatched tags or malformed structure.

### Examples

```python
>>> html = '<html><head></head><body></body></html>'
>>> css = '<style>body{background:#f0f0f0;}</style>'
>>> js = '<script>console.log("Hello, world!");</script>'
>>> result = finalize_output(html, css, js)
{'final_html': '<html><head><style>body{background:#f0f0f0;}</style></head><body><script>console.log("Hello, world!");</script></body></html>', 'render_status': true, 'render_errors': []}
```

```python
>>> html = '<html><head></head><body></body>'
>>> css = '<style>body{color:red;}</style>'
>>> js = ''
>>> result = finalize_output(html, css, js)
{'final_html': '', 'render_status': false, 'render_errors': ['Malformed HTML: missing closing tag for <html>']}
```
