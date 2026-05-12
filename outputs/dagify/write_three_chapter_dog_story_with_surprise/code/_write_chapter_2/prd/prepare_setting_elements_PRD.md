# prepare_setting_elements PRD

## Description
A shim function that prepares setting elements from the provided story setting and environmental details.


## Conceptual Info

The `prepare_setting_elements` shim prepares setting elements for the story setting and environmental details by extracting relevant information and processing it into a usable format.

## Docstring

### Summary
Prepare setting elements from the provided story setting and environmental details.

### Parameters

- **setting** (STR): Input story setting to be used for setting element preparation.
- **environmental_details** (STR): Input environmental details to be used for setting element preparation.

### Returns

STR: Processed setting elements in dictionary format, including location, time period, environmental factors, and the protagonist's favorite color.

### Raises

- ValueError: When input validation fails, such as invalid story setting or environmental details format.
- TypeError: When input types are incorrect, such as non-string input for setting or environmental details.

### Examples

```python
>>> from prepare_setting_elements import prepare_setting_elements
>>> setting = 'a futuristic city on a distant planet'
>>> environmental_details = 'scorching heat, dense pollution, strict social hierarchy'
>>> prep_setting_elements_output = prepare_setting_elements(setting, environmental_details)
>>> print(prep_setting_elements_output)
(
              "{"
              "  'setting': 'a futuristic city on a distant planet',"
              "  'environmental_details': 'scorching heat, dense pollution, strict social hierarchy',"
              "  'prepared_elements': {"
              "    'location': 'distant planet',"
              "    'time_period': 'indeterminate',"
              "    'environmental_factors': ['scorching heat', 'dense pollution'],"
              "    'protagonist_favorite_color': 'red'"
              "
```
