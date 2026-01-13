# extract_jurisdiction_advantages PRD

## Description
Returns a list of two key advantages for a specified jurisdiction based on analysis data.


## Conceptual Info

The shim extracts the top advantages of a jurisdiction from a pre‑computed analysis dictionary to inform fund domicile selection.

## Docstring

### Summary
Extracts the two most relevant advantages of the specified jurisdiction from the provided analysis data.

### Parameters

- **jurisdiction** (str): Name of the jurisdiction whose advantages are to be extracted.
- **analysis** (dict): Dictionary containing detailed analysis information keyed by jurisdiction names.

### Returns

List[str]: A list containing two strings, each describing a key advantage of the jurisdiction.

### Raises

- KeyError: Raised when the jurisdiction key is missing from the analysis dictionary.
- ValueError: Raised when the extracted advantages list does not contain exactly two items.
- TypeError: Raised if inputs are not of the expected types.

### Examples

```python
>>> analysis_data = {
...     'Cayman Islands': {
...         'advantages': ['No direct taxes', 'Strong confidentiality laws'],
...         'disadvantages': ['Limited local market', 'High regulatory scrutiny']
...     }
>>> }
>>> extract_jurisdiction_advantages('Cayman Islands', analysis_data)
['No direct taxes', 'Strong confidentiality laws']
```

```python
>>> analysis_data = {
...     'Delaware': {
...         'advantages': ['Favorable corporate law', 'Established legal framework'],
...         'disadvantages': ['Higher filing fees', 'Limited privacy']
...     }
>>> }
>>> extract_jurisdiction_advantages('Delaware', analysis_data)
['Favorable corporate law', 'Established legal framework']
```
