# analyze_jurisdictions PRD

## Description
Analyze a list of candidate jurisdictions against tax, regulatory, and investor criteria to produce a structured assessment dictionary.


## Conceptual Info

This shim serves as the core decision‑support engine that evaluates each candidate jurisdiction on multiple dimensions—tax efficiency, regulatory simplicity, and investor appeal—and returns a comprehensive, machine‑readable analysis for downstream selection logic.

## Docstring

### Summary
Evaluates candidate jurisdictions against specified criteria and returns a detailed analysis as a JSON string.

### Parameters

- **candidates** (List[str]): A list of jurisdiction names (e.g., ['Cayman Islands', 'Bermuda']) to be evaluated.
- **tax_requirements** (str): A short description of the desired tax efficiency (e.g., 'low withholding tax', 'zero corporate tax').
- **regulatory_preferences** (str): A short description of preferred regulatory characteristics (e.g., 'fast registration', 'minimal reporting').
- **investor_targets** (str): A short description of the target investor profile (e.g., 'high net worth individuals', 'institutional investors').

### Returns

str: A JSON‑formatted string containing a dictionary. Each key is a jurisdiction name; each value is a dictionary with keys such as 'tax_score', 'regulatory_score', 'investor_score', 'advantages', 'disadvantages', and 'summary'.

### Raises

- ValueError: Raised when the candidates list is empty or any required criterion string is missing or empty.
- TypeError: Raised when any argument is not of the expected type.

### Examples

```python
>>> result = analyze_jurisdictions(

...     candidates=['Cayman Islands', 'Bermuda'],

...     tax_requirements='zero corporate tax',

...     regulatory_preferences='fast registration',

...     investor_targets='high net worth individuals'

>>> )
"{\n  \"Cayman Islands\": {\n    \"tax_score\": 9,\n    \"regulatory_score\": 8,\n    \"investor_score\": 7,\n    \"advantages\": [\"Low tax\", \"Robust financial sector\"],\n    \"disadvantages\": [\"Limited banking options\", \"High setup costs\"],\n    \"summary\": \"Suitable for private equity funds targeting high net worth investors.\"\n  },\n  \"Bermuda\": {\n    \"tax_score\": 8,\n    \"regulatory_score\": 7,\n    \"investor_score\": 8,\n    \"advantages\": [\"No capital gains tax\", \"Strong legal framework\"],\n    \"disadvantages\": [\"Regulatory scrutiny\", \"Higher operational costs\"],\n    \"summary\": \"Good for funds focused on institutional investors.\"\n  }\n}"
```

```python
>>> try:
...     analyze_jurisdictions([], 'zero tax', 'fast', 'individuals')
>>> except ValueError as e:
...     print(e)
"candidates list cannot be empty"
```
