# select_test_tools PRD

## Description
Choose testing technologies and platforms


## Conceptual Info

Selects the most appropriate testing tools based on the scope identified by the parent node, ensuring coverage of functional, performance, and security requirements.

## Docstring

### Summary
Selects testing tools and provides concise justifications.

### Parameters

- **tested_features** (List[str]): Names of features, systems, or processes that will be tested, as provided by the output of `identify_test_scope`.
- **excluded_features** (List[str]): Names of features, systems, or processes that are explicitly excluded from testing, as provided by the output of `identify_test_scope`.

### Returns

Dict[str, List[str]]: A dictionary with two keys: `tools`, a list of tool names, and `justifications`, a list of one‑phrase explanations corresponding to each tool.

### Raises

- ValueError: If either `tested_features` or `excluded_features` is empty or not a list.
- RuntimeError: If no suitable tools can be identified for the provided scope.

### Examples

```python
>>> selected = select_test_tools(tested_features=["Login", "API"], excluded_features=["Documentation"])
{
  "tools": ["Selenium", "Postman", "OWASP ZAP"],
  "justifications": ["Automated UI testing", "API contract testing", "Dynamic security scanning"]
}
```

```python
>>> selected = select_test_tools(tested_features=["Payment Gateway"], excluded_features=["Legacy System"])
{
  "tools": ["JMeter", "Burp Suite"],
  "justifications": ["Performance/load testing", "Penetration testing"]
}
```
