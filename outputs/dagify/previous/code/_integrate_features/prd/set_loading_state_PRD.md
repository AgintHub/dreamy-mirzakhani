# set_loading_state PRD

## Description
Sets the loading state of the application UI to the specified state.


## Conceptual Info

This shim function is responsible for updating the loading state of the application's UI, reflecting the current status of ongoing operations.

## Docstring

### Summary
Updates the loading state of the application UI based on the provided state and loading status.

### Parameters

- **state** (str): The current state of the application, represented as a string.
- **loading** (str): The loading state to be set, which can be 'loading', 'success', or 'error'.

### Returns

str: The updated loading state of the application UI.

### Raises

- ValueError: If the 'loading' parameter is not one of 'loading', 'success', or 'error'.
- TypeError: If either 'state' or 'loading' is not a string.

### Examples

```python
>>> set_loading_state(state='initial_state', loading='loading')
'loading'
```

```python
>>> set_loading_state(state='initial_state', loading='success')
'success'
```
