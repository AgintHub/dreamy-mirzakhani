# convert_to_base64 PRD

## Description
Converts binary data to a base64-encoded string representation.


## Conceptual Info

This shim node is responsible for converting binary data into a base64-encoded string, which is useful for representing binary data in text formats.

## Docstring

### Summary
Converts binary data to a base64-encoded string.

### Parameters

- **binary_data** (str): The binary data to be converted to base64 encoding.

### Returns

str: The base64-encoded string representation of the input binary data.

### Raises

- TypeError: If the input binary_data is not of type str.
- ValueError: If the input binary_data is not valid binary data.

### Examples

```python
>>> binary_data = 'Hello, World!'
>>> base64_encoded = convert_to_base64(binary_data=binary_data.encode('utf-8'))
>>> print(base64_encoded)
'SGVsbG8sIFdvcmxkIQ=='
```

```python
>>> binary_data = 'example'
>>> base64_encoded = convert_to_base64(binary_data=binary_data.encode('utf-8'))
>>> print(base64_encoded)
'ZXhhbXBsZQ=='
```
