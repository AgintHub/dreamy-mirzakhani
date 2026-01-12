# manage_snackbar_notifications PRD

## Description
Manages snackbar notifications based on the state and success/error status.


## Conceptual Info

This shim manages snackbar notifications based on the application state and success/error status, providing a standardized way to handle notifications across the application.

## Docstring

### Summary
Manages snackbar notifications based on the application state and success/error status.

### Parameters

- **state** (str): The current state of the application, used to determine the snackbar notification status.
- **success** (str): A boolean indicating whether the operation was successful.
- **error** (str): An optional error message if the operation failed.

### Returns

str: A dictionary containing the snackbar notification data, including visibility and message.

### Raises

- ValueError: If the state is not a valid string or if success is not a valid boolean representation.
- TypeError: If the input types are incorrect, such as state not being a string or success/error not being strings that can be interpreted as boolean or error message respectively.

### Examples

```python
>>> manage_snackbar_notifications(state='initial_state', success='True')
>>> manage_snackbar_notifications(state='error_state', success='False', error='Error message')
{'visible': True, 'message': 'Operation successful'}
```

```python
>>> manage_snackbar_notifications(state='initial_state', success='True')
>>> manage_snackbar_notifications(state='error_state', success='False', error='Error message')
{'visible': True, 'message': 'Error message'}
```
