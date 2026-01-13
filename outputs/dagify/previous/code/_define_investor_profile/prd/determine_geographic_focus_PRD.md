# determine_geographic_focus PRD

## Description
Derives a geographic focus description for a fund based on investor demographics and regulatory requirements.


## Conceptual Info

This shim encapsulates the logic that interprets investor demographic data and applicable regulatory constraints to generate a concise geographic focus for a new investment fund, enabling downstream components to align strategy and compliance.

## Docstring

### Summary
Determine the geographic focus of a fund from investor demographics and regulatory requirements.

### Parameters

- **investor_demographics** (str): JSON‑encoded string representing the target investor base, e.g., `{"types": ["family office", "pension fund"], "regions": ["North America", "Europe"]}`.
- **regulatory_requirements** (str): JSON‑encoded string of applicable regulatory constraints, e.g., `{"EU": true, "US": false}`.

### Returns

str: A plain‑text sentence stating the fund's geographic focus, such as "The fund will primarily invest in North America and Europe, complying with EU investment regulations."

### Raises

- ValueError: Raised when either input string is empty or fails to provide required keys.
- TypeError: Raised when the input types are not strings.

### Examples

```python
>>> investor_demographics = "{\"types\": [\"family office\", \"pension fund\"], \"regions\": [\"North America\", \"Europe\"]}"
>>> regulatory_requirements = "{\"EU\": true, \"US\": false}"
>>> result = determine_geographic_focus(investor_demographics, regulatory_requirements)
>>> print(result)
"The fund will primarily invest in North America and Europe, complying with EU investment regulations."
```

```python
>>> investor_demographics = "{\"types\": [\"family office\"], \"regions\": [\"Asia\"]}"
>>> regulatory_requirements = "{\"EU\": false, \"US\": false}"
>>> print(determine_geographic_focus(investor_demographics, regulatory_requirements))
"The fund will primarily invest in Asia with no specific regulatory constraints."
```
