# format_exception_message PRD

## Description
Formats exception messages for specific musician IDs.


## Conceptual Info

This shim function is responsible for formatting exception messages that occur during the processing of musician data. It takes in the exception details and the associated musician ID, and returns a formatted message that can be used for logging or further processing.

## Docstring

### Summary
Formats an exception message with the musician ID and exception details.

### Parameters

- **exception** (str): The exception details to be formatted into the message.
- **musician_id** (str): The ID of the musician associated with the exception.

### Returns

str: The formatted exception message containing the musician ID and exception details.

### Raises

- TypeError: If the input types are not as expected (e.g., exception or musician_id are not strings).
- ValueError: If the input values are invalid (e.g., empty strings).

### Examples

```python
>>> format_exception_message(exception='Error: Network failure', musician_id='M1234')
'Error processing musician M1234: Error: Network failure'
```

```python
>>> format_exception_message(exception='Invalid data format', musician_id='M5678')
'Error processing musician M5678: Invalid data format'
```
