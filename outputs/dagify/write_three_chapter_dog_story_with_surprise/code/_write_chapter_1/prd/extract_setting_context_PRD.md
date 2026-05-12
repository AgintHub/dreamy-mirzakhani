# extract_setting_context PRD

## Description
Extracts a setting context dictionary from a given story setting string.


## Conceptual Info

extract_setting_context is a shim node responsible for taking a story setting string and transforming it into a JSON-formatted dictionary. Its primary role is to provide a standardized way of handling story setting inputs, making it easier to integrate with other nodes in the system.

## Docstring

### Summary
This function takes a story setting string as input and returns a dictionary containing the extracted setting context.

### Parameters

- **story_setting** (str): The story setting string from which the setting context will be extracted.

### Returns

dict: A dictionary containing the setting context, with keys representing the different setting elements and values representing their corresponding values.

### Raises

- ValueError: If the input story setting string is malformed or missing required elements.
- TypeError: If the input story setting string cannot be properly converted to a dictionary.

### Examples

```python
>>> extract_setting_context('location: city, time_period: past, environmental_details: sunny')
>>> print(extract_setting_context('location: forest, time_period: present, environmental_details: rainy'))
{"location": "forest", "time_period": "present", "environmental_details": "rainy"}
```

```python
>>> extract_setting_context('invalid setting string')
>>> print(extract_setting_context('missing required elements'))
ValueError: Invalid story setting string
```
